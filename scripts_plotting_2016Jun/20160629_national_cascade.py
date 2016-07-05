# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:09:39 2016

@author: ruth
"""
from numpy import array

cascade_deaths = [{0.25: {u'Balanced energy supplementation': array([  1.53342209e-09]),
   u'Breastfeeding promotion (dual delivery)': array([ 6687803.57875095]),
   u'Complementary feeding (education)': array([  6.48891512e-09]),
   u'Complementary feeding (supplementation)': array([  2.44820964e-08]),
   u'Multiple micronutrient supplementation': array([  2.40880991e-08]),
   u'Vitamin A supplementation': array([  3.53238022e-09]),
   u'Zinc supplementation': array([  1.08623329e-08])}},
 {0.5: {u'Balanced energy supplementation': array([  9.29527639e-09]),
   u'Breastfeeding promotion (dual delivery)': array([ 13375607.15750202]),
   u'Complementary feeding (education)': array([  5.86434103e-09]),
   u'Complementary feeding (supplementation)': array([  1.32232816e-09]),
   u'Multiple micronutrient supplementation': array([  3.11550468e-09]),
   u'Vitamin A supplementation': array([  1.01982858e-09]),
   u'Zinc supplementation': array([  5.48745886e-09])}},
 {0.75: {u'Balanced energy supplementation': array([  9.31968337e-09]),
   u'Breastfeeding promotion (dual delivery)': array([ 20063410.73625298]),
   u'Complementary feeding (education)': array([  6.55465563e-09]),
   u'Complementary feeding (supplementation)': array([  1.71056049e-08]),
   u'Multiple micronutrient supplementation': array([  3.26046815e-08]),
   u'Vitamin A supplementation': array([  1.72283584e-09]),
   u'Zinc supplementation': array([  2.73461405e-08])}},
 {1.0: {u'Balanced energy supplementation': array([  2.12056131e-08]),
   u'Breastfeeding promotion (dual delivery)': array([ 26751214.31500373]),
   u'Complementary feeding (education)': array([  3.11121523e-08]),
   u'Complementary feeding (supplementation)': array([  1.63681249e-08]),
   u'Multiple micronutrient supplementation': array([  2.85497695e-07]),
   u'Vitamin A supplementation': array([  1.44791651e-08]),
   u'Zinc supplementation': array([  5.50574937e-24])}},
 {1.5: {u'Balanced energy supplementation': array([ 3659.50608654]),
   u'Breastfeeding promotion (dual delivery)': array([ 33932763.46389456]),
   u'Complementary feeding (education)': array([  9.58781887e-11]),
   u'Complementary feeding (supplementation)': array([ 0.]),
   u'Multiple micronutrient supplementation': array([ 6183721.07081046]),
   u'Vitamin A supplementation': array([ 0.]),
   u'Zinc supplementation': array([ 6677.43171459])}},
 {2.0: {u'Balanced energy supplementation': array([ 9268.74364629]),
   u'Breastfeeding promotion (dual delivery)': array([ 43197422.23839132]),
   u'Complementary feeding (education)': array([ 20231.51036032]),
   u'Complementary feeding (supplementation)': array([ 0.]),
   u'Multiple micronutrient supplementation': array([ 9713068.23884403]),
   u'Vitamin A supplementation': array([ 562437.89876623]),
   u'Zinc supplementation': array([  2.54322842e-11])}},
 {3.0: {u'Balanced energy supplementation': array([ 10984588.40740118]),
   u'Breastfeeding promotion (dual delivery)': array([ 52247754.01920905]),
   u'Complementary feeding (education)': array([ 0.]),
   u'Complementary feeding (supplementation)': array([ 0.]),
   u'Multiple micronutrient supplementation': array([ 12844842.88867163]),
   u'Vitamin A supplementation': array([ 4176457.62973043]),
   u'Zinc supplementation': array([ 0.])}},
 {4.0: {u'Balanced energy supplementation': array([ 34946224.11112832]),
   u'Breastfeeding promotion (dual delivery)': array([ 54091774.08052409]),
   u'Complementary feeding (education)': array([ 0.]),
   u'Complementary feeding (supplementation)': array([ 0.]),
   u'Multiple micronutrient supplementation': array([ 13385659.48865178]),
   u'Vitamin A supplementation': array([ 4581199.57971219]),
   u'Zinc supplementation': array([  7.44682521e-10])}}]
   
   
cascade_stunting = [{0.25: {u'Balanced energy supplementation': array([  3.39650600e-09]),
   u'Breastfeeding promotion (dual delivery)': array([  2.17762160e-08]),
   u'Complementary feeding (education)': array([ 6687803.57875091]),
   u'Complementary feeding (supplementation)': array([  2.77087637e-08]),
   u'Multiple micronutrient supplementation': array([  2.21241697e-08]),
   u'Vitamin A supplementation': array([  1.68396002e-08]),
   u'Zinc supplementation': array([  2.78128403e-08])}},
 {0.5: {u'Balanced energy supplementation': array([  1.60685688e-07]),
   u'Breastfeeding promotion (dual delivery)': array([  5.00284776e-08]),
   u'Complementary feeding (education)': array([ 13375607.15750157]),
   u'Complementary feeding (supplementation)': array([  1.39451187e-08]),
   u'Multiple micronutrient supplementation': array([  1.37592942e-08]),
   u'Vitamin A supplementation': array([  2.07964821e-07]),
   u'Zinc supplementation': array([  2.47732580e-08])}},
 {0.75: {u'Balanced energy supplementation': array([  2.44386427e-08]),
   u'Breastfeeding promotion (dual delivery)': array([  4.20595516e-09]),
   u'Complementary feeding (education)': array([ 20063410.73625288]),
   u'Complementary feeding (supplementation)': array([  2.76873645e-08]),
   u'Multiple micronutrient supplementation': array([  6.15173057e-08]),
   u'Vitamin A supplementation': array([  4.10053325e-10]),
   u'Zinc supplementation': array([  7.49061016e-08])}},
 {1.0: {u'Balanced energy supplementation': array([ 3701.56515951]),
   u'Breastfeeding promotion (dual delivery)': array([  5.99877716e-12]),
   u'Complementary feeding (education)': array([ 22767390.37905907]),
   u'Complementary feeding (supplementation)': array([ 101751.43289554]),
   u'Multiple micronutrient supplementation': array([ 4764.89290685]),
   u'Vitamin A supplementation': array([ 21756.94266735]),
   u'Zinc supplementation': array([ 3851849.10231578])}},
 {1.5: {u'Balanced energy supplementation': array([ 390.64028988]),
   u'Breastfeeding promotion (dual delivery)': array([ 0.]),
   u'Complementary feeding (education)': array([ 22984863.73983936]),
   u'Complementary feeding (supplementation)': array([ 723.34885366]),
   u'Multiple micronutrient supplementation': array([ 0.]),
   u'Vitamin A supplementation': array([  3.03574079e-10]),
   u'Zinc supplementation': array([ 17140843.74352324])}},
 {2.0: {u'Balanced energy supplementation': array([ 2063.33251414]),
   u'Breastfeeding promotion (dual delivery)': array([ 512.79138925]),
   u'Complementary feeding (education)': array([ 23794447.17035755]),
   u'Complementary feeding (supplementation)': array([ 0.]),
   u'Multiple micronutrient supplementation': array([ 2150.994408]),
   u'Vitamin A supplementation': array([ 986.93220919]),
   u'Zinc supplementation': array([ 29702267.40913007])}},
 {3.0: {u'Balanced energy supplementation': array([ 0.]),
   u'Breastfeeding promotion (dual delivery)': array([ 14102.00776309]),
   u'Complementary feeding (education)': array([ 26448995.94716854]),
   u'Complementary feeding (supplementation)': array([ 0.]),
   u'Multiple micronutrient supplementation': array([  3.88996134e-10]),
   u'Vitamin A supplementation': array([ 15173.28459677]),
   u'Zinc supplementation': array([ 53775371.70548391])}},
 {4.0: {u'Balanced energy supplementation': array([ 26312.12414725]),
   u'Breastfeeding promotion (dual delivery)': array([ 0.]),
   u'Complementary feeding (education)': array([ 29665630.3528865]),
   u'Complementary feeding (supplementation)': array([  1.32000692e-10]),
   u'Multiple micronutrient supplementation': array([ 43737.68011588]),
   u'Vitamin A supplementation': array([ 2453786.56472193]),
   u'Zinc supplementation': array([ 74815390.53814483])}}]
   
   