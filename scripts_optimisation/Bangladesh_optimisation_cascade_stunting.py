# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 14:04:46 2016

@author: ruth
"""

import os, sys
moduleDir = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(moduleDir)
import optimisation

dataSpreadsheetName = '../input_spreadsheets/Bangladesh/InputForCode_Bangladesh.xlsx'
numModelSteps = 180
MCSampleSize = 25

cascadeValues = [0.25, 0.50, 0.75, 1.0, 1.50, 2.0, 3.0, 4.0]  
#cascadeValues = [0.25, 0.50, 0.75, 1.0]

thisOptimisation = optimisation.Optimisation(dataSpreadsheetName, numModelSteps)

optimise = 'stunting'
filename = 'Bangladesh_cascade_stunting_v4_'
thisOptimisation.performCascadeOptimisation(optimise, MCSampleSize, filename, cascadeValues)