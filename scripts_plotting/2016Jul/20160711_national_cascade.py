# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 12:01:43 2016

@author: ruth
"""

from numpy import array

cascade_deaths = [{0.25: {u'Balanced energy supplementation': array([ 0.]),
   u'Breastfeeding promotion (dual delivery)': array([ 6687803.57875095]),
   u'Complementary feeding (education)': array([  2.12244849e-09]),
   u'Complementary feeding (supplementation)': array([ 0.]),
   u'Multiple micronutrient supplementation': array([  4.19042156e-08]),
   u'Vitamin A supplementation': array([  3.20378717e-08]),
   u'Zinc supplementation': array([ 0.])}},
 {0.5: {u'Balanced energy supplementation': array([  1.11893890e-09]),
   u'Breastfeeding promotion (dual delivery)': array([ 13375607.15750202]),
   u'Complementary feeding (education)': array([  5.33990785e-09]),
   u'Complementary feeding (supplementation)': array([  7.20419912e-09]),
   u'Multiple micronutrient supplementation': array([  5.24466139e-09]),
   u'Vitamin A supplementation': array([  1.47635411e-09]),
   u'Zinc supplementation': array([  6.32842964e-09])}},
 {0.75: {u'Balanced energy supplementation': array([  4.71483903e-08]),
   u'Breastfeeding promotion (dual delivery)': array([ 20063410.73625299]),
   u'Complementary feeding (education)': array([  1.00423835e-23]),
   u'Complementary feeding (supplementation)': array([  3.14347844e-10]),
   u'Multiple micronutrient supplementation': array([  3.55453148e-08]),
   u'Vitamin A supplementation': array([  6.44190724e-10]),
   u'Zinc supplementation': array([  1.55759449e-09])}},
 {1.0: {u'Balanced energy supplementation': array([  5.19300895e-09]),
   u'Breastfeeding promotion (dual delivery)': array([ 26751214.31500383]),
   u'Complementary feeding (education)': array([  7.73345823e-08]),
   u'Complementary feeding (supplementation)': array([  2.86186727e-08]),
   u'Multiple micronutrient supplementation': array([  3.56676568e-08]),
   u'Vitamin A supplementation': array([  5.24809412e-09]),
   u'Zinc supplementation': array([  1.14189890e-07])}},
 {1.5: {u'Balanced energy supplementation': array([ 7959.3609778]),
   u'Breastfeeding promotion (dual delivery)': array([ 33907854.66388132]),
   u'Complementary feeding (education)': array([ 0.]),
   u'Complementary feeding (supplementation)': array([ 18198.72887221]),
   u'Multiple micronutrient supplementation': array([ 6179129.26261385]),
   u'Vitamin A supplementation': array([  8.67877913e-11]),
   u'Zinc supplementation': array([ 13679.45616097])}},
 {2.0: {u'Balanced energy supplementation': array([ 5170.86670145]),
   u'Breastfeeding promotion (dual delivery)': array([ 43632140.07256103]),
   u'Complementary feeding (education)': array([ 10170.78614586]),
   u'Complementary feeding (supplementation)': array([  7.69190472e-11]),
   u'Multiple micronutrient supplementation': array([ 9846705.77950072]),
   u'Vitamin A supplementation': array([ 8241.12509915]),
   u'Zinc supplementation': array([ 0.])}},
 {3.0: {u'Balanced energy supplementation': array([ 14863916.69543779]),
   u'Breastfeeding promotion (dual delivery)': array([ 52477521.61843766]),
   u'Complementary feeding (education)': array([ 10121.27443957]),
   u'Complementary feeding (supplementation)': array([  4.62192711e-10]),
   u'Multiple micronutrient supplementation': array([ 12902083.35669727]),
   u'Vitamin A supplementation': array([  4.62192711e-10]),
   u'Zinc supplementation': array([  4.62192711e-10])}},
 {4.0: {u'Balanced energy supplementation': array([ 38781115.16609029]),
   u'Breastfeeding promotion (dual delivery)': array([ 54608769.23422522]),
   u'Complementary feeding (education)': array([ 71383.2863803]),
   u'Complementary feeding (supplementation)': array([  1.71841126e-10]),
   u'Multiple micronutrient supplementation': array([ 13543589.57332058]),
   u'Vitamin A supplementation': array([  3.43682253e-10]),
   u'Zinc supplementation': array([ 0.])}}]
   
   
   
cascade_stunting = [{0.25: {u'Balanced energy supplementation': array([  4.22662254e-12]),
   u'Breastfeeding promotion (dual delivery)': array([ 2936.41839546]),
   u'Complementary feeding (education)': array([ 2196928.77972108]),
   u'Complementary feeding (supplementation)': array([ 208.8528197]),
   u'Multiple micronutrient supplementation': array([ 5401.92414154]),
   u'Vitamin A supplementation': array([ 4479123.43662985]),
   u'Zinc supplementation': array([ 3204.1670434])}},
 {0.5: {u'Balanced energy supplementation': array([ 0.]),
   u'Breastfeeding promotion (dual delivery)': array([ 407.0856329]),
   u'Complementary feeding (education)': array([ 8299352.80534197]),
   u'Complementary feeding (supplementation)': array([  3.14725790e-11]),
   u'Multiple micronutrient supplementation': array([ 6359.17247653]),
   u'Vitamin A supplementation': array([ 5069488.09405065]),
   u'Zinc supplementation': array([  1.25890316e-10])}},
 {0.75: {u'Balanced energy supplementation': array([ 1442.42566142]),
   u'Breastfeeding promotion (dual delivery)': array([ 43.18555004]),
   u'Complementary feeding (education)': array([ 13951390.73011632]),
   u'Complementary feeding (supplementation)': array([ 0.]),
   u'Multiple micronutrient supplementation': array([  4.85432688e-11]),
   u'Vitamin A supplementation': array([ 6110534.3949253]),
   u'Zinc supplementation': array([  5.82519225e-11])}},
 {1.0: {u'Balanced energy supplementation': array([  1.10049271e-10]),
   u'Breastfeeding promotion (dual delivery)': array([ 4205.24106584]),
   u'Complementary feeding (education)': array([ 19399647.04420812]),
   u'Complementary feeding (supplementation)': array([ 0.]),
   u'Multiple micronutrient supplementation': array([ 3750.87948469]),
   u'Vitamin A supplementation': array([ 7343611.15024544]),
   u'Zinc supplementation': array([ 0.])}},
 {1.5: {u'Balanced energy supplementation': array([ 14135.66287047]),
   u'Breastfeeding promotion (dual delivery)': array([ 0.]),
   u'Complementary feeding (education)': array([ 20806069.39117776]),
   u'Complementary feeding (supplementation)': array([ 0.]),
   u'Multiple micronutrient supplementation': array([ 0.]),
   u'Vitamin A supplementation': array([ 7644562.54836294]),
   u'Zinc supplementation': array([ 11662053.87009498])}},
 {2.0: {u'Balanced energy supplementation': array([  1.10276989e-10]),
   u'Breastfeeding promotion (dual delivery)': array([ 7692.29136772]),
   u'Complementary feeding (education)': array([ 21445317.23604035]),
   u'Complementary feeding (supplementation)': array([  4.41107955e-10]),
   u'Multiple micronutrient supplementation': array([  1.10276989e-10]),
   u'Vitamin A supplementation': array([ 7769008.32574077]),
   u'Zinc supplementation': array([ 24280410.77685937])}},
 {3.0: {u'Balanced energy supplementation': array([ 13664.92829113]),
   u'Breastfeeding promotion (dual delivery)': array([  2.13296603e-09]),
   u'Complementary feeding (education)': array([ 23841977.07083534]),
   u'Complementary feeding (supplementation)': array([ 18416.55701801]),
   u'Multiple micronutrient supplementation': array([ 3533.24018881]),
   u'Vitamin A supplementation': array([ 8290649.09781987]),
   u'Zinc supplementation': array([ 48085402.05085915])}},
 {4.0: {u'Balanced energy supplementation': array([ 0.]),
   u'Breastfeeding promotion (dual delivery)': array([ 26841.29127564]),
   u'Complementary feeding (education)': array([ 27179366.7946822]),
   u'Complementary feeding (supplementation)': array([ 21054.87793145]),
   u'Multiple micronutrient supplementation': array([ 0.]),
   u'Vitamin A supplementation': array([ 9112994.64851627]),
   u'Zinc supplementation': array([ 70664599.64761083])}}]
   