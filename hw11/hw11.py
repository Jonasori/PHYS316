"""
Homework 11
Thermal Phys
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

m0 = {'Temp': 1.,
      'mag': 0.99951,
      'var': 0.0000001
      }

m1 = {'Temp': 1.5,
      'mag': 0.98828,
      'var': 0.0000025
      }

m2 = {'Temp': 2.,
      'mag': 0.91931,
      'var': 0.0000484
      }

m3 = {'Temp': 2.1,
      'mag': 0.86450,
      'var': 0.0001131
      }

m4 = {'Temp': 2.2,
      'mag': 0.79395,
      'var': 0.0005007
      }

m5 = {'Temp': 2.22,
      'mag': 0.75305,
      'var': 0.0017801
      }

m6 = {'Temp': 2.24,
      'mag': 0.67908,
      'var': 0.0020295
      }

m7 = {'Temp': 2.25,
      'mag': 0.67102,
      'var': 0.0028165
      }
m8 = {'Temp': 2.26,
      'mag': 0.68311,
      'var': 0.0130422
      }

m9 = {'Temp': 2.28,
      'mag': 0.52307,
      'var': 0.1562516
      }

m10 = {'Temp': 2.29,
       'mag': 0.59497,
       'var': 0.0442572
       }

m11 = {'Temp': 2.3,
       'mag': 0.09729,
       'var': 0.0437948
       }

m12 = {'Temp': 2.31,
       'mag': 0.10388,
       'var': 0.0771536
       }

m13 = {'Temp': 2.32,
       'mag': 0.03796,
       'var': 0.0276515
       }

m14 = {'Temp': 2.32,
       'mag': 0.03796,
       'var': 0.0276515
       }

m15 = {'Temp': 2.33,
       'mag': 0.08459,
       'var': 0.0340594
       }

m16 = {'Temp': 2.34,
       'mag': 0.14587,
       'var': 0.0280273
       }

m17 = {'Temp': 2.35,
       'mag': 0.20837,
       'var': 0.0214568
       }

m18 = {'Temp': 2.4,
       'mag': 0.09888,
       'var': 0.0095013
       }


m19 = {'Temp': 2.5,
       'mag': 0.03174,
       'var': 0.0037607
       }

m20 = {'Temp': 2.6,
       'mag': 0.05505,
       'var': 0.0021601
       }

m21 = {'Temp': 2.7,
       'mag': 0.04077,
       'var': 0.0014564
       }

m22 = {'Temp': 2.8,
       'mag': 0.02454,
       'var': 0.0010768
       }

m23 = {'Temp': 3.0,
       'mag': 0.06543,
       'var': 0.0007420
       }


ms = [m0, m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15,
      m16, m17, m18, m19, m20, m21, m22, m23]
ms_short = [m11, m12, m13, m14, m15, m16, m17, m18, m19, m20]

d = pd.DataFrame(ms)

def m(T):
    m = (1 - (np.sinh(2/T))**(-4.))**(1./8.)
    return m


ts = np.arange(min(d['Temp']), max(d['Temp']), 0.0001)



# Plot m(T)
# Do this through pandas plots?
plt.plot(d['Temp'], d['mag'], 'or')
plt.plot(ts, m(ts))
plt.show(block=False)




# Part B:

"""
Easier to just use Mathematica's FindFit, so export these data out
"""

with open('variances.csv', 'wb') as csvfile:
    data_out = csv.writer(csvfile, delimiter=',')
    for row in ms:
        data_out.writerow([row['Temp'], row['var']])


with open('mags.csv', 'wb') as csvfile:
    data_out = csv.writer(csvfile, delimiter=',')
    for row in ms:
        data_out.writerow([row['Temp'], row['mag']])


with open('vars_short.csv', 'wb') as csvfile:
    data_out = csv.writer(csvfile, delimiter=',')
    for row in ms_short:
        data_out.writerow([row['Temp'], row['var']])












"""

{'converged': array([ True], dtype=bool),
 'deconvolved': {'component0':
                    {'beam':
                        {'beamarcsec':
                            {'major':
                                {'unit': 'arcsec',
                                'value': 0.5997909903526306},
                                'minor': {'unit': 'arcsec',
                                          'value': 0.4910927712917328},
                                'positionangle': {'unit': 'deg',
                                                  'value': 53.43278121948242}},
                            'beampixels': 164.81732912442337,
                            'beamster': 7.844723364690403e-12},
                            'flux': {'error': array([ 0.00433223, 0., 0., 0.]),
                                     'polarisation': 'Stokes',
                                     'unit': 'Jy',
                                     'value': array([ 0.01510276, 0., 0., 0.])},
                            'ispoint': False,
                            'label': '',
                            'peak': {'error': 0.0017023436531734706,
                                     'unit': 'Jy/beam',
                                     'value': 0.007689121354174457},
                            'shape': {'direction':
                                         {'error':
                                            {'latitude':
                                                {'unit': 'arcsec','value': 0.10066511139994555},
                                            'longitude':
                                                {'unit': 'arcsec','value': 0.09292209626485337}},
                                            'm0':
                                                {'unit': 'rad', 'value': 1.4628825898786437},
                                            'm1':
                                                {'unit': 'rad', 'value': -0.09407412464210597},
                                            'refer': 'J2000',
                                            'type': 'direction'},
                                    'majoraxis':
                                        {'unit': 'arcsec', 'value': 0.9921681770253743},
                                    'majoraxiserror':
                                        {'unit': 'arcsec', 'value': 0.3567690111711921},
                                    'minoraxis':
                                        {'unit': 'arcsec', 'value': 0.5831198022427594},
                                    'minoraxiserror':
                                        {'unit': 'arcsec', 'value': 0.2760049117717094},
                                    'positionangle':
                                        {'unit': 'deg', 'value': 38.57583513704645},
                                    'positionangleerror':
                                        {'unit': 'deg', 'value': 89.08968695322082},
                                    'type': 'Gaussian'},
                           'spectrum': {'channel': 0,
                                        'frequency':
                                            {'m0':
                                                {'unit': 'GHz', 'value': 350.01116341206654},
                                            'refer': 'LSRK',
                                            'type': 'frequency'},
                                        'type': 'Constant'},
                           'sum': {'unit': 'Jy/beam', 'value': 1.204984947340563}},
                 'nelements': 1},

'results': {'component0':
           {'beam':
                {'beamarcsec':
                    {'major':
                        {'unit': 'arcsec',
                        'value': 0.5997909903526306},
                        'minor':
                            {'unit': 'arcsec', 'value': 0.4910927712917328},
                            'positionangle':
                                {'unit': 'deg', 'value': 53.43278121948242}},
                            'beampixels': 164.81732912442337,
                            'beamster': 7.844723364690403e-12},
            'flux':
                {'error': array([ 0.00433223, 0., 0., 0.]),
                'polarisation': 'Stokes',
                'unit': 'Jy',
                'value': array([ 0.01510276, 0., 0., 0.])},
            'ispoint': False,
            'label': '',
            'peak':
                {'error': 0.0011107390042698294,
                'unit': 'Jy/beam',
                'value': 0.0050169699759061055},
            'shape':
                {'direction':
                    {'error':
                        {'latitude':
                            {'unit': 'arcsec','value': 0.10066511139994555},
                        'longitude':
                            {'unit': 'arcsec', 'value': 0.09292209626485337}},
                    'm0':
                        {'unit': 'rad', 'value': 1.4628825898786437},
                    'm1':
                        {'unit': 'rad', 'value': -0.09407412464210597},
                    'refer': 'J2000',
                    'type': 'direction'},
                'majoraxis':
                    {'unit': 'arcsec', 'value': 1.1565054896295464},
                'majoraxiserror':
                    {'unit': 'arcsec', 'value': 0.28398751565830105},
                'minoraxis':
                    {'unit': 'arcsec', 'value': 0.7667090646714674},
                'minoraxiserror':
                    {'unit': 'arcsec', 'value': 0.15304533251234606},
                'positionangle':
                    {'unit': 'deg', 'value': 40.82419527541133},
                'positionangleerror':
                    {'unit': 'deg', 'value': 19.131095053759417},
                'type': 'Gaussian'},
            'spectrum': {'channel': 0,
                        'frequency':
                            {'m0':
                                {'unit': 'GHz', 'value': 350.01116341206654},
                                'refer': 'LSRK',
                                'type': 'frequency'},
                            'type': 'Constant'},
            'sum':
                {'unit': 'Jy/beam', 'value': 1.204984947340563}},
            'nelements': 1}
}

"""





# The End
