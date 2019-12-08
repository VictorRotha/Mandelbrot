import numpy as np
import matplotlib.pyplot as plt

class Mandelbrot:
    def __init__(self):
        self.limiter = 2
        self.max_iter = 100

        w, h = self.width, self.height = 600, 600
        centerx, centery = self.center = (-0.6, 0.5)
        self.step = 0.001
        self.xrange = (centerx - w//2*self.step, centerx + w//2*self.step)
        self.yrange = (centery - h//2*self.step, centery + h//2*self.step)

        self.screen_array = np.zeros((self.height, self.width))

    def create_array(self):
        xmin, xmax = self.xrange
        ymin, ymax = self.yrange
        step = self.step
        max_iter, limiter = self.max_iter, self.limiter
        for i in range(self.height):
            for j in range(self.width):
                c = complex(xmin + step * j, ymax - step * i)
                z = 0
                result = max_iter
                for n in range(max_iter):
                    if abs(z) < limiter:
                        z = z * z + c
                    else:
                        result = n
                        break
                self.screen_array[i, j] = result
                # n ist Anzahl der Iterationen, bis z > limiter.
                # Wenn z NICHT über limiter geht (= Mandelbrot Bedingung!!), dann ist n = max_iter

    def show(self):
        # title = f'Mandelbrotmenge\nx={self.xrange}, y={self.yrange}, limit={self.limiter}, iter={self.max_iter}\n' \
        #         f'size={self.width}*{self.height}'
        title = f'Mandelbrotmenge\ncenter={self.center}, px={self.step}\nlimit={self.limiter}, iter={self.max_iter}'
        plt.title(title)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(np.log(self.screen_array), cmap=plt.cm.hot_r)
        plt.show()
