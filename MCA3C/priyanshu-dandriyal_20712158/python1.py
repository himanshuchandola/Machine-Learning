#importing matplot and seborn for plot 
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

reading pollution data
data = pd.read_csv("pollution.csv")
data.head(10)

plotting Histogram
plt.hist(data['Air Quality'])
plt.xlabel('NH3 in Air')
plt.ylabel('Quality Level')
plt.title("Air Quality with NH3 In Dehradun")
plt.show()

plotting Seaborn
sns.scatterplot(x="NO2μg/l", y="Air Quality", data=data)
plt.title('Air Quality Of Dehradun')
plt.show()

