import pandas

df1 = pandas.read_csv("archivos/supermarkets/supermarkets.csv")
df2 = pandas.read_json("archivos/supermarkets/supermarkets.json")
df3 = pandas.read_excel("archivos/supermarkets/supermarkets.xlsx", sheet_name=0)
df4 = pandas.read_csv("archivos/supermarkets/supermarkets-commas.txt")
df5 = pandas.read_csv("archivos/supermarkets/supermarkets-semi-colons.txt", sep=";")

print(df5)