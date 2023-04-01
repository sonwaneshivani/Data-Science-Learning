import os, sys
from os.path import abspath , join, dirname
sys.path.insert(0,abspath(join(dirname(__file__), '..')))

from course import  course_details_12

def payment():
    print("This is my payment file")

course_details_12.course()


# So,now we have python file inside coursr folder,again inside payment folder we have python file, we are trying to call This payment details from course details file and viceversa
# It means from one module we have to import another module and viceversa
''' Packages are nothing but folder or a directory. Ex: course and payment folder
in these we can create n number of dffrnt files or folders.
Module : Here python file is called as module. Ex: course_details.py and payment_details.py '''
#Whenever we are going to write down the project we are not going to write down the complete code.We end up creating multiple files and folders. So we have to understand how to import from one module to another module
