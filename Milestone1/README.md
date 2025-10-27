#  StudyTrack – AI-Based Student Study Habit Recommender  
## Milestone 1: Data Preprocessing & Visualization  

---

###  Objective
The goal of this milestone is to perform *data exploration, cleaning, and visualization* to understand students’ study behaviors and academic performance patterns.  
This step builds the foundation for later stages such as *clustering* and *pattern detection*, which will help recommend better study habits for students.

---

###  Dataset Source
We used the publicly available *Student Performance Dataset* from the *UCI Machine Learning Repository*:

🔗 *URL:* https://www.kaggle.com/datasets/whenamancodes/students-performance

*Files used:*
- student-mat.csv – Student performance data in Mathematics  
- student-por.csv – Student performance data in Portuguese  

Each file contains demographic, social, and academic features such as study time, family background, school support, and grades.

---

###  Steps Followed

#### 1 Dataset Loading
- Imported both CSV files (student-mat.csv, student-por.csv) using *Pandas*.
- Combined them into a single dataset using pd.concat() for unified analysis.

#### 2 Data Cleaning
- Checked for null or missing values and handled them using dropna().  
- Verified data types and removed unnecessary spaces or formatting issues.
- Renamed columns for clarity (e.g., G3 → G3_math / G3_por when merged).

#### 3 Exploratory Data Analysis (EDA)
- Calculated descriptive statistics using describe() and info().
- Identified distributions, relationships, and correlations between important variables.

#### 4 Visualization
Created *four major plots* to analyze student performance:

| Type | Purpose |
|------|----------|
|  *Histogram* | To visualize distribution of final grades (G3_math). |
|  *Scatter Plot* | To study relationship between study time and performance. |
|  *Bar Chart* | To compare average grades across schools. |
|  *Heatmap* | To visualize correlations among numeric variables. |

---

###  Tools & Libraries Used

| Tool / Library | Purpose |
|----------------|----------|
| *Python 3.10.6* | Programming Language |
| *PyCharm (Jupyter Notebook)* | Development Environment |
| *Pandas* | Data loading and cleaning |
| *Matplotlib* | Basic visualization |
| *Seaborn* | Advanced, styled visualizations |

---

###  Key Insights
- The *distribution of final grades* shows that most students score around the middle range, with fewer achieving very high or very low marks.  
- Students who *spend more time studying* generally achieve *better final grades*.  
- There are *performance differences between schools*, indicating possible institutional or teaching impacts.  
- The *heatmap* revealed a *strong correlation between G1, G2, and G3 grades*, showing consistent student performance trends.

---

### Graphs
- Histogram
- Scatter plot
- Bar chart
- Haetmap

---