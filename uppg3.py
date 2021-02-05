import pandas as pd


area = pd.Series({'Italy': 294140, 'Sweden': 410340, 'Finland': 308890,
             'Germany': 248560, 'Spain': 498800})

pop = pd.Series({'Italy': 60461826,
                   'Sweden': 10099265,
                   'Finland': 5540720,
                   'Germany': 83783942,
                   'Spain': 46754778})

BNP = pd.Series({'Italy': 	1850735,
                   'Sweden': 	511000,
                   'Finland': 	238601,
                   'Germany': 3479232,
                   'Spain': 1232597})

debt = pd.Series({'Italy': 2510690000000,
                   'Sweden': 993939662900,
                   'Finland': 483369000000,
                   'Germany': 5735803200000,
                   'Spain': 2259127000000})




data = pd.DataFrame({'area':area, 'pop':pop, 'BNP':BNP, 'debt':debt})

#Räkna fram density, dvs befolkningstäthet på arean
data['density'] = data['pop']/data['area']

#Räkna fram BNP per capita
data['BNP/capita'] = data['BNP']/data['pop']

#Räkna fram skuld per capita
data['debt/capita'] = data['debt']/data['pop']



print(data)