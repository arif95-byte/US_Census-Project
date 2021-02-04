import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

census_file = glob.glob("states*.csv")

file_list = []
for filename in census_file:
  data = pd.read_csv(filename)
  file_list.append(data)
us_census = pd.concat(file_list)
print(us_census.head())
print(us_census.columns)
print(us_census.dtypes)

us_census.Income = us_census.Income.replace("[\$]", " ", regex=True)
print(us_census.Income.head())

population_split = us_census.GenderPop.str.split("_")
print(population_split.head())

us_census["male_population"] = population_split.str.get(0)
us_census["female_population"] = population_split.str.get(1)
print(us_census.head())

pop_split = pd.DataFrame()
pop_split["male_pop"] = us_census.male_population.str[0:-1]
pop_split["female_pop"] = us_census.female_population.str[0:-1]
print(pop_split.head())
us_census = pd.concat([us_census, pop_split], axis=1)
print(us_census.head())

us_census = us_census[["State", "TotalPop", "Hispanic", "White", "Black", "Native", "Asian", "Pacific", "Income", "male_pop", "female_pop"]]
us_census.columns = ["State", "TotalPop", "Hispanic", "White", "Black", "Native", "Asian", "Pacific", "Income", "male_population", "female_population"]
us_census.male_population = pd.to_numeric(us_census.male_population)
us_census.female_population = pd.to_numeric(us_census.female_population)
print(us_census.dtypes)

plt.scatter(us_census.female_population, us_census.Income) 
plt.show()
print(us_census.female_population.head(15))
fem_pop_nan = us_census.female_population.isnull()
print(fem_pop_nan.head(15))
print(fem_pop_nan.value_counts())

example_nan = us_census[["TotalPop", "male_population", "female_population"]]
nan_value = us_census.TotalPop - us_census.male_population
us_census.female_population = us_census.female_population.fillna(value=nan_value)
example_nan = us_census[['TotalPop', 'male_population', 'female_population']]
example_nan.iloc[12]

nan_value = us_census.TotalPop - us_census.male_population

duplicates = us_census.duplicated()
print(duplicates.value_counts())
us_census = us_census.drop_duplicates()
duplicates_check = us_census.duplicated()
duplicates_check.value_counts()

plt.scatter(us_census.female_population, us_census.Income) 
plt.show()

us_census.Hispanic = us_census.Hispanic.replace('[\%]', '', regex=True)
us_census.White = us_census.White.replace('[\%]', '', regex=True)
us_census.Black = us_census.Black.replace('[\%]', '', regex=True)
us_census.Native = us_census.Native.replace('[\%]', '', regex=True)
us_census.Asian = us_census.Asian.replace('[\%]', '', regex=True)
us_census.Pacific = us_census.Pacific.replace('[\%]', '', regex=True)
print(us_census.head())

us_census.Hispanic = pd.to_numeric(us_census.Hispanic)
us_census.White = pd.to_numeric(us_census.White)
us_census.Black = pd.to_numeric(us_census.Black)
us_census.Native = pd.to_numeric(us_census.Native)
us_census.Asian = pd.to_numeric(us_census.Asian)
us_census.Pacific = pd.to_numeric(us_census.Pacific)
print(us_census.dtypes)

Hnan = us_census.Hispanic.isnull()
Wnan = us_census.White.isnull()
Bnan = us_census.Black.isnull()
Nnan = us_census.Native.isnull()
Anan = us_census.Asian.isnull()
Pnan = us_census.Pacific.isnull()

nan_value = us_census.Pacific.mean()
us_census.Pacific = us_census.Pacific.fillna(value=nan_value)
print(us_census.Pacific)
print(us_census.head())

plt.hist(us_census.Hispanic)
plt.xlabel('Percentage')
plt.ylabel('Frequency of occurance')
plt.show()


plt.hist(us_census.White)
plt.xlabel('Percentage')
plt.ylabel('Frequency of occurance')
plt.show()