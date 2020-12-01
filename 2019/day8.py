import numpy as np
import matplotlib.pyplot as plt

with open('inputs/day8.txt', 'r') as f:
    image = next(f)
    image = [int(n) for n in image]

width = 25
height = 6
n_pixels = len(image)
n_layers = n_pixels // width // height
arr = np.array(image).reshape((n_layers, height, width))

min_layer = 0
min_zeros = width * height
for l in range(n_layers):
    unique, counts = np.unique(arr[l, :, :], return_counts=True)
    dic = dict(zip(unique, counts))
    n_zeros = dic[0]
    if n_zeros < min_zeros:
        min_zeros = n_zeros
        min_layer = l

unique, counts = np.unique(arr[min_layer, :, :], return_counts=True)
dic = dict(zip(unique, counts))
print("Part 1:", dic[1] * dic[2])

decoded_image = np.empty((height, width))
decoded_image[:] = np.nan

for l in range(n_layers):

    layer = arr[l, :, :]
    layer_i = np.nonzero(np.logical_or(layer == 0, layer == 1))

    for i in range(len(layer_i[0])):
        ind = tuple([layer_i[0][i], layer_i[1][i]])
        if np.isnan(decoded_image[ind]):
            decoded_image[ind] = layer[ind]

plt.imshow(decoded_image)
plt.show()
