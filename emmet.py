# Author          : John Kenneth S. Lesaba
# Course and Year : 2-BSCS
# Filename        : emmet.py
# Description     : Contains a class that can turn simple Emmet abbreviations into an actual HTML code
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
class Emmet:                                                                        #Emmet class declaration
    def __init__(self, raw):                                                        #class initialization definition
        self.raw = raw.split("+")                                                   #give self.raw the value of raw splitted by "+"

    def __str__(self):                                                              #THis is for string override
        ans = ""                                                                    #initialized the value of variable ans
        acceptableValues = ["div","nav","p","span"]                                 #a list that contains the acceptable html tags
        for i in range(len(self.raw)):
            append = self.raw[i].split(">")                                         #splits each item in list self.raw using ">" as splitter and returns it to a variable append as a list
            for x in range(len(append)):                                            #loop to go through each element of list append
                if any(y in append[x] for y in acceptableValues) == False:          #checks whether value of item in list append against the list of acceptable values
                    return "Error: Unrecognized abbreviation\n"                     #if the value of an element in list append is not accepted, ends the class by returning an error message
                indentCounter = x                                                   #assigns the value of x to indentCounter variable
                while indentCounter > 0:                                            #loops until indentCounter reaches zero
                    ans = ans + "    "                                              #adds indention every instance of while loop
                    indentCounter = indentCounter - 1                               #decrements indentCounter by 1 to avoid infinite loop
                ans = ans + "<{}>\n".format(append[x])                              #outputs opening html tag
            while x >= 0:                                                           #loop for indention of ending html tag
                indentCounter = x                                                   #assigns the value of x to indentCounter variable
                while indentCounter > 0:                                            #loops until indentCounter reaches zero
                    ans = ans + "    "                                              #adds indention every instance of while loop
                    indentCounter = indentCounter - 1                               #decrements indentCounter by 1 to avoid infinite loop
                ans = ans + "</{}>\n".format(append[x])                             #outputs ending html tag
                x = x - 1                                                           #decrement x by 1
        return ans                                                                  #this returns ans after post processing of class Emmet
