import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATA
mat_df = pd.read_csv('data/student-mat.csv', sep=';')
por_df = pd.read_csv('data/student-por.csv', sep=';')
print("Math Dataset Shape:", mat_df.shape)
print("Portuguese Dataset Shape:", por_df.shape)

# 2. MERGE DATA ON COMMON ATTRIBUTES
merge_columns = ['school', 'sex', 'age', 'address', 'famsize', 'Pstatus',
                 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian']
merged_df = pd.merge(mat_df, por_df, on=merge_columns, suffixes=('_mat', '_por'))
print("Merged Dataset Shape:", merged_df.shape)

# 3. DATA CLEANING
print("\nMissing values before cleaning:\n", merged_df.isnull().sum())
merged_df.drop_duplicates(inplace=True)

# 4. SUMMARY STATISTICS
print("\nSummary Statistics:\n", merged_df.describe())

# 5. VISUALIZATIONS (4 GRAPHS)
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (8,5)

# Distribution of study time
plt.figure()
sns.histplot(merged_df['studytime_mat'], kde=True, color='blue', label='Math')
sns.histplot(merged_df['studytime_por'], kde=True, color='orange', label='Portuguese')
plt.title("Study Time Distribution (Math vs Portuguese)")
plt.xlabel("Study Time (hours)")
plt.legend()
plt.show()

# Boxplot - Compare Final Grades
plt.figure()
sns.boxplot(data=merged_df[['G3_mat', 'G3_por']], palette='Set2')
plt.title("Final Grade Comparison (Math vs Portuguese)")
plt.ylabel("Grade (G3)")
plt.show()

# Scatter Plot - Study Time vs Final Grade (Math)
plt.figure()
sns.scatterplot(x='studytime_mat', y='G3_mat', hue='sex', data=merged_df, palette='cool')
plt.title("Math: Study Time vs Final Grade by Gender")
plt.xlabel("Study Time")
plt.ylabel("Final Grade (G3)")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,8))
numeric_df = merged_df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), cmap='coolwarm', annot=False)
plt.title("Correlation Heatmap of Numeric Features")
plt.show()

print("\n Milestone 1 EDA Completed Successfully..")