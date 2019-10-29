#Threading practice in python

import threading


def print_square(num):
    print('Square: {}'.format(num*num))

def print_cube(num):
    print('Cube: {}'.format(num* num * num))

def main():

    #Creating the first thread
    th1 = threading.Thread(target = print_square,args=(10,))
    
    #Creating the second thread
    th2 = threading.Thread(target = print_cube,args=(10,))

    th1.start()

    th2.start()

    th1.join()

    th2.join()

    print('Done')

if __name__ == '__main__':
    main()