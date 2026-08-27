# Exploring Eigenvalues of Random Hermitian Matrices
In this project I will be exploring the relationship between the eigenvalues of randomly generated Hermitian Matrices using Python.
## Objectives
- Generate random Hermitian matrices 
- Calculate their eigenvalues
- Investigate relationships, properties and distribution of the eigenvalues
- Produce figures to visualise the results using Matplotlib
- Analyse and interpret the results
## Experiment 1: Distribution of Eigenvalues
### Research Question
What does the distribution of eigenvalues look like when we repeatedly generate random matrices?
### Method
I generated 1000 random 3x3 Hermitian Matrices using NumPy. For each matrix, I calculated its three eigenvalues using 'numpy.linalg.eigvalsh()'. This produced 3000 eigenvalues which were collected and displayed using a Histogram using Matplotlib. 
### Results
The distribution of the eigenvalues was centred around zero, with the frequency decreasing towards the more positive and negative eigenvalue ends.

Summary:
- Standard Deviation: 1.420
- Mean Eigenvalue: -0.027
- Minimum Eigenvalue: -3.998
- Maximum Eigenvalue: 4.134
### Interpretation
The mean eigenvalue -0.027 is close to zero which indicates that the eigenvalues are centred around zero. This is consistent with the random matrix entries being generated around zero. The minimum and maximum eigenvalues show the range over which the eigenvalues occurred, ranging from -3.998 to 4.134. The distribution was approximately symmetric around zero, with there being fewer eigenvalues at the positive and negative ends. Since the matrices are Hermitian, all the eigenvalues must be real. Therefore, the Histogram provides a way of investigating how real eigenvalues are distributed across many randomly generated matrices. 
### Figure 1
![Distribution of Eigenvalues](Figure_1.png)

The Histogram shows the frequency of the 3000 eigenvalues generated from the 1000 random 3x3 Hermitian matrices.
## Experiment 2: Effect of Matrix Dimension
### Research Question
How does increasing the dimension of a random Hermitian matrix affect the distribution of its eigenvalues?
### Method
I generated random Hermitian matrices of dimensions 3x3, 5x5, 10x10 and 20x20. For each dimension, 1000 random matrices were generated. The eigenvalues of each matrix were then calculated and collected for analysis. The mean, standard deviation, minimum and maximum eigenvalues were then calculated for each dimension. I produced Histograms to visualise the eigenvalue distributions with probability density used on the y-axis to allow the distributions to be compared.
### Results
| Matrix Dimension | Mean | Standard Deviation | Minimum | Maximum |
|---:|---:|---:|---:|---:|
| 3x3 | -0.0075 | 1.4158 | -3.7582 | 4.0189 | 
| 5x5 | -0.0217 | 1.7261 | -4.6422 | 4.3632 |
| 10x10 | -0.0109 | 2.3462 | -5.8965 | 6.0294 |
| 20x20 | 0.0010 | 3.2443 | -7.4746 | 7.6665 |
![3x3 eigenvalue distribution](Figure_2_3x3.png)
![5x5 eigenvalue distribution](Figure_2_5x5.png)
![10x10 eigenvalue distribution](Figure_2_10x10.png)
![20x20 eigenvalue distribution](Figure_2_20x20.png)
![Eigenvalue spread vs matrix dimension](Figure_2_summary.png)
### Interpretation 
 Increasing the matrix dimension resulted in an increase in the spread of the eigenvalues. The standard deviation increased from approximately 1.42 for 3x3 matrices to 3.24 for 20x20 matrices. The minimum and maximum eigenvalues also moved further away from zero as the dimension increased. Despite this increase in spread, the mean eigenvalue remained close to zero. This suggests that the eigenvalue distribution remained approximately centred around zero while becoming wider as the matrix dimension increased. The summary plot provides further evidence of this relationship, showing an increasing trend between matrix dimension and the standard deviation of the eigenvalues. Overall, the experiment suggests that increasing the dimension of these randomly generated Hermitian matrices causes their eigenvalues to become more dispersed around zero.
 ## Experiment 3: Largest Eigenvalue and Matrix Dimension
 ### Research Question
 How does the largest eigenvalue of a random Hermitian matrix change as the matrix dimension increases?
 ### Method
 The random Hermitian matrices of dimensions 3x3, 5x5, 10x10 and 20x20 were generated and for each dimension, 1000 random matrices were generated. The eigenvalues were calculated and given in ascending order. This allowed me to calculate the largest eigenvalue using 'eigenvalues[-1]', obtaining the final element in the array. For each matrix dimension, the mean and standard deviation of the largest eigenvalue were calculated. The results were then compared with the square root of the matrix dimension to investigate whether the mean largest eigenvalue appeared to follow a square root relationship.
 ### Results
| Matrix Dimension | Mean Largest Eigenvalue | Standard Deviation | Mean Largest Eigenvalue / $\sqrt{n}$ |
|---:|---:|---:|---:|
| 3x3 | 1.4173 | 0.7878 | 0.8596 |
| 5x5 | 2.3091 | 0.6726 | 1.0410 |
| 10x10 | 3.7214 | 0.6071 | 1.1872 |
| 20x20 | 5.3540 | 0.5640 | 1.2825 |
![Mean largest eigenvalue vs matrix dimension](Figure_3_mean_largest.png)
![Largest eigenvalue scaling with square root of matrix dimension](Figure_3_sqrt_scaling.png)
### Interpretation 
The results show an increase in the mean largest eigenvalue as matrix dimension increases. The mean largest eigenvalue increased from 1.4173 for 3x3 matrices to 5.3540 for 20x20 matrices. The standard deviation of the largest eigenvalue decreased as the matrix dimension increased, from 0.7878 for 3x3 matrices to 0.5640 for 20x20 matrices. This suggests that the largest eigenvalue became less variable as the matrix dimension increased. The relationship between matrix dimension and mean largest eigenvalue was not exactly linear as increasing the dimension from 10x10 to 20x20 doubled it, but the mean largest eigenvalue increased from 3.7214 to only 5.3540. The mean largest eigenvalue was divided by the square root of the dimension and if the largest eigenvalue was proportionate to $\sqrt{n}$, this ratio would be approximately constant. Instead the ratio increased from 0.8596 for dimension 3x3 to 1.2825 for dimension 20x20. Therefore, the results do not establish a simple $\sqrt{n}$ relationship. The increase in the ratio is gradual compared with the increase in matrix dimension, the results suggest that the relationship is sub-linear. A larger range of matrix dimension and a greater number of simulations would be required to determine the relationship more reliably.


