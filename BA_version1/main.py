import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cubic_sphere import Sphere, Cubic, listcopy, projection_origin, projection_test_fun

'''generate the test image of longtitude and latitude for reverse
   projection 
'''
class testCircleImage:
    image_data = [[], [], []]
    def __init__(self, edgesize, samplesize, divide_input):
        self.edge = edgesize
        self.sample_size = samplesize
        self.divide = divide_input

    def generate_data(self):
        phi = np.arange(0.0, np.pi * (1 + 1 / self.divide), np.pi / self.divide)
        rho = np.arange(-self.edge/2, self.edge/2 + self.edge/self.sample_size, self.edge/self.sample_size)
        '''first facet z = -10'''
        for phi_index in phi:
            for rho_index in rho:
                self.image_data[0].append(rho_index*np.cos(phi_index))
                self.image_data[1].append(rho_index*np.sin(phi_index))
                self.image_data[2].append(-self.edge/2)

        '''second facet z = 10'''
        for phi_index in phi:
            for rho_index in rho:
                self.image_data[0].append(rho_index*np.cos(phi_index))
                self.image_data[1].append(rho_index*np.sin(phi_index))
                self.image_data[2].append(self.edge/2)



class testLineImage:
    image_data = [[], [], []]
    '''constructor: testimage edge size, in total 6 facets'''
    def __init__(self, edgesize, samplesize, divide_input):
        self.edge = edgesize
        self.sample_size = samplesize
        self.divide = divide_input

    '''test for the first side'''
    def generate_data(self):
        step = np.arange(-self.edge/2, self.edge/2 + self.edge/self.divide, self.edge/self.divide)
        step_sample = np.arange(-self.edge/2, self.edge/2 + self.edge/self.sample_size, self.edge/self.sample_size)
        '''first facet x = -10'''
        for step_index in step:
            for sample_index in step_sample:
                self.image_data[0].append(-self.edge/2)
                self.image_data[2].append(step_index)
                self.image_data[1].append(sample_index)

        '''second facet x = 10'''
        for step_index in step:
            for sample_index in step_sample:
                self.image_data[0].append(self.edge/2)
                self.image_data[1].append(sample_index)
                self.image_data[2].append(step_index)

        '''third facet y = -10'''
        for step_index in step:
            for sample_index in step_sample:
                self.image_data[0].append(sample_index)
                self.image_data[1].append(-self.edge/2)
                self.image_data[2].append(step_index)

        '''fourth facet y = 10'''
        for step_index in step:
            for sample_index in step_sample:
                self.image_data[0].append(step_index)
                self.image_data[1].append(self.edge/2)
                self.image_data[2].append(sample_index)

def reverse_projection(inputdata, edgesize):
    output_data = listcopy(inputdata)
    print("the size of list " + str(0.25*len(output_data[0])))
    for index in range(len(output_data[0])):
        '''distance from the point to origin'''
        length = np.sqrt(np.power(output_data[0][index],2) + np.power(output_data[1][index], 2) + np.power(output_data[2][index],2))
        factor = length/(edgesize)
        output_data[0][index] = output_data[0][index]/factor
        output_data[1][index] = output_data[1][index]/factor
        output_data[2][index] = output_data[2][index]/factor
    return output_data


def main():
    # generate sphere
    sphere = Sphere(100, 10, 10)
    sphere.generate_data()

    ##generate cubic
    cubic = Cubic(20, 100, 2)
    cubic.generate_data()

    ##testImage
    testData = testLineImage(20, 4, 40) #edge, sample, samplesize
    testData.generate_data()

    ##testCircleImage
    testCircleData = testCircleImage(20, 8, 40)
    testCircleData.generate_data()
    reverTestDataCircle = reverse_projection(testCircleData.image_data, 10)


    #reverse projection
    reverTestData=reverse_projection(testData.image_data, 10)

    # set figured
    fig = plt.figure(figsize=(12, 15))
    ax = fig.add_subplot(221, projection='3d')
    ax.plot(sphere.sphere_data_display[0], sphere.sphere_data_display[1], sphere.sphere_data_display[2], 'k',
            label='parametric curve', linewidth=1)
    ax.plot(cubic.cubic_data_display[0], cubic.cubic_data_display[1], cubic.cubic_data_display[2], 'g',
            label='parametric curve', linewidth=0.5)
    ax.scatter(testData.image_data[0], testData.image_data[1], testData.image_data[2], 'r', marker='o', s=1, color='r')

    ax2 = fig.add_subplot(222, projection="3d")
    ax2.plot(sphere.sphere_data_display[0], sphere.sphere_data_display[1], sphere.sphere_data_display[2], 'k',
            label='parametric curve', linewidth=0.5)
    ax2.scatter(reverTestData[0], reverTestData[1], reverTestData[2], 'r', marker='o', s=1, color='r')

    ax3 = fig.add_subplot(223, projection="3d")
    ax3.plot(sphere.sphere_data_display[0], sphere.sphere_data_display[1], sphere.sphere_data_display[2], 'k',
            label='parametric curve', linewidth=1)
    ax3.plot(cubic.cubic_data_display[0], cubic.cubic_data_display[1], cubic.cubic_data_display[2], 'g',
            label='parametric curve', linewidth=0.5)
    ax3.scatter(testCircleData.image_data[0], testCircleData.image_data[1], testCircleData.image_data[2], 'r', marker='o', s=1, color='r')


    ax4 = fig.add_subplot(224, projection="3d")
    ax4.plot(sphere.sphere_data_display[0], sphere.sphere_data_display[1], sphere.sphere_data_display[2], 'k',
            label='parametric curve', linewidth=0.5)
    ax4.scatter(reverTestDataCircle[0], reverTestDataCircle[1], reverTestDataCircle[2], 'r', marker='o', s=1, color='r')


    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.show()


if __name__ == "__main__":
    main()

