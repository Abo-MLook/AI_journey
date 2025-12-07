import pandas as pd

# Load the CSV files into DataFrames
df_2010 = pd.read_csv(r"C:\Users\memom\Downloads\MERGED2010_11_PP.csv", on_bad_lines='skip')
df_2012 = pd.read_csv(r"C:\Users\memom\Downloads\MERGED2012_13_PP.csv", on_bad_lines='skip')
df_2013 = pd.read_csv(r"C:\Users\memom\Downloads\MERGED2013_14_PP.csv", on_bad_lines='skip')

# Print the first few rows of each DataFrame
print("2011 DataFrame:")
print(df_2011.head())

print("\n2012 DataFrame:")
print(df_2012.head())

print("\n2013 DataFrame:")
print(df_2013.head())
print()
print(df_2011.head(3))

print(len(df_2010))
print(len(df_2012))
print(len(df_2013))

# this one bitter to see in coursera