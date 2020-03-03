boston = load_boston();

type(boston)

type(boston)

boston.keys()

type(boston['data'])

boston['feature_names']

print(boston['DESCR'])
 
boston['data'].shape


row = boston['data'][17]
row.reshape(-1, 10)

boston['target'][17]
