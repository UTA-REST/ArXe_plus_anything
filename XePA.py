from tables import *
import os

def getXePA():
    APA = open_file(os.path.join(os.path.dirname(os.path.realpath(__file__)),"Xenon_Plus_Anything.h5"))
    return APA