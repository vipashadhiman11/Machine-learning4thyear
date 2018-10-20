from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from statistics import mean


file='Gait_data.xlsx'
x1=pd.ExcelFile(file)



df1=pd.read_excel(x1,'Combined')


df1 = df1.rename(columns={'stride length (m)': 'stride_len', 'cadence (step/min)': 'Cadence'})
df1 = df1.rename(columns={'leg len (m)': 'leg_len', 'age (year)': 'age'})

style.use('ggplot')



print(mean(df1.stride_len))

print(mean(df1.Cadence))

print(mean(df1.leg_len))

print(mean(df1.age))

from statistics import median,mode

print(median(df1.stride_len))


print(median(df1.Cadence))


print(median(df1.leg_len))

print(median(df1.age))


#print(mode(df1.stride_len))

#print(mode(df1.Cadence))

#print(mode(df1.leg_len))

#print(mode(df1.age))

from statistics import stdev


print(stdev(df1.stride_len))

print(stdev(df1.Cadence))

print(stdev(df1.leg_len))

print(stdev(df1.age))


from statistics import variance

print(variance(df1.stride_len))

print(variance(df1.Cadence))

print(variance(df1.leg_len))

print(variance(df1.age))


plt.scatter(df1.Cadence,df1.age)
print(np.corrcoef(df1.Cadence,df1.age))
plt.title('Cadence vs age')
plt.ylabel('Cadence')
plt.xlabel('age')
plt.show()

plt.scatter(df1.stride_len,df1.age)
print(np.corrcoef(df1.stride_len,df1.age))
plt.title('stride_length vs age')
plt.ylabel('stride_length')
plt.xlabel('age')
plt.show()

plt.scatter(df1.leg_len,df1.age)
print(np.corrcoef(df1.leg_len,df1.age))
plt.title('leg_length vs age')
plt.ylabel('leg_length')
plt.xlabel('age')
plt.show()

plt.scatter(df1.Cadence,df1.stride_len)
print(np.corrcoef(df1.Cadence,df1.stride_len))
plt.title('Cadence vs stride_length')
plt.ylabel('Cadence')
plt.xlabel('stride_length')
plt.show()

plt.scatter(df1.Cadence,df1.leg_len)
print(np.corrcoef(df1.Cadence,df1.leg_len))
plt.title('Cadence vs leg_length')
plt.ylabel('Cadence')
plt.xlabel('leg_length')
plt.show()

plt.scatter(df1.leg_len,df1.stride_len)
print(np.corrcoef(df1.leg_len,df1.stride_len))
plt.title('leg_length vs stride_length')
plt.ylabel('leg_length')
plt.xlabel('stride_length')
plt.show()