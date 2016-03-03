# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:57:07 2016

@author: ruth
"""

class Data:
    def __init__(self, ages, causesOfDeath, totalMortalityByAge, causeOfDeathByAge, RRStunting, RRWasting, RRBreastFeeding, stuntingDistribution, wastingDistribution, breastfeedingDistribution, birthCircumstanceDist, timeBetweenBirthsDist, RRbirthOutcomeByAgeAndOrder, RRbirthOutcomeByTime, ORstuntingProgression):
        self.ages = ages
        self.causesOfDeath = causesOfDeath
        self.totalMortalityByAge = totalMortalityByAge
        self.causeOfDeathByAge = causeOfDeathByAge
        self.RRStunting = RRStunting
        self.RRWasting = RRWasting
        self.RRBreastFeeding = RRBreastFeeding
        self.stuntingDistribution = stuntingDistribution
        self.wastingDistribution = wastingDistribution
        self.breastfeedingDistribution = breastfeedingDistribution
        self.birthCircumstanceDist = birthCircumstanceDist
        self.timeBetweenBirthsDist = timeBetweenBirthsDist
        self.RRbirthOutcomeByAgeAndOrder = RRbirthOutcomeByAgeAndOrder
        self.RRbirthOutcomeByTime = RRbirthOutcomeByTime
        self.ORstuntingProgression = ORstuntingProgression
    
    
def getFakeData():
        
    ages = ["0-1 month", "1-6 months", "6-12 months", "12-24 months", "24-59 months"]
    causesOfDeath = ["diarrhea", "malaria"]
    #THIS IS LEFT HAND SIDE OF EQUATION
    totalMortalityByAge = [22, 35, 35, 35, 49]
    
    #causes of death are percent (0 to 1)
    causeOfDeathByAge = {"diarrhea":{"0-1 month":0.4, "1-6 months":0.1, "6-12 months":0.1, "12-24 months":0.1, "24-59 months":0.1}, "malaria":{"0-1 month":0.2, "1-6 months":0.2, "6-12 months":0.2, "12-24 months":0.2, "24-59 months":0.2}}
    
    #Relative Risks for stunting, wasting, breast feeding
    RRStuntingMalaria = {"normal":{"0-1 month":0.1, "1-6 months":0.1, "6-12 months":0.1, "12-24 months":0.1, "24-59 months":0.1},
                         "mild":{"0-1 month":0.1, "1-6 months":0.1, "6-12 months":0.1, "12-24 months":0.1, "24-59 months":0.1},
                         "moderate":{"0-1 month":0.1, "1-6 months":0.1, "6-12 months":0.1, "12-24 months":0.1, "24-59 months":0.1},
                         "high":{"0-1 month":0.1, "1-6 months":0.1, "6-12 months":0.1, "12-24 months":0.1, "24-59 months":0.1} }
    
    RRBreastFeedingMalaria = {"exclusive":{"0-1 month":0.1, "1-6 months":0.1, "6-12 months":0.1, "12-24 months":0.1, "24-59 months":0.1},
                                 "predominant":{"0-1 month":0.1, "1-6 months":0.1, "6-12 months":0.1, "12-24 months":0.1, "24-59 months":0.1},
                                 "partial":{"0-1 month":0.1, "1-6 months":0.1, "6-12 months":0.1, "12-24 months":0.1, "24-59 months":0.1},
                                 "none":{"0-1 month":0.1, "1-6 months":0.1, "6-12 months":0.1, "12-24 months":0.1, "24-59 months":0.1} }    
    
    #make a dictionary of RR for each disease
    #diarrhea would be same form as malaria, just re-use for now
    RRStunting = {"diarrhea":RRStuntingMalaria, "malaria":RRStuntingMalaria}
    RRWasting = {"diarrhea":RRStuntingMalaria, "malaria":RRStuntingMalaria} #this is just the same as stunting for now    
    RRBreastFeeding = {"diarrhea":RRBreastFeedingMalaria, "malaria":RRBreastFeedingMalaria} #this is just the same as stunting for now
    
    #stunting, wasting, breast feeding distributions (similar form to one disease table of RR, so just re-use for now)
    stuntingDistribution = RRStuntingMalaria
    wastingDistribution = RRStuntingMalaria
    breastfeedingDistribution = RRBreastFeedingMalaria
    
    # birth circumstance distributions
    birthCircumstanceDist = {"<18 years":{"first":0.0543,"second or third":0.009,"greater than third":0.00},
                             "18-34 years":{"first":0.1711,"second or third":0.3607,"greater than third":0.2908},
                             "35-49 years":{"first":0.0003,"second or third":0.0085,"greater than third":0.1048}}

    # distribution of time between births
    timeBetweenBirthsDist = {"first":0.2258,"<18 months":0.0705,"18-23 months":0.134,"<24 months":0.5698}


    # Relative Risks of (first 3) Birth Outcomes by maternal age & birth order, and time
    RRbirthOutcomeByAgeAndOrder = {"pretermSGA":{"<18 years":{"first":3.14,"second or third":1.6,"greater than third":1.6},
                                                 "18-34 years":{"first":1.73,"second or third":1.,"greater than third":1.},
                                                 "35-49 years":{"first":1.73,"second or third":1.57,"greater than third":1.57}},
                                   "pretermAGA":{"<18 years":{"first":1.75,"second or third":1.4,"greater than third":1.4},
                                                 "18-34 years":{"first":1.75,"second or third":1.,"greater than third":1.},
                                                 "35-49 years":{"first":1.75,"second or third":1.33,"greater than third":1.33}},
                                   "termSGA":{"<18 years":{"first":1.52,"second or third":1.2,"greater than third":1.2},
                                              "18-34 years":{"first":1.52,"second or third":1.,"greater than third":1.},
                                              "35-49 years":{"first":1.52,"second or third":1.,"greater than third":1.}}}


    RRbirthOutcomeByTime = {"pretermSGA":{"first":1.,"<18 months":3.03,"18-23 months":1.77,"<24 months":1.},
                            "pretermAGA":{"first":1.,"<18 months":1.49,"18-23 months":1.1,"<24 months":1.},
                            "termSGA":{"first":1.,"<18 months":1.41,"18-23 months":1.18,"<24 months":1.}}


    # Odds Ratios on Stunting by: BirthOutcomes, Previous Stunting Category, ...
    ORstuntingProgression = {ages[1]:12.4, ages[2]:21.4, ages[3]:30.3, ages[4]:46.2}

    fakeData = Data(ages, causesOfDeath, totalMortalityByAge, causeOfDeathByAge, RRStunting, RRWasting, RRBreastFeeding, stuntingDistribution, wastingDistribution, breastfeedingDistribution, birthCircumstanceDist, timeBetweenBirthsDist, RRbirthOutcomeByAgeAndOrder, RRbirthOutcomeByTime, ORstuntingProgression)

    return fakeData
    
    
    
def getDataFromSpreadsheet(fileName):
    
    import pandas
    Location = fileName
    
    #  READ TOTAL MORTALITY SHEET
    #  gets you:
    #  - totalMortalityByAge
    
    df = pandas.read_excel(Location, sheetname = 'total mortality')
    totalMortalityByAge = list(df.iloc[0])
    
    #  READ MORTALITY SHEET
    #  gets you:
    #  - ages
    #  - causesOfDeath
    #  - casueOfDeathByAge
    
    #get list of ages and causesOfDeath
    df = pandas.read_excel(Location, sheetname = 'mortality') #read this way for this task
    causesOfDeath = list(df['Cause'])
    ages = list(df.columns.values)[1:]
    #get the nested list of causeOfDeathByAge
    df = pandas.read_excel(Location, sheetname = 'mortality', index_col = 'Cause') #read this way for this task
    causeOfDeathByAge = {}
    for cause in causesOfDeath:
        causeOfDeathByAge[cause] = {}
        for age in ages:
            causeOfDeathByAge[cause][age] = df.loc[cause, age]
            
    #  READ RRStunting SHEET
    #  gets you:
    #  - RRStunting
    
    #get the list of causes for which we have relative risks
    df = pandas.read_excel(Location, sheetname = 'RRStunting', index_col = [0]) #read this way for this task
    mylist = list(df.index.values)
    myset = set(mylist)
    listCausesRRStunting = list(myset)
    #put the RR into RRStunting
    df = pandas.read_excel(Location, sheetname = 'RRStunting', index_col = [0, 1]) #read this way for this task
    
    RRStunting = {}
    for cause in causesOfDeath:
        RRStunting[cause] = {}
        for stuntingStatus in ['normal', 'mild', 'moderate', 'high']:
            RRStunting[cause][stuntingStatus] = {}
            for age in ages:
                if cause in listCausesRRStunting: #if no RR given for this cause then set to 1
                    RRStunting[cause][stuntingStatus][age] = df.loc[cause][age][stuntingStatus]
                else:
                    RRStunting[cause][stuntingStatus][age] = 1
                   
            
    #  READ RRWasting SHEET
    #  gets you:
    #  - RRWasting
    
    #get the list of causes for which we have relative risks
    df = pandas.read_excel(Location, sheetname = 'RRWasting', index_col = [0]) #read this way for this task
    mylist = list(df.index.values)
    myset = set(mylist)
    listCausesRRWasting = list(myset)
    #put the RR into RRWasting
    df = pandas.read_excel(Location, sheetname = 'RRWasting', index_col = [0, 1]) #read this way for this task
    
    RRWasting = {}
    for cause in causesOfDeath:
        RRWasting[cause] = {}
        for wastingStatus in ['normal', 'mild', 'moderate', 'high']:
            RRWasting[cause][wastingStatus] = {}
            for age in ages:
                if cause in listCausesRRWasting: #if no RR given for this cause then set to 1
                    RRWasting[cause][wastingStatus][age] = df.loc[cause][age][wastingStatus]
                else:
                    RRWasting[cause][wastingStatus][age] = 1        

    #  READ RRBreastFeeding SHEET
    #  gets you:
    #  - RRBreastFeeding
    
    #get the list of causes for which we have relative risks
    df = pandas.read_excel(Location, sheetname = 'RRBreastFeeding', index_col = [0]) #read this way for this task
    mylist = list(df.index.values)
    myset = set(mylist)
    listCausesRRBreastFeeding = list(myset)
    #put the RR into RRBreastFeeding
    df = pandas.read_excel(Location, sheetname = 'RRBreastFeeding', index_col = [0, 1]) #read this way for this task
    
    RRBreastFeeding = {}
    for cause in causesOfDeath:
        RRBreastFeeding[cause] = {}
        for breastFeedingStatus in ['exclusive', 'predominant', 'partial', 'none']:
            RRBreastFeeding[cause][breastFeedingStatus] = {}
            for age in ages:
                if cause in listCausesRRBreastFeeding: #if no RR given for this cause then set to 1
                    RRBreastFeeding[cause][breastFeedingStatus][age] = df.loc[cause][age][breastFeedingStatus]
                else:
                    RRBreastFeeding[cause][breastFeedingStatus][age] = 1  
        
    #  READ distributions SHEET
    #  gets you:
    #  - stuntingDistribution
    #  - wastingDistribution
    #  - breastfeedingDistribution
    
    df = pandas.read_excel(Location, sheetname = 'distributions', index_col = [0, 1]) #read this way for this task
    stuntingDistribution = {}
    wastingDistribution = {}
    breastfeedingDistribution = {}
    
    #stunting
    for status in ['normal', 'mild', 'moderate', 'high']:
        stuntingDistribution[status] = {}
        for age in ages:
            stuntingDistribution[status][age] = df.loc['Stunting'][age][status]
    #wasting        
    for status in ['normal', 'mild', 'moderate', 'high']:
        wastingDistribution[status] = {}
        for age in ages:
            wastingDistribution[status][age] = df.loc['Wasting'][age][status]        
    #breast feeding       
    for status in ['exclusive', 'predominant', 'partial', 'none']:
        breastfeedingDistribution[status] = {}
        for age in ages:
            breastfeedingDistribution[status][age] = df.loc['Breast Feeding'][age][status]
            
    #set these to zero for now, need to add them to spreadsheet
    birthCircumstanceDist = 0
    timeBetweenBirthsDist = 0   
    RRbirthOutcomeByAgeAndOrder = 0
    RRbirthOutcomeByTime = 0
            
    spreadsheetData = Data(ages, causesOfDeath, totalMortalityByAge, causeOfDeathByAge, RRStunting, RRWasting, RRBreastFeeding, stuntingDistribution, wastingDistribution, breastfeedingDistribution, birthCircumstanceDist, timeBetweenBirthsDist, RRbirthOutcomeByAgeAndOrder, RRbirthOutcomeByTime)
    return spreadsheetData        
                  