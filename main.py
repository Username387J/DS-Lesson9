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
sepal56=df[df["sepal_length"]> 5 and df["sepal_length"]<6]
print(sepal56) 
# 16. Sort the dataset by petal length in ascending order.
# 17. Sort the dataset by sepal width in descending order.
# 18. Display only the sepal_length, petal_length, and species columns.
# 19. Find the first 10 flowers with the largest petal width.
# 20. Display all flowers except those belonging to the setosa species.

# Focus: Mean, median, maximum, minimum, and aggregation.
# 21. Calculate the average sepal length.
# 22. Find the maximum and minimum petal length.
# 23. Calculate the average petal width.
# 24. Find the median sepal width.
# 25. Calculate the standard deviation of petal length.
# 26. Find the total number of flowers belonging to each species.
# 27. Calculate the average sepal length for each species.
# 28. Find the average petal width for each species.
# 29. Identify which species has the highest average petal length.
# 30. Calculate the maximum sepal length for each species.