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


x0 = np.ones(8)

X = np.concatenate((np.matrix(x0).T, np.matrix(x1).T), axis=1)

w = np.dot(np.linalg.pinv(X), y)

b = np.asarray(w).reshape(-1)[0]

m = np.asarray(w).reshape(-1)[1]


fig, ax = plt.subplots()

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

ax.scatter(x1, y)

x_min, x_max = ax.get_xlim()
y_at_xmin = m*x_min + b
y_at_xmax = m*x_max + b

ax.set_xlim([x_min, x_max])
_ = ax.plot([x_min, x_max], [y_at_xmin, y_at_xmax], c='C01')
plt.show()