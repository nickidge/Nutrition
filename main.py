# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 13:49:18 2016

@author: ruthpearson
"""
from __future__ import division

import data as dataCode
import output as output
import helper as helper
import pickle as pickle
from copy import deepcopy as dcp
import costcov
from numpy import array

helper = helper.Helper()
costCov = costcov.Costcov()

timestep = 1./12. 
numsteps = 168  
timespan = timestep * float(numsteps)

ages = ["<1 month", "1-5 months", "6-11 months", "12-23 months", "24-59 months"]
birthOutcomes = ["Pre-term SGA", "Pre-term AGA", "Term SGA", "Term AGA"]
wastingList = ["normal", "mild", "moderate", "high"]
stuntingList = ["normal", "mild", "moderate", "high"]
breastfeedingList = ["exclusive", "predominant", "partial", "none"]
keyList = [ages, birthOutcomes, wastingList, stuntingList, breastfeedingList]

spreadsheetData = dataCode.getDataFromSpreadsheet('InputForCode_Kenya.xlsx', keyList)
mothers = helper.makePregnantWomen(spreadsheetData)
mothers['annualPercentPopGrowth'] = 0.03
ageGroupSpans = [1., 5., 6., 12., 36.] # number of months in each age group
agingRateList = [1./1., 1./5., 1./6., 1./12., 1./36.] # fraction of people aging out per MONTH (WARNING use ageSpans to define this)
numAgeGroups = len(ages)
#agePopSizes  = [1.7e5, 4.e5, 7.e5, 1.44e6, 44.e5]
agePopSizes  = helper.makeAgePopSizes(numAgeGroups, ageGroupSpans, spreadsheetData)

for intervention in spreadsheetData.interventionList:
    print "Baseline coverage of %s = %g"%(intervention,spreadsheetData.interventionCoveragesCurrent[intervention])

plotData = []
run = 0

#------------------------------------------------------------------------    
# DEFAULT RUN WITH NO CHANGES TO INTERVENTIONS
nametag = "Baseline"
pickleFilename = 'testDefault.pkl'
plotcolor = 'grey'

print "\n"+nametag
model, constants, params = helper.setupModelConstantsParameters(nametag, mothers, timestep, agingRateList, agePopSizes, keyList, spreadsheetData)

outfile = open(pickleFilename, 'wb')
pickle.dump(model, outfile)
for t in range(numsteps-1):
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
nametag = "Fixed investment"
pickleFilename = 'test_Investment.pkl'
plotcolor = 'green'

print "\n"+nametag
modelZ, constants, params = helper.setupModelConstantsParameters(nametag, mothers, timestep, agingRateList, agePopSizes, keyList, spreadsheetData)


# file to dump objects into at each time step
outfile = open(pickleFilename, 'wb')
pickle.dump(modelZ, outfile)

# initialise
newCoverages={}
for intervention in spreadsheetData.interventionList:
    newCoverages[intervention] = spreadsheetData.interventionCoveragesCurrent[intervention]
# arbitrary allocation of funding
investmentDict = {} # dictionary of money for each intervention
for intervention in spreadsheetData.interventionList:
    investmentDict[intervention] = 1.e6 # 1 million BDT per intervention per year for the full 14 years
# calculate coverage (%)
targetPopSize = {}
for intervention in spreadsheetData.interventionList:
    print intervention
    investment = array([investmentDict[intervention]])
    targetPopSize[intervention] = 0.
    for ageInd in range(numAgeGroups):
        age = ages[ageInd]
        targetPopSize[intervention] += spreadsheetData.interventionTargetPop[intervention][age] * modelZ.listOfAgeCompartments[ageInd].getTotalPopulation()
    targetPopSize[intervention] +=     spreadsheetData.interventionTargetPop[intervention]['pregnant women'] * modelZ.fertileWomen.populationSize
    ccopar = {}
    ccopar['unitcost']   = array([dcp(spreadsheetData.interventionCostCoverage[intervention]["unit cost"])])
    ccopar['saturation'] = array([dcp(spreadsheetData.interventionCostCoverage[intervention]["saturation coverage"])])
    additionalPeopleCovered = costCov.function(investment, ccopar, targetPopSize[intervention]) # function from HIV
    additionalCoverage = additionalPeopleCovered / targetPopSize[intervention]
    print "additional coverage: %g"%(additionalCoverage)
    newCoverages[intervention] += additionalCoverage[0] 
    print "new coverage: %g"%(newCoverages[intervention])
# update coverage
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



