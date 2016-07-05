# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 13:22:48 2016

@author: ruth
"""

numberOfDeaths_baseline = {'region 0': 84967.959963224261,
 'region 1': 432500.2928533018,
 'region 2': 581900.92304565408,
 'region 3': 251923.21805830728,
 'region 4': 230689.47857887507,
 'region 5': 179523.82705260918,
 'region 6': 208735.92365968353}

numberAgingOutStunted_baseline = {'region 0': 1441125.9229754584,
 'region 1': 5160482.1781260716,
 'region 2': 7222870.012320918,
 'region 3': 1874370.9590635994,
 'region 4': 2615774.3595650303,
 'region 5': 2534200.0804932341,
 'region 6': 2455233.9196933494}
 
 
numberOfDeaths_optimisingDeaths = {'region 0': {0.25: 88749.686610927267,
  0.5: 86839.807052956006,
  0.75: 85470.388691085711,
  1.0: 84562.323985018462,
  1.5: 83349.319968361437,
  2.0: 82604.92657305146,
  3.0: 81672.630860179925,
  4.0: 81131.60148621157},
 'region 1': {0.25: 450308.50025882351,
  0.5: 441474.14725744637,
  0.75: 435485.74083499605,
  1.0: 431058.31017493602,
  1.5: 425230.08313678636,
  2.0: 420784.57849004731,
  3.0: 415934.34364457498,
  4.0: 412889.26353478915},
 'region 2': {0.25: 607961.46999298059,
  0.5: 592555.98043137393,
  0.75: 582321.7433747719,
  1.0: 576069.515366368,
  1.5: 567945.86417975207,
  2.0: 563539.18918593659,
  3.0: 558314.11957239872,
  4.0: 555909.15843683935},
 'region 3': {0.25: 263602.68030619627,
  0.5: 256335.83543130226,
  0.75: 251564.28475992792,
  1.0: 248616.83829141001,
  1.5: 245033.8720315932,
  2.0: 243241.36540963413,
  3.0: 241241.44190552237,
  4.0: 240141.92783795457},
 'region 4': {0.25: 241616.42703422866,
  0.5: 235017.67227832205,
  0.75: 230561.88446501704,
  1.0: 227901.56548874849,
  1.5: 224462.14152935654,
  2.0: 222773.14401568196,
  3.0: 220841.96917988799,
  4.0: 219988.02836223092},
 'region 5': {0.25: 187278.11725078805,
  0.5: 182015.25485768879,
  0.75: 178765.20047667043,
  1.0: 176765.83575966011,
  1.5: 174405.1106252578,
  2.0: 173311.06231646254,
  3.0: 172020.01032902871,
  4.0: 171125.2830651018},
 'region 6': {0.25: 218018.95007756015,
  0.5: 213190.52450872664,
  0.75: 209733.71110236665,
  1.0: 207521.4471357268,
  1.5: 204579.26917523766,
  2.0: 202791.05888367191,
  3.0: 200480.17191835531,
  4.0: 199454.13351034524}}

numberOfDeaths_optimisingStunting = {'region 0': {0.25: 90668.493213702808,
  0.5: 90375.146818544192,
  0.75: 90174.938487074978,
  1.0: 90052.401104449527,
  1.5: 89775.01790427207,
  2.0: 89510.875559886292,
  3.0: 89091.359211822622,
  4.0: 88583.436252378131},
 'region 1': {0.25: 458525.31125022168,
  0.5: 456258.78320195351,
  0.75: 454807.51253032166,
  1.0: 453980.80252359033,
  1.5: 452336.88275230612,
  2.0: 450835.48983031639,
  3.0: 448347.76794687368,
  4.0: 445248.20841680374},
 'region 2': {0.25: 625165.64291877451,
  0.5: 623440.49902834883,
  0.75: 622353.56755055755,
  1.0: 621718.11865578662,
  1.5: 620495.04529832536,
  2.0: 619428.67773391842,
  3.0: 617203.25194155739,
  4.0: 615130.98484739056},
 'region 3': {0.25: 271997.47912651679,
  0.5: 271417.26317551913,
  0.75: 271056.73230011086,
  1.0: 270808.77769498347,
  1.5: 270233.82618362131,
  2.0: 269732.67668484681,
  3.0: 268914.27775800275,
  4.0: 268462.05984163261},
 'region 4': {0.25: 249129.94413564799,
  0.5: 248590.13813458377,
  0.75: 248244.33670339291,
  1.0: 248047.72166632282,
  1.5: 247659.92201709308,
  2.0: 247316.37942952901,
  3.0: 246770.29337325407,
  4.0: 246371.71025111375},
 'region 5': {0.25: 193691.30826570623,
  0.5: 193284.56535903332,
  0.75: 193046.78797908555,
  1.0: 192855.68322781971,
  1.5: 192479.36041862017,
  2.0: 192160.4935491959,
  3.0: 191679.34555828042,
  4.0: 191342.71016457243},
 'region 6': {0.25: 222960.04976616416,
  0.5: 222222.56454453332,
  0.75: 221720.61854135292,
  1.0: 221414.18430666541,
  1.5: 220998.80154553917,
  2.0: 220603.60930885546,
  3.0: 219941.65324959677,
  4.0: 219469.92494742057}}

numberAgingOutStunted_optimisingDeaths = {'region 0': {0.25: 1456738.6427372512,
  0.5: 1457316.5966850587,
  0.75: 1457730.8932985105,
  1.0: 1456687.1766045827,
  1.5: 1455100.7391965881,
  2.0: 1427361.82896909,
  3.0: 1390675.3086795411,
  4.0: 1366594.982506651},
 'region 1': {0.25: 5251198.3100624904,
  0.5: 5254322.198354857,
  0.75: 5256439.3403696232,
  1.0: 5252264.5575018292,
  1.5: 5136394.7821625583,
  2.0: 5033734.5151307797,
  3.0: 4934603.2270907341,
  4.0: 4848406.154612611},
 'region 2': {0.25: 7398080.6825223174,
  0.5: 7402712.296470657,
  0.75: 7405788.4512053914,
  1.0: 7404941.6307082912,
  1.5: 7392554.8335554935,
  2.0: 7182238.719387264,
  3.0: 6951241.2416612525,
  4.0: 6804120.098384968},
 'region 3': {0.25: 1925363.4457698236,
  0.5: 1927252.4330668941,
  0.75: 1928492.5116366982,
  1.0: 1928376.5658239424,
  1.5: 1926193.6018476433,
  2.0: 1885209.518497458,
  3.0: 1804577.2677665458,
  4.0: 1756365.9894498726},
 'region 4': {0.25: 2682423.4993322999,
  0.5: 2684332.498845811,
  0.75: 2685621.2731860941,
  1.0: 2686390.6289964877,
  1.5: 2682983.4635694083,
  2.0: 2639985.0934551414,
  3.0: 2519429.6616010652,
  4.0: 2472937.7592320526},
 'region 5': {0.25: 2594145.8784461832,
  0.5: 2595957.9072525981,
  0.75: 2597076.8160217553,
  1.0: 2596380.5814380385,
  1.5: 2594911.012374741,
  2.0: 2540835.3542189323,
  3.0: 2483769.2830688721,
  4.0: 2474667.8103021001},
 'region 6': {0.25: 2468018.6746225241,
  0.5: 2470510.1443567364,
  0.75: 2472293.7203540206,
  1.0: 2473435.0973199522,
  1.5: 2473207.6491932673,
  2.0: 2443172.2388536129,
  3.0: 2404156.4752066801,
  4.0: 2386474.8000494456}}

numberAgingOutStunted_optimisingStunting = {'region 0': {0.25: 1429044.3971680438,
  0.5: 1407140.0772892111,
  0.75: 1392003.3379534867,
  1.0: 1382664.5309095404,
  1.5: 1369462.9261218649,
  2.0: 1357053.6882525908,
  3.0: 1336052.8727736182,
  4.0: 1320895.7334532398},
 'region 1': {0.25: 5130384.785488205,
  0.5: 5032641.3283734256,
  0.75: 4969169.0528852139,
  1.0: 4932708.2730050422,
  1.5: 4883172.8145689191,
  2.0: 4836924.5662012836,
  3.0: 4761406.7200638456,
  4.0: 4708983.4323466588},
 'region 2': {0.25: 7203748.3715060269,
  0.5: 7051940.2518051956,
  0.75: 6955585.9338399004,
  1.0: 6901266.7606861945,
  1.5: 6815745.9101368813,
  2.0: 6736734.9233593205,
  3.0: 6610062.627689315,
  4.0: 6524304.7794827409},
 'region 3': {0.25: 1866386.5953544804,
  0.5: 1823318.4113602336,
  0.75: 1796354.2459918302,
  1.0: 1780948.8697556749,
  1.5: 1754835.6420839531,
  2.0: 1730947.2207436066,
  3.0: 1693263.3022893218,
  4.0: 1668763.2945833222},
 'region 4': {0.25: 2605139.53291651,
  0.5: 2545537.9998405045,
  0.75: 2507090.3365559862,
  1.0: 2485143.0188236637,
  1.5: 2453070.6280604727,
  2.0: 2423259.0633257739,
  3.0: 2374928.7899638377,
  4.0: 2342513.3446083893},
 'region 5': {0.25: 2538149.8636712614,
  0.5: 2493867.7439724505,
  0.75: 2467781.3004802437,
  1.0: 2451165.6973162112,
  1.5: 2419629.1159407045,
  2.0: 2391531.7199383406,
  3.0: 2349232.0973845469,
  4.0: 2323582.1285568033},
 'region 6': {0.25: 2437743.1490316326,
  0.5: 2413844.7943755318,
  0.75: 2397309.0016565761,
  1.0: 2387107.909395841,
  1.5: 2375534.2479569674,
  2.0: 2365006.8291031537,
  3.0: 2347030.3740897188,
  4.0: 2333859.3784488509}}