from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['legend.fontsize'] = 10

# TO Do : 1. Sphere generation check!
#         2. Cubic generation check!
#         2. Projection to Cubic check!
# draw sphere in sphere coordination
# coordinaten transformation

'''define Sphere class'''
class Sphere:
    '''generate sphere data generations'''
    sphere_data = [[], [], []]
    sphere_data_display = [[], [], []]

    '''constructor'''

    def __init__(self, divide_input, radius_input):
        self.divide = divide_input
        self.radius = radius_input
        '''generate the sphere data in sphere coordinate and transfer it to kartesische coordinate'''

    def generate_data(self):
        th = np.arange(0.0, np.pi * (1 + 1 / self.divide), np.pi / self.divide)
        phi = np.arange(0.0, 2 * np.pi * (1 + 1 / self.divide), 2 * np.pi / self.divide)

        # define sphere data generation functions
        th_count = 0
        for th_index in th:
            for phi_index in phi:
                self.sphere_data[0].append(self.radius * np.sin(th_index) * np.cos(phi_index))
                self.sphere_data[1].append(self.radius * np.sin(th_index) * np.sin(phi_index))
                self.sphere_data[2].append(self.radius * np.cos(th_index))
                if th_count % (self.divide / 10) == 0:
                    self.sphere_data_display[0].append(self.radius * np.sin(th_index) * np.cos(phi_index))
                    self.sphere_data_display[1].append(self.radius * np.sin(th_index) * np.sin(phi_index))
                    self.sphere_data_display[2].append(self.radius * np.cos(th_index))
            th_count = th_count + 1

        phi_count = 0
        for phi_index in phi:
            for th_index in th:
                self.sphere_data[0].append(self.radius * np.sin(th_index) * np.cos(phi_index))
                self.sphere_data[1].append(self.radius * np.sin(th_index) * np.sin(phi_index))
                self.sphere_data[2].append(self.radius * np.cos(th_index))
                if phi_count % (self.divide / 10) == 0:
                    self.sphere_data_display[0].append(self.radius * np.sin(th_index) * np.cos(phi_index))
                    self.sphere_data_display[1].append(self.radius * np.sin(th_index) * np.sin(phi_index))
                    self.sphere_data_display[2].append(self.radius * np.cos(th_index))
            phi_count = phi_count + 1

'''define cubic class '''

class Cubic:
    # define parameter
    cubic_data = [[], [], []]
    cubic_data_display = [[], [], []]

    def __init__(self, edge, divide, interval):
        self.edge = edge;
        self.divide = 1 / divide;
        self.interval = divide/interval

    def generate_data(self):
        variable_cubic_range = np.arange(-self.edge / 2, self.edge / 2 + self.edge * self.divide,
                                         self.edge * self.divide)
        # for x = d/2 there are four lines
        # first line z = d/2 y is change variable
        d = self.edge
        count_x = 0
        for variable_index_x in reversed(variable_cubic_range):
            if (count_x % self.interval == 0):
                for variable_index in variable_cubic_range:
                    self.cubic_data_display[0].append(variable_index_x)
                    self.cubic_data_display[1].append(variable_index)
                    self.cubic_data_display[2].append(d / 2)
                for variable_index in reversed(variable_cubic_range):
                    self.cubic_data_display[0].append(variable_index_x)
                    self.cubic_data_display[1].append(d / 2)
                    self.cubic_data_display[2].append(variable_index)
                for variable_index in variable_cubic_range:
                    self.cubic_data_display[0].append(variable_index_x)
                    self.cubic_data_display[1].append(variable_index)
                    self.cubic_data_display[2].append(-d / 2)
                for variable_index in variable_cubic_range:
                    self.cubic_data_display[0].append(variable_index_x)
                    self.cubic_data_display[1].append(-d / 2)
                    self.cubic_data_display[2].append(variable_index)

            for variable_index in variable_cubic_range:
                self.cubic_data[0].append(variable_index_x)
                self.cubic_data[1].append(variable_index)
                self.cubic_data[2].append(d / 2)
            for variable_index in reversed(variable_cubic_range):
                self.cubic_data[0].append(variable_index_x)
                self.cubic_data[1].append(d / 2)
                self.cubic_data[2].append(variable_index)
            for variable_index in variable_cubic_range:
                self.cubic_data[0].append(variable_index_x)
                self.cubic_data[1].append(variable_index)
                self.cubic_data[2].append(-d / 2)
            for variable_index in variable_cubic_range:
                self.cubic_data[0].append(variable_index_x)
                self.cubic_data[1].append(-d / 2)
                self.cubic_data[2].append(variable_index)
            count_x = count_x + 1

        count_y = 0
        for variable_index_z in variable_cubic_range:
            if (count_y % self.interval == 0):
                for variable_index in variable_cubic_range:
                    self.cubic_data_display[0].append(variable_index)
                    self.cubic_data_display[1].append(-d / 2)
                    self.cubic_data_display[2].append(variable_index_z)
                for variable_index in variable_cubic_range:
                    self.cubic_data_display[0].append(d / 2)
                    self.cubic_data_display[1].append(variable_index)
                    self.cubic_data_display[2].append(variable_index_z)
                for variable_index in reversed(variable_cubic_range):
                    self.cubic_data_display[0].append(variable_index_x)
                    self.cubic_data_display[1].append(d / 2)
                    self.cubic_data_display[2].append(variable_index_z)
                for variable_index in reversed(variable_cubic_range):
                    self.cubic_data_display[0].append(-d / 2)
                    self.cubic_data_display[1].append(variable_index)
                    self.cubic_data_display[2].append(variable_index_z)

            for variable_index in variable_cubic_range:
                self.cubic_data[0].append(variable_index)
                self.cubic_data[1].append(-d / 2)
                self.cubic_data[2].append(variable_index_z)
            for variable_index in variable_cubic_range:
                self.cubic_data[0].append(d / 2)
                self.cubic_data[1].append(variable_index)
                self.cubic_data[2].append(variable_index_z)
            for variable_index in reversed(variable_cubic_range):
                self.cubic_data[0].append(variable_index_x)
                self.cubic_data[1].append(d / 2)
                self.cubic_data[2].append(variable_index_z)
            for variable_index in reversed(variable_cubic_range):
                self.cubic_data[0].append(-d / 2)
                self.cubic_data[1].append(variable_index)
                self.cubic_data[2].append(variable_index_z)
            count_y = count_y + 1

        count_z = 0
        for variable_index_y in variable_cubic_range:
            if (count_z % self.interval == 0):
                for variable_index in variable_cubic_range:
                    self.cubic_data_display[0].append(variable_index)
                    self.cubic_data_display[1].append(variable_index_y)
                    self.cubic_data_display[2].append(-d / 2)
                for variable_index in variable_cubic_range:
                    self.cubic_data_display[0].append(d / 2)
                    self.cubic_data_display[1].append(variable_index_y)
                    self.cubic_data_display[2].append(variable_index)
                for variable_index in reversed(variable_cubic_range):
                    self.cubic_data_display[0].append(variable_index)
                    self.cubic_data_display[1].append(variable_index_y)
                    self.cubic_data_display[2].append(d / 2)
                for variable_index in reversed(variable_cubic_range):
                    self.cubic_data_display[0].append(-d / 2)
                    self.cubic_data_display[1].append(variable_index_y)
                    self.cubic_data_display[2].append(variable_index)

            for variable_index in variable_cubic_range:
                self.cubic_data[0].append(variable_index)
                self.cubic_data[1].append(variable_index_y)
                self.cubic_data[2].append(-d / 2)
            for variable_index in variable_cubic_range:
                self.cubic_data[0].append(d / 2)
                self.cubic_data[1].append(variable_index_y)
                self.cubic_data[2].append(variable_index)
            for variable_index in reversed(variable_cubic_range):
                self.cubic_data[0].append(variable_index)
                self.cubic_data[1].append(variable_index_y)
                self.cubic_data[2].append(d / 2)
            for variable_index in reversed(variable_cubic_range):
                self.cubic_data[0].append(-d / 2)
                self.cubic_data[1].append(variable_index_y)
                self.cubic_data[2].append(variable_index)
            count_z = count_z + 1

def listcopy(list):
    outputlist = [[], [], []]
    for index in range(len(list)):
        outputlist[index] = list[index].copy()
    return outputlist

def projection_origin(data,edge_length):
    for index in range(len(data[0])):
        # find the biggest value among x, y, z
        if abs(data[0][index]) >= abs(data[1][index]):  # x > y
            if abs(data[0][index]) >= abs(data[2][index]):  # x > z in x is biggest value
                temp_ratio = edge_length / (abs(data[0][index]) + .000001)
                data[0][index] = data[0][index] * temp_ratio
                data[1][index] = data[1][index] * temp_ratio
                data[2][index] = data[2][index] * temp_ratio
            else:  # z > x > y
                temp_ratio = edge_length / (abs(data[2][index]) + .000001)
                data[2][index] = data[2][index] * temp_ratio
                data[0][index] = data[0][index] * temp_ratio
                data[1][index] = data[1][index] * temp_ratio
        else:  # x < y
            if abs(data[1][index]) >= abs(data[2][index]):  # y > z y is biggest value
                temp_ratio = edge_length / (abs(data[1][index]) + .000001)
                data[1][index] = data[1][index] * temp_ratio
                data[0][index] = data[0][index] * temp_ratio
                data[2][index] = data[2][index] * temp_ratio
            else:  # z > y
                temp_ratio = edge_length / (abs(data[2][index]) + .000001)
                data[2][index] = data[2][index] * temp_ratio
                data[0][index] = data[0][index] * temp_ratio
                data[1][index] = data[1][index] * temp_ratio

'''generate sphere'''
sphere = Sphere(100, 10)
sphere.generate_data()

'''generate cubic'''
cubic = Cubic(20, 100, 2)
cubic.generate_data()

'''projection'''
edge_length = 20/2
data = [[],[],[]]
data = listcopy(sphere.sphere_data_display)
projection_origin(data, edge_length)

# set figuredl
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(sphere.sphere_data_display[0], sphere.sphere_data_display[1], sphere.sphere_data_display[2], 'k', label='parametric curve', linewidth=1)
ax.plot(cubic.cubic_data_display[0], cubic.cubic_data_display[1], cubic.cubic_data_display[2], 'g', label='parametric curve', linewidth=0.5)
ax.scatter(data[0], data[1], data[2], 'r', marker='o', s = 1, color = 'r')

'''
origin = [0], [0], [0]
plt.quiver(*origin, data[0], data[1], data[2], scale=1)
'''

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()