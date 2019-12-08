from Apfel_Class import Mandelbrot
import time

now = time.time()

apfel = Mandelbrot(screen_size=(600,600),
                   center = complex(-0.6,0.5),
                   step=0.0005)
apfel.print_parameters()
apfel.create_array()
print(time.time()-now)
apfel.show()
# apfel.save('mandel01.png', info=True)
while True:
    value = input('q=quit, 1=save, 2=show: ')
    if value.lower() == 'q':
        break
    elif value=='2':
        apfel.show()
    elif value=='1':
        filename = input('filename: ')
        apfel.save(filename, info=True)
        break


