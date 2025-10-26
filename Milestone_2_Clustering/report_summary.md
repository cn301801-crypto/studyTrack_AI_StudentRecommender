# Milestone 2: Clustering and Pattern Detection

## Objective
The objective of this milestone is to perform behavior clustering and pattern detection on student data. By analyzing key numerical features, we aim to group students based on study habits and performance to identify meaningful patterns.

## Dataset Source
- *Files used:* student-mat.csv and student-por.csv
- *Source:* UCI Machine Learning Repository – Student Performance Dataset
- *Description:* These datasets contain student demographic, social, and academic information along with grades (G1, G2, G3) in secondary education.

## Steps Followed
1. *Data Loading and Combination:*  
   - Loaded student-mat.csv and student-por.csv using pandas with sep=';'.  
   - Combined both datasets into a single DataFrame for analysis.  

2. *Data Cleaning:*  
   - Stripped column names of extra spaces and converted to lowercase.  
   - Selected numerical features relevant for clustering: age, studytime, failures, absences, g1, g2, g3.  

3. *Feature Scaling and Dimensionality Reduction:*  
   - Standardized features using StandardScaler.  
   - Applied PCA to reduce dimensions to 2 for visualization.  

4. *Clustering:*  
   - Applied K-Means clustering with 3 clusters.  
   - Added cluster labels to the dataset.  
   - Summarized each cluster by calculating the mean of key features.

5. *Visualization:*  
   - *Scatter Plot (PCA):* Shows clusters in 2D. (visualizations/cluster_scatter.png)  
   - *Cluster Characteristics Bar Plot:* Mean of key metrics per cluster. (visualizations/cluster_profile_bar.png)  
   - *Correlation Heatmap:* Displays correlations among numeric features. (visualizations/correlation_heatmap.png)  

## Tools Used
- *Python* (3.10)  
- *Libraries:* Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- *Environment:* PyCharm with Jupyter Notebook  

## Key Insights
- *Cluster 0:* Large-sized cluster; students higher studytime and grades.  
- *Cluster 1:* Medium-cluster; students with medium studytime and lower grades, indicating low engagement.  
- *Cluster 2:* Low-cluster; students with low studytime and better grades, representing high performance and engagement.  
- Clusters help identify patterns of study habits and academic performance, useful for recommending personalized study strategies.

## Visualizations
- *Scatter Plot (PCA):* visualizations/cluster_scatter.png  
- *Bar Plot (Cluster Profile):* visualizations/cluster_profile_bar.png  
- *Correlation Heatmap:* visualizations/correlation_heatmap.png