import numpy as np  
import matplotlib.pyplot as plt
import pandas as pd 
import csv
#read the file
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [x for x in dataset[i]]
	return dataset


file_name = 'pima-indians-diabetes.csv'
df = loadCsv(file_name)
# df.head(n=10)

# class_label = pd.DataFrame(df.iloc[:,-1])
# class_label.columns = ['label']
# df = df.iloc[:, :-1]
# df.head(n=10)

# df = df.sub(df.mean(axis=0), axis=1)

df_mat = np.asmatrix(df)
sigma = np.cov(df_mat.T)

eigVals, eigVec = np.linalg.eig(sigma)

sorted_index = eigVals.argsort()[::-1] 
eigVals = eigVals[sorted_index]
eigVec = eigVec[:,sorted_index]
eigVec = eigVec[:,:2]

transformed = df_mat.dot(eigVec)

#horizontally stack transformed data set with class label.
final_df = np.hstack((transformed, class_label))

#convert the numpy array to data frame
final_df = pd.DataFrame(final_df)

#define the column names
final_df.columns = ['x','y','label']

groups = final_df.groupby('label')
figure, axes = plt.subplots()
axes.margins(0.05)
for name, group in groups:
    axes.plot(group.x, group.y, marker='o', linestyle='', ms=6, label=name)
    axes.set_title("PCA on pca_a.txt")
axes.legend()
plt.xlabel("principal component 1")
plt.ylabel("principal component 2")
plt.show()

