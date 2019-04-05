import numpy as np
import matplotlib.pyplot as plt
from svmutil import *
from svm import *
import pdb

#train
y, x = svm_read_problem('total_scale')
prob = svm_problem(y[70:], x[70:])
param = svm_parameter('-c 4 -g 0.5')
model = svm_train(prob, param)

#load model
#model = svm_load_model('test.model')

#predict
plabel, _, _ = svm_predict(y[:70], x[:70], model)

#transform training data to numpy array
ytrain = np.asarray(y[70:])
xtrain_dict = x[70:]
xtrain = np.zeros([len(xtrain_dict), 4])
for l in range(0, len(xtrain_dict)):
	for idx in range(1, 5):
		try:
			xtrain[l, idx-1] = xtrain_dict[l][idx]
		except:
			xtrain[l, idx-1] = 0

# create the plot figure
fig, ax = plt.subplots(2, 3)

# config 
max_val = 1
min_val = -1

##1 VS 2
#make grid point
xi, yi = np.meshgrid(np.arange(min_val, max_val+0.1, 0.1), 
					np.arange(min_val, max_val+0.1, 0.1))
#make decision boundary
dd = [] 
dd_label = []
for idx1 in np.arange(min_val, max_val+0.1, 0.1):
	for idx2 in np.arange(min_val, max_val+0.1, 0.1):
		dd.append({1:idx2, 2:idx1})
		dd_label.append(-1)
plabel, _, _ = svm_predict(dd_label, dd, model)
plabel = np.asarray(plabel)
pos = np.where(plabel==1.0)
neg = np.where(plabel==-1.0)
Z = np.zeros(len(dd))
Z[pos] = 1
Z = Z.reshape(xi.shape)
ax[0, 0].contourf(xi, yi, Z, alpha=0.3)
#draw training data
pos = np.where(ytrain==1)
neg = np.where(ytrain==-1)
ax[0, 0].scatter(xtrain[pos, 0], xtrain[pos, 1], c='b', s=5)
ax[0, 0].scatter(xtrain[neg, 0], xtrain[neg, 1], c='r', s=5)
ax[0, 0].set_title('1 vs 2')


##1 VS 3
#make grid point
xi, yi = np.meshgrid(np.arange(min_val, max_val+0.1, 0.1), 
					np.arange(min_val, max_val+0.1, 0.1))
#make decision boundary
dd = [] 
dd_label = []
for idx1 in np.arange(min_val, max_val+0.1, 0.1):
	for idx2 in np.arange(min_val, max_val+0.1, 0.1):
		dd.append({1:idx2, 3:idx1})
		dd_label.append(-1)
plabel, _, _ = svm_predict(dd_label, dd, model)
plabel = np.asarray(plabel)
pos = np.where(plabel==1.0)
neg = np.where(plabel==-1.0)
Z = np.zeros(len(dd))
Z[pos] = 1
Z = Z.reshape(xi.shape)
ax[0, 1].contourf(xi, yi, Z, alpha=0.3)
#draw training data
pos = np.where(ytrain==1)
neg = np.where(ytrain==-1)
ax[0, 1].scatter(xtrain[pos, 0], xtrain[pos, 2], c='b', s=5)
ax[0, 1].scatter(xtrain[neg, 0], xtrain[neg, 2], c='r', s=5)
ax[0, 1].set_title('1 vs 3')


##1 VS 4
#make grid point
xi, yi = np.meshgrid(np.arange(min_val, max_val+0.1, 0.1), 
					np.arange(min_val, max_val+0.1, 0.1))
#make decision boundary
dd = [] 
dd_label = []
for idx1 in np.arange(min_val, max_val+0.1, 0.1):
	for idx2 in np.arange(min_val, max_val+0.1, 0.1):
		dd.append({1:idx2, 4:idx1})
		dd_label.append(-1)
plabel, _, _ = svm_predict(dd_label, dd, model)
plabel = np.asarray(plabel)
pos = np.where(plabel==1.0)
neg = np.where(plabel==-1.0)
Z = np.zeros(len(dd))
Z[pos] = 1
Z = Z.reshape(xi.shape)
ax[0, 2].contourf(xi, yi, Z, alpha=0.3)
#draw training data
pos = np.where(ytrain==1)
neg = np.where(ytrain==-1)
ax[0, 2].scatter(xtrain[pos, 0], xtrain[pos, 3], c='b', s=5)
ax[0, 2].scatter(xtrain[neg, 0], xtrain[neg, 3], c='r', s=5)
ax[0, 2].set_title('1 vs 4')


##2 VS 3
#make grid point
xi, yi = np.meshgrid(np.arange(min_val, max_val+0.1, 0.1), 
					np.arange(min_val, max_val+0.1, 0.1))
#make decision boundary
dd = [] 
dd_label = []
for idx1 in np.arange(min_val, max_val+0.1, 0.1):
	for idx2 in np.arange(min_val, max_val+0.1, 0.1):
		dd.append({2:idx2, 3:idx1})
		dd_label.append(-1)
plabel, _, _ = svm_predict(dd_label, dd, model)
plabel = np.asarray(plabel)
pos = np.where(plabel==1.0)
neg = np.where(plabel==-1.0)
Z = np.zeros(len(dd))
Z[pos] = 1
Z = Z.reshape(xi.shape)
ax[1, 0].contourf(xi, yi, Z, alpha=0.3)
#draw training data
pos = np.where(ytrain==1)
neg = np.where(ytrain==-1)
ax[1, 0].scatter(xtrain[pos, 1], xtrain[pos, 2], c='b', s=5)
ax[1, 0].scatter(xtrain[neg, 1], xtrain[neg, 2], c='r', s=5)
ax[1, 0].set_title('2 vs 3')


##2 VS 4
#make grid point
xi, yi = np.meshgrid(np.arange(min_val, max_val+0.1, 0.1), 
					np.arange(min_val, max_val+0.1, 0.1))
#make decision boundary
dd = [] 
dd_label = []
for idx1 in np.arange(min_val, max_val+0.1, 0.1):
	for idx2 in np.arange(min_val, max_val+0.1, 0.1):
		dd.append({2:idx2, 4:idx1})
		dd_label.append(-1)
plabel, _, _ = svm_predict(dd_label, dd, model)
plabel = np.asarray(plabel)
pos = np.where(plabel==1.0)
neg = np.where(plabel==-1.0)
Z = np.zeros(len(dd))
Z[pos] = 1
Z = Z.reshape(xi.shape)
ax[1, 1].contourf(xi, yi, Z, alpha=0.3)
#draw training data
pos = np.where(ytrain==1)
neg = np.where(ytrain==-1)
ax[1, 1].scatter(xtrain[pos, 1], xtrain[pos, 3], c='b', s=5)
ax[1, 1].scatter(xtrain[neg, 1], xtrain[neg, 3], c='r', s=5)
ax[1, 1].set_title('2 vs 4')


##3 VS 4
#make grid point
xi, yi = np.meshgrid(np.arange(min_val, max_val+0.1, 0.1), 
					np.arange(min_val, max_val+0.1, 0.1))
#make decision boundary
dd = [] 
dd_label = []
for idx1 in np.arange(min_val, max_val+0.1, 0.1):
	for idx2 in np.arange(min_val, max_val+0.1, 0.1):
		dd.append({3:idx2, 4:idx1})
		dd_label.append(-1)
plabel, _, _ = svm_predict(dd_label, dd, model)
plabel = np.asarray(plabel)
pos = np.where(plabel==1.0)
neg = np.where(plabel==-1.0)
Z = np.zeros(len(dd))
Z[pos] = 1
Z = Z.reshape(xi.shape)
ax[1, 2].contourf(xi, yi, Z, alpha=0.3)
#draw training data
pos = np.where(ytrain==1)
neg = np.where(ytrain==-1)
ax[1, 2].scatter(xtrain[pos, 2], xtrain[pos, 3], c='b', s=5)
ax[1, 2].scatter(xtrain[neg, 2], xtrain[neg, 3], c='r', s=5)
ax[1, 2].set_title('3 vs 4')

plt.show()

