import matplotlib.pyplot as plt

import pandas as pd
from scipy.stats import norm
import numpy as np


x = np.linspace(1,1000,1000)
index=pd.date_range('01/01/2016', periods=1000,freq="1H")
rs=np.random.RandomState(5)
g = pd.Series( 0,index=index)

for i in rs.choice(x,size=200, replace=False):
    spread=rs.uniform(1,50)
    multiplicator=30*spread
    g+=pd.Series(norm.pdf(x,i,spread)*multiplicator, index=index)

seasonx=x = np.linspace(1,24,24)
season_index=pd.date_range('01/01/2016', periods=24,freq="1H")
season = pd.Series( 0,index=season_index)


for i in rs.choice(x[6:-6],size=3, replace=True):
    spread=rs.uniform(1,5)
    multiplicator=g.mean()
    s=pd.Series(norm.pdf(seasonx,i,spread)*multiplicator, index=season_index)
    season+=s



for i in range (0,len(g)/len(season)):
    g=g.add(s.shift(24*i,freq="1H")*3,fill_value=0)



g.plot()


plt.show()





