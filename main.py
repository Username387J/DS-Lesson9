# Load the iris.csv dataset into a DataFrame named df.
import pandas as pd 

df=pd.read_csv('iris.csv')
# Display the first 5 rows of the dataset.
print(df.head())
# Display the last 10 rows.
print(df.tail(10))
# Find the total number of rows and columns.
print(df.shape)
# Display all the column names.
print(df.columns)
# Check the data types of each column.
print(df.dtypes)
# Find the total number of non-null values in each column.
print(df.count)
# Check whether the dataset contains any missing values.

# Display basic statistical information about the dataset using describe().
print(df.describe())

# Focus: Selecting specific records and applying conditions.

# 11. Display all flowers belonging to the setosa species.
setosas=df[df["species"]=="setosa"]
print("Setosas")
print(setosas)
# 12. Display flowers whose petal length is greater than 5.

petal5=df[df["petal_length"]>5]
print(petal5)
# 13. Find flowers whose sepal width is less than 3.
sepalminus3=df[df["sepal_width"]<3]
print(sepalminus3)
# 14. Display flowers having:
# Petal length greater than 4.
petalmore4=df[df["petal_length"]>4]
print(petalmore4)
# Petal width greater than 1.
petalmore1=df[df["petal_width"]>1]
print(petalmore1)
# 15. Find all flowers whose sepal length is between 5 and 6.
sepal56=df[(df["sepal_length"]>= 5) & (df["sepal_length"]<=6)]
print(sepal56) 

# 16. Sort the dataset by petal length in ascending order.
petalSorted= df.sort_values(by= "petal_length", ascending=True)
# 17. Sort the dataset by sepal width in descending order.
sepalWidth= df.sort_values(by= "sepal_width", ascending=False)
# 18. Display only the sepal_length, petal_length, and species columns.
print(df[["sepal_length","petal_length","species"]])
# 19. Find the first 10 flowers with the largest petal width.
largestWidth=df.sort_values(by="petal_width", ascending=False)
print(largestWidth.head(10))
# 20. Display all flowers except those belonging to the setosa species.
nosetosa=df[df["species"] !="setosa"]
print(nosetosa)
# Focus: Mean, median, maximum, minimum, and aggregation.
# 21. Calculate the average sepal length.
avgSepalLength=df["sepal_length"].mean()
print(avgSepalLength)
# 22. Find the maximum and minimum petal length.
maxPetalLength=df["petal_length"].max()
minPetalLength=df["petal_length"].min()
#print("Max petal length is", maxPetalLength,", and minimum petal length is", minPetalLength)
# 23. Calculate the average petal width.
print(df["petal_width"].mean())
# 24. Find the median sepal width.
# 25. Calculate the standard deviation of petal length.
# 26. Find the total number of flowers belonging to each species.
# 27. Calculate the average sepal length for each species.
# 28. Find the average petal width for each species.
# 29. Identify which species has the highest average petal length.
# 30. Calculate the maximum sepal length for each species.