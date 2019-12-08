from Apfel_Class import Mandelbrot
import time

now = time.time()

apfel = Mandelbrot()
apfel.create_array()
print(time.time()-now)
apfel.show()

