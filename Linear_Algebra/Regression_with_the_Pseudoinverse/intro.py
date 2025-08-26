import matplotlib.pyplot as plt
import numpy as np


#For regression problems, we typically have many more cases (n, or rows of X) than features to predict (columns of X).
#Let’s solve a miniature example of such an overdetermined situation.
#We have eight data points (n = 8):


x1 = [0, 1, 2, 3, 4, 5, 6, 7.] # E.g.: Dosage of drug for treating Alzheimer's disease
y = [1.86, 1.31, .62, .33, .09, -.67, -1.23, -1.37] # E.g.: Patient's "forgetfulness score"


title = 'Clinical Trial'
xlabel = 'Drug dosage (mL)'
ylabel = 'Forgetfulness'

fig, ax = plt.subplots()
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
_ = ax.scatter(x1, y)
plt.show()