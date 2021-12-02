import pandas as pd
import numpy as np
from glob import glob
import csv, os, sys

os.chdir("raw")
x_data, y_data = ([] for i in range(2))
for fname in glob('*.data'):
    print(fname)
    x,y = np.genfromtxt(fname, usecols=(0,1),unpack=True)
    x_data.extend(x)
    y_data.extend(y)
tmp = list(zip(x_data, y_data))
d = [x for x in tmp if not x[0] >= 40000]
df = pd.DataFrame(d)
df.to_csv("my_muon.csv")
