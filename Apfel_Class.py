import numpy as np
import matplotlib.pyplot as plt
import os

class Mandelbrot:
    def __init__(self, limiter=2, max_iter=100, screen_size=(600,600), center=(-0.5+0.5j), step=0.001):
        self.limiter = limiter
        self.max_iter = max_iter
        w, h = self.width, self.height = screen_size
        c = self.center = center
        self.step = step

        self.xrange = (c.real - w//2*self.step, c.real + w//2*self.step)
        self.yrange = (c.imag - h//2*self.step, c.imag + h//2*self.step)

        self.screen_array = np.zeros((self.height, self.width))

    def print_parameters(self):
        print(f'Aufloesung: {self.width}*{self.height} Pixel')
        print(f'Zentrum: {self.center}\nPixelbreite: {self.step}')
        print(f'xrange: {self.xrange}, yrange: {self.yrange}')
        print(f'Limiter: {self.limiter}\nMax. Iterationstiefe: {self.max_iter}')

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

    def show(self, colormap=plt.cm.hot_r):
        # title = f'Mandelbrotmenge\nx={self.xrange}, y={self.yrange}, limit={self.limiter}, iter={self.max_iter}\n' \
        #         f'size={self.width}*{self.height}'
        title = f'Mandelbrotmenge\ncenter={self.center}, px={self.step}\nlimit={self.limiter}, iter={self.max_iter}\n' \
                f'Colormap={colormap}'
        plt.title(title)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(np.log(self.screen_array), cmap=colormap)
        plt.show()

    def save(self, filename, info=False):
        # TODO check filename/path exits
        filename = os.path.join(os.getcwd(), '_img', filename)
        plt.imsave(filename, np.log(self.screen_array), cmap=plt.cm.hot_r)
        print(f'img saved:\n{filename}')
        if info:
            infofile = os.path.splitext(filename)[0] + '.txt'
            with open(infofile, 'w') as f:
                f.write(f'Aufloesung: {self.width}*{self.height} Pixel\n\n')
                f.write(f'Zentrum: {self.center}\nPixelbreite: {self.step}\n')
                f.write(f'xrange: {self.xrange}, yrange: {self.yrange}\n\n')
                f.write(f'Limiter: {self.limiter}\nMax. Iterationstiefe: {self.max_iter}')

            print(infofile)


