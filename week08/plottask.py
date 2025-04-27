# plottask.py
# Author: Marcin Kaminski

"""
This program displays:
- a histogram of a normal distribution of a 1000 values with 
a mean of 5 and standard deviation of 2, 
- and a plot of the function  h(x)=x³ in the range 0 to 10, 
on the one set of axes.
"""

# Import required libraries
import seaborn as sns # seaborn: a library for creating beautiful and informative statistics
# Referenced from [28]: https://seaborn.pydata.org/

import matplotlib.pyplot as plt # matplotlib.pyplot: a library for creating visualizations in Python
# Referenced from [29]: https://matplotlib.org/stable/tutorials/introductory/pyplot.html

import numpy as np # numpy: a package for handling mathematics and multidimensional arrays
# Referenced from [30]: https://numpy.org/doc/stable/user/absolute_beginners.html

import pandas as pd # pandas: a data analysis and manipulation package
# Referenced from [31]: https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html

from scipy.stats import norm # scipy.stats.norm: allows you to generate data according 
# to a normal distribution
# Referenced from [32]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html


# Create a sample from a normal distribution
mu, sigma = 5, 2  # mean and standard deviation
np.random.seed(1) # Seeding random number generator.The results will be the same every time 
# the program is run, if the seed value is identical.
# Referenced from [33]: https://numpy.org/doc/stable/reference/random/generated/numpy.random.seed.html

s = np.random.normal(mu, sigma, 1000) # Then we create a sample of 1000 values ​​
# from the normal distribution
# Referenced from [34]: https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html

# Create a range for the function h(x) = x^3
x = np.linspace(0, 10, num=1000) # This code creates a sequence of 1000 numbers (between 0 and 10). 
# This means that we have 1000 evenly distributed points between 0 and 10.
# Referenced from [35]: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html

y = x**3 # Then we generate the 'y' values ​​for these points.

# Create a DataFrame using Pandas
"""
In the next step, we create two dataframes using Pandas library.
The first dataframe 'df' contains two columns: "x" and "h(x)"
The second dataframe 'df_sample' contains one column 'Normal Distribution', 
which represents our sample from the normal distribution.
"""
# The first dataframe 'df' contains two columns: "x" and "h(x)"
df = pd.DataFrame({'x': x, 'h(x)': y})
# Referenced from [36]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

# The second dataframe 'df_sample' contains one column 'Normal Distribution',
# which represents our sample from the normal distribution.
df_sample = pd.DataFrame({'Normal Distribution': s})
# Referenced from [36]: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html

# Figure
# This code creates a figure with a size of 10 x 6 inches.
plt.figure(figsize=(10, 6))
# Referenced from [37]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html

# Draw a histogram
# The histogram is created using the seaborn library.
sns.histplot(data=df_sample, x="Normal Distribution", color="skyblue", label="Histogram", bins=30)
# The color is set to light blue and the label is 'Histogram'. The number of bins is 30.
# Referenced from [38]: https://seaborn.pydata.org/generated/seaborn.histplot.html

# Add vertical lines for mean and standard deviation
# The mean is represented by the variable 'mu' and the standard deviation by the variable 'sigma'. 
plt.axvline(mu, color='blue', linestyle='dashed', linewidth=1, label='Mean') # Mean
plt.axvline(mu + 3*sigma, color='green', linestyle='dotted', linewidth=1, label='+3σ')
plt.axvline(mu - 3*sigma, color='green', linestyle='dotted', linewidth=1, label='-3σ')
# Referenced from [39]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.axvline.html


# Draw a plot h(x) = x^3
# The plot is created using the seaborn library.
sns.lineplot(data=df, x="x", y="h(x)", color="green", label="h(x) = x³")
# The color is set to green and the label is "h(x) = x^3".
# Referenced from [40]: https://seaborn.pydata.org/generated/seaborn.lineplot.html


"""
*** The following section (Gaussian curve plotting) was developed with 
guidance from ChatGPT (OpenAI) ***
---------------------------------------------------------------------------
"""

# Create a range of x values for the Gaussian curve
x_pdf = np.linspace(min(s), max(s), 1000)
# Referenced from [41]: https://numpy.org/doc/stable/reference/generated/numpy.linspace.html


# Compute the PDF for the normal distribution
# using the mean and standard deviation of the sample
# The PDF is calculated using the scipy.stats.norm.pdf function.
pdf = norm.pdf(x_pdf, mu, sigma)
# Referenced from [42]: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html

# Multiply by bin width and number of samples to match histogram height
# The bin width is calculated as the range of the sample divided by the number of bins (30).
bin_width = (max(s) - min(s)) / 30 

# Scale the PDF to match the histogram
# The PDF is scaled by multiplying it by the number of samples (len(s)) and the bin width.
pdf_scaled = pdf * len(s) * bin_width

# Plot the Gaussian curve
# The Gaussian curve is plotted using the matplotlib library.
plt.plot(x_pdf, pdf_scaled, color="red", label="Gaussian Curve")
# The color is set to red and the label is "Gaussian Curve".
# Referenced from [43]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

"""
Note: 
PDF stands for Probability Density Function.
It gives you the relative likelihood of a random variable 
(in this case from a normal distribution).
It is important to note that the area under the PDF curve
is equal to 1.
--------------------------------------------------------------------------
"""
# Referenced from [44]: https://stackoverflow.com/questions/43602270/what-is-probability-density-function-in-the-context-of-scipy-stats-norm
# Referenced from [45]: https://en.wikipedia.org/wiki/Probability_density_function



# Add labels of x and y axes
plt.xlabel("x")
plt.ylabel("y")
# Referenced from [46]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html

# Add title and legend
plt.title("Histogram and h(x) = x³ function")
# Referenced from [47]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html
plt.legend()
# Referenced from [48]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html

# Add grid
plt.grid(True) # Finally, we enable the grid on the chart using "plt.grid(True)".
# Referenced from [49]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html

""" 
Last but not least, we save the generated plot to the file 'plottask.png' 
and display it on the screen
"""

# Save the plot to a file
plt.savefig("plottask.png")
# Referenced from [50]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

# Show the plot
plt.show()
# Referenced from [51]: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html

# End


