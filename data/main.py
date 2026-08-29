import pandas as pd
import numpy as np

df =pd.read_csv(r"C:\Users\LNMIIT\Downloads\heart.csv")
# Data Loading & Initial Exploration
print(df.head(8))
print(df.tail())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())

print("==============================================================")

# print(2. Cleaning and column manipulation)

print(df.isnull().sum())
print(df.rename(columns={'trestbps':'resting_bp','thalach':'max_heart_rate'},inplace=True))
df['temp_id']=np.arange(1,len(df)+1)
df.drop_duplicates(inplace=True)
df.replace("?",np.nan,inplace=True)
df.fillna(df.median(numeric_only=True),inplace=True)
# print(df.head())
high_risk=df[(df["age"]>55)&(df["resting_bp"]>140)]
# print(df.iloc[0:10,0:5])

chol_arr = df["chol"].to_numpy()
age_arr = df["age"].to_numpy()


mean_chol = np.mean(chol_arr)
std_chol = np.std(chol_arr)

