import os,sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

''' from payment import payment_details_12 '''
#This means all the methods inside that will be available here

def course():
    print("This is my course file")

#To access those methods
''' payment_details_12.payment() '''

#Still we are getting not found error bcoz it is an untracked file(folder inside a folder inside a folder) at the tym of execution it is unable to locate but normally while accessing it does
#How to solve this error : By collapsing all the files/by creating cache 
#They are import os,sys and from line & atlast sys.path.ins

#It creates a pycache'''