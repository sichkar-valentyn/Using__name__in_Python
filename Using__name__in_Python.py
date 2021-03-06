# File: Using__name__in_Python.py
# Description: Example how and why to use __ name __ in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Example how and why to use __ name __ in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Using__name__in_Python (date of access: XX.XX.XXXX)
        
        
def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)


# Here we check if __name__ is a __main__ so we run the code
# But if we import this code, then the __name__ is not __main__ and we just import function
if __name__ == '__main__':
    print(__name__)
    print(fib(31))
