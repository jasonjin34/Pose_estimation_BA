from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib._png import read_png
from sphere_cubic import projection_test_fun, projection_origin, Sphere, Cubic, listcopy
from pylab import *

mpl.rcParams['legend.fontsize'] = 10
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# TO Do : 1. cubic surface plot

#def reverse_projection(img):
'''example code for left size cubic surface projection'''
'''
img = read_png("Image/markt.png")
edge_size = (img.shape[0]) / 2

output_data = reverse_projection(img)

z, y = ogrid[-edge_size:edge_size, -edge_size:edge_size]
x = (y*0 + z*0 + edge_size)

#sphere coordinaten system 
z_projection_reverse = z.copy()
y_projection_reverse = y.copy()
x_projection_reverse = x.copy()

for index in range(len(z)):
    z_projection_reverse[index] = z_projection_reverse[index]/np.sqrt(3)
    y_projection_reverse[0][index] = y_projection_reverse[0][index]/np.sqrt(3)

for index_z in range(len(z)):
    for index_y in range(len(z)):
        x_projection_reverse[index_z][index_y] = np.sqrt(pow(edge_size, 2) - pow(y_projection_reverse[0][index_y], 2) - pow(z_projection_reverse[index_z], 2))
'''
def reverse_projection(img):
    edge_size = (img.shape[0])/2
    output_data = [[], [], []]
    input_data = [[], [], []]
    input_data[0], input_data[1] = ogrid[-edge_size:edge_size, -edge_size:edge_size]
    input_data[2] = (input_data[0]*0 + input_data[1]*0 + edge_size)
    output_data[0] = input_data[0].copy()
    output_data[1] = input_data[1].copy()
    output_data[2] = input_data[2].copy()

    for index in range(len(input_data[0])):
        output_data[0][index] = output_data[0][index] / np.sqrt(3)
        output_data[1][0][index] = output_data[1][0][index] / np.sqrt(3)

    for index_z in range(len(input_data[0])):
        for index_y in range(len(input_data[0])):
            output_data[2][index_z][index_y] = np.sqrt(
                pow(edge_size, 2) - pow(output_data[1][0][index_y], 2) - pow(output_data[0][index_z], 2))
    return output_data

def reference_projection(img):
    edge_size = (img.shape[0])/2
    output_data = [[], [], []]
    output_data[0], output_data[1] = ogrid[-edge_size:edge_size, -edge_size:edge_size]
    output_data[2] = (output_data[0]* 0 + output_data[1]*0 - edge_size)
    return output_data

'''plot image in 3d space'''
img = read_png("Image/markt.png")
edge_size = (img.shape[0]) / 2

output_data = reverse_projection(img)
output_data_reference = reference_projection(img)

'''image projection cubic '''
cubic_image = Cubic(edge_size*2, 150, 2)
cubic_image.generate_data()


'''generate sphere'''
sphere = Sphere(300, edge_size, 10)
sphere.generate_data()

##projection
edge_length = edge_size
data = [[],[],[]]
data = listcopy(sphere.sphere_data_display)
projection_origin(data, edge_length)
#generate projection test data
test_sampe_size = 5
data_projection_test =[[], [], []]
data_projection_test = projection_test_fun(test_sampe_size, data)


'''the reference projection'''
fig = plt.figure(figsize=(18, 8.5))
plt.title("肥仔快乐球 ")
ax = fig.add_subplot(122, projection='3d')
ax.plot(sphere.sphere_data_display[0], sphere.sphere_data_display[1], sphere.sphere_data_display[2], 'k', label='parametric curve', linewidth=1)
ax.plot(cubic_image.cubic_data_display[0], cubic_image.cubic_data_display[1], cubic_image.cubic_data_display[2], 'g', label='parametric curve', linewidth=0.5)
ax.scatter(data[0], data[1], data[2], 'r', marker='o', s = 1, color = 'r')
ax.plot(data_projection_test[0], data_projection_test[1], data_projection_test[2], 'b', label='parametric curve', linewidth =1.5)

'''projection image in sphere'''
ax_image = fig.add_subplot(121, projection='3d')
ax_image.plot(cubic_image.cubic_data_display[0], cubic_image.cubic_data_display[1], cubic_image.cubic_data_display[2], 'g', label='parametric curve', linewidth=0.5)
ax_image.plot(sphere.sphere_data_display[0], sphere.sphere_data_display[1], sphere.sphere_data_display[2], 'c', label='parametric curve', linewidth=1)
ax_image.plot_surface(output_data[2], output_data[1], output_data[0], rstride=5, cstride=5, facecolors=img)
ax_image.plot_surface(output_data_reference[2], output_data_reference[1], output_data_reference[0], rstride=5, cstride=5, facecolors=img)

ax_image.set_xlabel('X Label')
ax_image.set_ylabel('Y Label')
ax_image.set_zlabel('Z Label')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


plt.show()