
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\indur\OneDrive\Desktop\depolyment projects\zomato_project\govinda\clean.csv')
print(df.to_string())

#exploratoty data analysis
#basics step 1

print(df.describe())
print(df.shape)
print(df.info())
print(df.columns)
print(df.head())
print(df.tail())
print('-------------------------------------------------------------------')

#deuplicates step 2

duplicates = df.duplicated().sum()
drop_duplicates = df.drop_duplicates()

print('----------------------------------------------------------------------')

#messing values step 3

missing_value = df.isna().sum()
missing_null = df.isnull()

print('-------------------------------------------------------------------------')

#understand categorical daat set step 4

citys = df['city'].value_counts()
print(citys)

plt.figure(figsize=(5,6))
plt.bar(citys.index,citys.values)
plt.title('Each total city')
plt.xlabel('citys')
plt.ylabel('values')
plt.tight_layout()
plt.show()

print('-------------------------------------------------------------------------')

#groupby 

group_data = df.groupby('city')['total_orders'].sum()
print(group_data)

plt.figure(figsize=(5,6))
group_data.plot(kind='bar')
plt.title('group data with city and total_orders')
plt.xlabel('citys')
plt.ylabel('total_orders')
plt.tight_layout()
plt.show()


print('-----------------------------------------------------------')

#correlation

corr = df.corr(numeric_only=True)
print(corr)

plt.figure(figsize=(5,6))
sns.heatmap(corr)
plt.title('corrleation')
plt.tight_layout()
plt.show()

#outliers

plt.figure(figsize=(5,6))
sns.boxplot(data=df[['total_revenue','total_orders','days_since_last_order']])
plt.title('outliers data')
plt.xlabel('total_revenue')
plt.ylabel('values')
plt.tight_layout()
plt.show()

#destribution

plt.figure(figsize=(5,4))
sns.histplot(data=df,x = 'days_since_last_order')
plt.title('distribustion of data ')
plt.xticks(rotation = 42)
plt.tight_layout()
plt.show()

#crosstab

realtion = pd.crosstab(df['city'],df['churn'])
percaentage = pd.crosstab(df['city'],df['churn'],normalize='index')  * 100
print(percaentage)

#relationship scatterplot
plt.figure(figsize=(4,7))
sns.scatterplot(data=df,x = 'total_orders',y = 'total_revenue')
plt.title('relationship')
plt.xlabel('total_orders')
plt.ylabel('total_revenue')
plt.tight_layout()
plt.show()

# EDA insights  summary:

# 1. customers with higher days_since_last_order are more likely to churn
# 2. customers with fewer total_orders show higher churn behavior.
# 3.high total_revenue customers tend to reamin active.
#4. churn distibustion is imbalanced,indicating the nedd for smote.
#5. city-wise analysis show variation in vchurn across regions.

