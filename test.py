# Author          : John Kenneth S. Lesaba
# Course and Year : 2-BSCS
# Filename        : test.py
# Description     : test.py is the python program that you run. It uses the Emmet class from emmet.py to translate emmet abbreviations into real html code/s.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.
from emmet import Emmet                     #imports Emmet class from emmet.py
w = input()                                 #catches user input in stdin and assigns it to variable w
while w != "quit" and w != "exit":          #repeat succeeding codes until user inputs quit or exit
    ans = Emmet(w)                          #variable ans of type string catches the return value of class Emmet when passed with the value of w as parameter
    print(ans)                              #prints variable ans
    w = input()                             #catches user input in stdin and assigns it to variable w (for succeeding inputs)