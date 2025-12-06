'''
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
Loads a dataset with assosciated attribute names, then reports on details
of the dataset including statistics and graphs
'''

# Load libraries
# Load necessary libraries for data analysis and visualization
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


# Load dataset
# Specify the filename of the dataset (must be in the same directory)
file = "iris.csv"
# Define column names that will label the dataset's columns when loaded
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# load data from the csv file with columns labeled by 'names' into a DataFrame called 'dataset'
dataset = pandas.read_csv(file, names=names)

# shape
# print the dimensions (rows, columns) of the dataset
print(dataset.shape)

# head
# print the first 20 rows of the dataset to preview the structure and values
print(dataset.head(20))

# descriptions
# print summary statistics for each numeric column (count, mean, std, min, quartiles, max)
print(dataset.describe())

# class distribution
# print how many samples belong to each class (Iris species)
print(dataset.groupby('class').size())

# box and whisker plots
# create box and whisker plots for each numeric feature to show distribution and outliers
dataset.plot(kind='box', subplots=True, layout=(
    2, 2), sharex=False, sharey=False)
# save the boxplot figure to a PNG file
plt.savefig('box.png')
print("Saved boxplot image as 'box.png'. You can open this file from the same folder to view the box-and-whisker plots.")

# histograms
# create histograms for each numeric feature to show frequency distribution
dataset.hist()
# save the histogram figure to a PNG file
plt.savefig('hist.png')
print("Saved histogram image as 'hist.png'. It shows frequency distributions for each numeric column.")

# scatter plot matrix
# create a scatter-plot matrix to show relationships between numeric variables
scatter_matrix(dataset)
# save the scatter matrix figure to a PNG file
plt.savefig('matrix.png')
print("Saved scatter matrix image as 'matrix.png'. It visualizes relationships between numeric features.")

print()
print("All PNG files (box.png, hist.png, matrix.png) were saved in the same folder as this script.")
print("To open them in VSCode: right-click the image in the Explorer panel and select 'Open Preview'.")
