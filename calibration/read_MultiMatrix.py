import numpy as np

loaded_arrays = np.load("MultiMatrix.npz")
print (loaded_arrays.files)
print()
print(loaded_arrays["camMatrix"])
print()
print(loaded_arrays["distCoef"])