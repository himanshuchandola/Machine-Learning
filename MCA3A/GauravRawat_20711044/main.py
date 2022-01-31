import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("pollution.csv")

print(df.head(3))
df.isna().sum()

#histogram

fig, ax = plt.subplots(figsize=(5,3))

plt.hist(df['NO2μg/l'],bins=5)

plt.title('QUALITY')

plt.xlabel('X')

plt.ylabel('NO2μg/l')

plt.show()



sns.distplot(df['AQI'],kde=False,bins=5)

plt.xlabel('AIR QUALITY')

sns.scatterplot(df['SO2 μg/l'],df['NO2μg/l'], hue=df['year'])

plt.ylabel("AIR QUALITY")

plt.show()


sns.distplot(df['NO2μg/l'],bins=10)

plt.xticks(range(0,200,25))

plt.show()
X = list(df.iloc[:, 0])

Y = list(df.iloc[:, 1])

#	Plot the data using bar() method plt.bar(X, Y, color='g') plt.title("month") plt.xlabel("Years") plt.ylabel("air quality") figsize=(10,10)

#	Show the plot
plt.show()

