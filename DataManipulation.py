# shows how to manipulate bunch object
from sklearn import datasets

boston = load_boston();

type(boston)

type(boston)

boston.keys()

type(boston['data'])

boston['feature_names']

print(boston['DESCR'])
 
boston['data'].shape

#Using dot notation

boston.data.shape

boston.feature_names

boston.data[17]

boston.target[17]

#Select Specific column
boston.data[:,1]


