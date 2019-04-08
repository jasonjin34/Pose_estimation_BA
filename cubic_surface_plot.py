from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib._png import read_png
from sphere_cubic import projection_test_fun, projection_origin, Sphere, Cubic, listcopy
from pylab import *

mpl.rcParams['legend.fontsize'] = 10
# TO Do : 1. cubic surface plot
fig = plt.figure(figsize=(12, 12))

'''plot image in 3d space'''
img = read_png("Image/smallpng.png")
edge_size = (img.shape[0]) / 2
z, y = ogrid[-edge_size:edge_size, -edge_size:edge_size]
x = (y*0 + z*0 + edge_size)

'''sphere coordinaten system '''
r = []
z_projection_reverse = z.copy()
y_projection_reverse = y.copy()
x_projection_reverse = x.copy()
r_ratio_list = []

print(z)
print(y)
print(x)

x_projection_reverse_min = x_projection_reverse[0][0]
for index_z in range(len(z)):
    for index_y in range(len(z)):
        temp = edge_size / np.sqrt(np.power(z[index_z], 2) + np.power(y[0][index_y], 2) + edge_size * edge_size)
        r_ratio_list.append(temp)
        x_projection_reverse[index_z][index_y] = x[index_z][index_y] * temp
        if x_projection_reverse_min > x[index_z][index_y]*temp:
            x_projection_reverse_min = x[index_z][index_y]*temp
ratio = x_projection_reverse_min / edge_size
for index_z in range(len(z)):
    z_projection_reverse[index_z] = z_projection_reverse[index_z]*ratio
    y_projection_reverse[0][index_z] = y_projection_reverse[0][index_z] * ratio

'''image projection cubic '''
cubic_image = Cubic(edge_size*2, 150, 2)
cubic_image.generate_data()

'''generate sphere'''
sphere = Sphere(300, edge_size, 10)
sphere.generate_data()

'''projection image in sphere'''
ax_image = fig.add_subplot(111, projection='3d')
ax_image.plot(cubic_image.cubic_data_display[0], cubic_image.cubic_data_display[1], cubic_image.cubic_data_display[2], 'g', label='parametric curve', linewidth=0.5)
ax_image.plot(sphere.sphere_data_display[0], sphere.sphere_data_display[1], sphere.sphere_data_display[2], 'c', label='parametric curve', linewidth=1)
#ax_image.plot_surface(x, y, z, rstride=2, cstride=2, facecolors=img)
ax_image.plot_surface(x_projection_reverse, y_projection_reverse, z_projection_reverse, rstride=5, cstride=5, facecolors=img)

ax_image.set_xlabel('X Label')
ax_image.set_ylabel('Y Label')
ax_image.set_zlabel('Z Label')

plt.show()