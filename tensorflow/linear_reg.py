
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

'''
x = [1, 2, 3, 4, 5, 6]
y = [1.27, 2.1, 2.92, 3.4, 4.8, 8.4]
best_fit = np.polyfit(x,y,3)

new_y = np.polyval(best_fit, x)

plt.plot(x, new_y)
plt.plot(x, y, 'bo')
plt.axis([0, x[-1]+1, 0, y[-1]+1])
#plt.show()
'''

import pandas as pd

traindata = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/train.csv")
evaldata = pd.read_csv("https://storage.googleapis.com/tf-datasets/titanic/eval.csv")

#plt.plot(
plt.subplot(traindata.sex.hist(bins=2))
plt.show()
plt.subplot(traindata.age.hist(bins=20))
plt.show()


#print(traindata.describe())

y_train = traindata.pop('survived')
y_eval = evaldata.pop('survived')

#print(traindata, '\n', evaldata)

