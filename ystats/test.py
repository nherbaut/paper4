import pandas as pd
import numpy as np
def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births/births.sum()
    return group

pieces = []
columns = ['name', 'sex', 'births']

for year in range(1880, 2012):
    path = 'test3.csv' % year
    frame = pd.read_csv(path, names = columns)
    frame['year'] = year
    pieces.append(frame)
    names = pd.concat(pieces, ignore_index = True)

total_births = names.pivot_table('births', rows = 'year', cols = 'sex', aggfunc = sum)
total_births.plot(title = 'Total Births by sex and year')
