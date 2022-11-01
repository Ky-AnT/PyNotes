import template.temp
import os
def openApp(name):
    print(f'Opening data from {os.getcwd()}/data/subject_data/{name}.txt')
    file = open("data/subject_data/"+name+".txt",'r')
    readLines = file.readlines()
    readableString = ''
    for i in range(len(readLines)): readableString += readLines[i]
    #print(readableString)
    template.temp.initialize(name.upper(),readableString)
    file.close()
subjects = ['english','hass','maths','science']
askApp = input('What app would you like to open: ')
while askApp not in subjects:
    print('Invalid Option')
    print(subjects)
    askApp = input('What app would you like to open: ')
openApp(askApp)

