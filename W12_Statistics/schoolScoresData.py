'''
School Scores Data Analysis using Pandas
Analyzes SAT school performance data from the CORGIS dataset.

Dataset source: https://corgis-edu.github.io/corgis/csv/school_scores/

Loads a dataset with SAT and GPA-related information, then reports on
statistics and generates graphs.'''

# Load libraries
# Load necessary libraries for data analysis and visualization
import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt


# Load dataset
# Specify the filename of the dataset (must be in the same directory)
file = "school_scores.csv"
# Define column names that will label the dataset's columns when loaded
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
# load data from the csv file with columns labeled by 'names' into a DataFrame called 'dataset'
#dataset = pandas.read_csv(file, names=names)
dataset = pandas.read_csv(file)

# select 5 numeric columns to analyze
dataset = dataset[[
    "Total.Math",
    "Total.Verbal",
    "Total.Test-takers",
    "Academic Subjects.Mathematics.Average GPA",
    "Academic Subjects.English.Average GPA"
]]

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
#print(dataset.groupby('class').size())

# box and whisker plots
# create box and whisker plots for each numeric feature to show distribution and outliers
num_cols = len(dataset.columns)
rows = (num_cols + 1) // 2  # 2 plots per row
dataset.plot(
    kind='box',
    subplots=True,
    layout=(rows, 2),         # enough slots for all columns
    sharex=False,
    sharey=False,
    figsize=(10, 3*rows)
)
plt.tight_layout()
plt.savefig('school_box.png')
print("Saved boxplot image as 'school_box.png'.")
# histograms
# create histograms for each numeric feature to show frequency distribution
dataset.hist(figsize=(10, 3*rows))
plt.tight_layout()
plt.savefig('school_hist.png')
print("Saved histogram image as 'school_hist.png'.")
# scatter plot matrix
# create a scatter-plot matrix to show relationships between numeric variables
scatter_matrix(dataset)
# save the scatter matrix figure to a PNG file
plt.savefig('school_matrix.png')
print("Saved scatter matrix image as 'school_matrix.png'. It visualizes relationships between numeric features.")

print()
print("All PNG files (school_box.png, school_hist.png, school_matrix.png) were saved in the same folder as this script.")
print("To open them in VSCode: right-click the image in the Explorer panel and select 'Open Preview'.")
