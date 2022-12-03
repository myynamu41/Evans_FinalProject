'''
Name: Team Evans
email: nguye2m6@mail.uc.edu, laupi@mail.uc.edu, mainalda@mail.uc.edu, Burkhadj@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project is our final group project, demonstrates that we can use Eclipse to create a PyDev project
'''
from PIL import Image
from Function import *

building = decryptBuilding()
im = Image.open("Team_Evans.jpeg")
im.show() 