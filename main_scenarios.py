# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:49:18 2016

@author: ruthpearson
"""
from __future__ import division

import model as modelCode
import data as dataCode
import constants as constantsCode
import parameters as parametersCode
import output as output



ages = ["<1 month", "1-5 months", "6-11 months", "12-23 months", "24-59 months"]
birthOutcomes = ["Pre-term SGA", "Pre-term AGA", "Term SGA", "Term AGA"]
wastingList = ["normal", "mild", "moderate", "high"]
stuntingList = ["normal", "mild", "moderate", "high"]
breastfeedingList = ["exclusive", "predominant", "partial", "none"]
keyList = [ages, birthOutcomes, wastingList, stuntingList, breastfeedingList]

spreadsheetData = dataCode.getDataFromSpreadsheet('InputForCode.xlsx', keyList)

mothers = modelCode.FertileWomen(0.9, 2.e6)

ageRangeList  = ages 
agingRateList = [1./1., 1./5., 1./6., 1./12., 1./36.] # fraction of people aging out per MONTH
numAgeGroups = len(ageRangeList)
agePopSizes  = [1.7e5, 4.e5, 7.e5, 1.44e6, 44.e5]

timestep = 1./12. 
numsteps = 168
timespan = timestep * float(numsteps)
nstep_eq = 24

for intervention in spreadsheetData.interventionList:
    print "Baseline coverage of %s = %g"%(intervention,spreadsheetData.interventionCoveragesCurrent[intervention])

#-------------------------------------------------------------------------    
def makeBoxes(thisAgePopSize, ageGroup, keyList):
    allBoxes = {}
    ages, birthOutcomes, wastingList, stuntingList, breastfeedingList = keyList
    for stuntingCat in stuntingList:
        allBoxes[stuntingCat] = {} 
        for wastingCat in wastingList:
            allBoxes[stuntingCat][wastingCat] = {}
            for breastfeedingCat in breastfeedingList:
                thisPopSize = thisAgePopSize * spreadsheetData.stuntingDistribution[ageGroup][stuntingCat] * spreadsheetData.wastingDistribution[ageGroup][wastingCat] * spreadsheetData.breastfeedingDistribution[ageGroup][breastfeedingCat]   # Assuming independent
                thisMortalityRate = 0
                allBoxes[stuntingCat][wastingCat][breastfeedingCat] =  modelCode.Box(stuntingCat, wastingCat, breastfeedingCat, thisPopSize, thisMortalityRate)
    return allBoxes

def makeAgeCompartments(agingRateList, agePopSizes, keyList):
    ages, birthOutcomes, wastingList, stuntingList, breastfeedingList = keyList
    numAgeGroups = len(ages)
    listOfAgeCompartments = []
    for age in range(numAgeGroups): # Loop over all age-groups
        ageGroup  = ages[age]
        agingRate = agingRateList[age]
        agePopSize = agePopSizes[age]
        thisAgeBoxes = makeBoxes(agePopSize, ageGroup, keyList)
        compartment = modelCode.AgeCompartment(ageGroup, thisAgeBoxes, agingRate, keyList)
        listOfAgeCompartments.append(compartment)
    return listOfAgeCompartments         
#-------------------------------------------------------------------------  

plotData = []
run = 0

#------------------------------------------------------------------------    
# DEFAULT RUN WITH NO CHANGES TO INTERVENTIONS
nametag = "Baseline"
pickleFilename = 'testDefault.pkl'
plotcolor = 'grey'

print "\n"+nametag
listOfAgeCompartments = makeAgeCompartments(agingRateList, agePopSizes, keyList)
model = modelCode.Model(nametag, mothers, listOfAgeCompartments, keyList, timestep)
constants = constantsCode.Constants(spreadsheetData, model, keyList)
model.setConstants(constants)
params = parametersCode.Params(spreadsheetData, constants, keyList)
model.setParams(params)
model.updateMortalityRate()

# Find equilibrium
for t in range(nstep_eq):
    model.moveOneTimeStep()

# file to dump objects into at each time step
import pickle as pickle
outfile = open(pickleFilename, 'wb')

# Run model
for t in range(numsteps):
    model.moveOneTimeStep()
    pickle.dump(model, outfile)
outfile.close()    

# collect output, make graphs etc.
infile = open(pickleFilename, 'rb')
modelList = []
while 1:
    try:
        modelList.append(pickle.load(infile))
    except (EOFError):
        break
infile.close()

plotData.append({})
plotData[run]["modelList"] = modelList
plotData[run]["tag"] = nametag
plotData[run]["color"] = plotcolor
run += 1

#------------------------------------------------------------------------    
# INTERVENTION
percentageIncrease = 90

for ichoose in range(len(spreadsheetData.interventionList)):
    chosenIntervention = spreadsheetData.interventionList[ichoose]
    #nametag = chosenIntervention+": increase coverage by %g%% points"%(percentageIncrease)
    nametag = chosenIntervention
    pickleFilename = 'test_Intervention%i_P%i.pkl'%(ichoose,percentageIncrease)
    plotcolor = (0.1*run, 1.-0.1*run, 0.3+0.05*run)
    print "\n"+nametag

    listOfAgeCompartments = makeAgeCompartments(agingRateList, agePopSizes, keyList)
    modelX = modelCode.Model("Increased Coverage model", mothers, listOfAgeCompartments, keyList, timestep)
    constants = constantsCode.Constants(spreadsheetData, modelX, keyList)
    modelX.setConstants(constants)
    params = parametersCode.Params(spreadsheetData,constants,keyList)
    modelX.setParams(params)
    modelX.updateMortalityRate()

    # Find equilibrium
    for t in range(nstep_eq):
        modelX.moveOneTimeStep()

    # file to dump objects into at each time step
    import pickle as pickle
    outfile = open(pickleFilename, 'wb')
    modelX.moveOneTimeStep()
    pickle.dump(modelX, outfile)

    # initialise
    newCoverages={}
    for intervention in spreadsheetData.interventionList:
        newCoverages[intervention] = spreadsheetData.interventionCoveragesCurrent[intervention]
    # scale up intervention
    newCoverages[chosenIntervention] += percentageIncrease/100.
    modelX.updateCoverages(newCoverages)

    # Run model
    for t in range(numsteps-1):
        modelX.moveOneTimeStep()
        pickle.dump(modelX, outfile)
    outfile.close()    

    # collect output, make graphs etc.
    infile = open(pickleFilename, 'rb')
    modelXList = []
    while 1:
        try:
            modelXList.append(pickle.load(infile))
        except (EOFError):
            break
    infile.close()

    plotData.append({})
    plotData[run]["modelList"] = modelXList
    plotData[run]["tag"] = nametag
    plotData[run]["color"] = plotcolor
    run += 1


#------------------------------------------------------------------------    
# INTERVENTION
percentageIncrease = 90
nametag = "All interventions: increase coverage by %g%% points"%(percentageIncrease)
pickleFilename = 'test_Intervention_P%i.pkl'%(percentageIncrease)
plotcolor = 'blue'

print "\n"+nametag
listOfAgeCompartments = makeAgeCompartments(agingRateList, agePopSizes, keyList)
modelZ = modelCode.Model("Increased Coverage model", mothers, listOfAgeCompartments, keyList, timestep)
constants = constantsCode.Constants(spreadsheetData, modelZ, keyList)
modelZ.setConstants(constants)
params = parametersCode.Params(spreadsheetData,constants,keyList)
modelZ.setParams(params)
modelZ.updateMortalityRate()

# Find equilibrium
for t in range(nstep_eq):
    modelZ.moveOneTimeStep()

# file to dump objects into at each time step
import pickle as pickle
outfile = open(pickleFilename, 'wb')
modelZ.moveOneTimeStep()
pickle.dump(modelZ, outfile)

# scale up all interventions
# initialise
newCoverages={}
for intervention in spreadsheetData.interventionList:
    newCoverages[intervention] = spreadsheetData.interventionCoveragesCurrent[intervention]
for intervention in spreadsheetData.interventionList:
    newCoverages[intervention] = min(1.0,newCoverages[intervention]+percentageIncrease/100.) 
modelZ.updateCoverages(newCoverages)

for t in range(numsteps-1):
    modelZ.moveOneTimeStep()
    pickle.dump(modelZ, outfile)
outfile.close()    

# collect output, make graphs etc.
infile = open(pickleFilename, 'rb')
newModelList = []
while 1:
    try:
        newModelList.append(pickle.load(infile))
    except (EOFError):
        break
infile.close()

plotData.append({})
plotData[run]["modelList"] = newModelList
plotData[run]["tag"] = nametag
plotData[run]["color"] = plotcolor
run += 1


#------------------------------------------------------------------------    


output.getCombinedPlots(run, plotData)
output.getDeathsAverted(modelList, newModelList, 'test')



