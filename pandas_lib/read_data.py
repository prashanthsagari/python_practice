import pandas as pd

sal = pd.read_csv('Salaries.csv')


print(sal.head(4))

# print(sal.info())

# print(sal['BasePay'].mean())

# print(sal['OvertimePay'].max())

print("***************")

# print(sal[sal['EmployeeName'] == 'JOSEPH dRISCOLL'.upper()]['JobTitle'])

# print(sal.groupby('Year').mean()['BasePay'])  
print(sal['JobTitle'].unique())
 
print(sal['JobTitle'].nunique())

print(sal['JobTitle'].value_counts().head(5))

print(sum(sal['JobTitle'].apply(lambda x: 'chief' in x.lower().split())))
