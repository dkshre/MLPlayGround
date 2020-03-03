print(__doc__)

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.linear_model import LinearRegression

# Loading some example data
X, y = datasets.load_boston(return_X_y=True)

# Training classifiers
reg3 = LinearRegression()

reg3.fit(X, y)


xt = X[:20]

plt.figure()


plt.plot(reg3.predict(xt), 'ys', label='LinearRegression')

plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)

plt.ylabel('predicted')
plt.xlabel('training samples')

plt.legend(loc="best")
plt.title('Comparison of individual predictions with averaged')
plt.show()
