#import os
from setuptools import setup, Extension

#os.environ["CC"] = "g++"
#os.environ["CFLAGS"] = "-std=c++17"

setup(name='fastglob', version='1.0',
      ext_modules=[
        Extension('fastglob', ['fastglob.cpp'],
            )])
