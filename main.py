import matplotlib.pyplot as plt
import numpy as np 
import pandas 

names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']

x = np.array(range(10))
y = np.array(names)
plt.title("Plotting Sorted Names")

plt.xlabel('SomeNumbers')
plt.ylabel('Names')
plt.show()

print(names)

pf = pandas.dataframe
cols = ['player', 'position', 'team']
df[cols] = df[cols].applymap(lambda x: x.lower())