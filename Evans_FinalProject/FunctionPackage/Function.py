'''
Name: Team Evans
email: nguye2m6@mail.uc.edu, laupi@mail.uc.edu, mainalda@mail.uc.edu, Burkhadj@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project is our final group project, demonstrates that we can use Eclipse to create a PyDev project
'''
import json
from PIL import Image
def decryptBuilding():
    englishFile = open('english.txt','r').readlines()
    
    jsonFile = open('EncryptedGroupHints.json')
    
    jsonDict = json.load(jsonFile)
    
    hints = jsonDict['Evans']
    
    print(hints)
    
    print(englishFile[7479])
    
    for x in hints:
        print(englishFile[int(x)])
    
from PIL import Image

def load_image(filename):
    myimage = Image.open(filename)
    myimage.load()
    return myimage
   