from annoy import AnnoyIndex
from tqdm import trange
import h5py
import numpy as np
import random

f = h5py.File("testfile.hdf5", "w")
arr = np.arange(1000)
dset = f.create_dataset("test", data=arr)

f = h5py.File('testfile.hdf5', 'r')
dset = f['test']
print(dset.shape)

f = 40
t = AnnoyIndex(f)  # Length of item vector that will be indexed
for i in range(1000):
    v = [random.gauss(0, 1) for z in range(f)]
    t.add_item(i, v)

# 10 trees
t.build(10)
t.save('test.ann')

u = AnnoyIndex(f)
u.load('test.ann')
print("100 nearest neighbors:", u.get_nns_by_item(0, 100))

a = AnnoyIndex(3)
a.add_item(0, [10, 0, 10])
a.add_item(1, [20, 0, 0])
a.add_item(2, [10, 0, 20])
a.add_item(3, [0, 0, 30])
a.add_item(4, [0, 0, 30])
a.add_item(5, [0, 0, 50])
a.build(-1)

for i in trange(len(dset)):
    pass

print("Nearest neighbour by item:", a.get_nns_by_item(4, 100))
print("Nearest neighbour by vector:", a.get_nns_by_vector([10, 0, 30], 100))
