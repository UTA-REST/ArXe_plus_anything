from tables import *
import os 

def getAPA():
    print(os.path.join(os.path.dirname(os.path.realpath(__file__)),"Argon_Plus_Anything.h5"))
    APA = open_file(os.path.join(os.path.dirname(os.path.realpath(__file__)),"Argon_Plus_Anything.h5"))
    return APA