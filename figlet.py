import sys
from pyfiglet import Figlet
import random
figlet = Figlet()
font_fig = figlet.getFonts()
if len(sys.argv)==2:
    sys.exit("Invalid usage")

elif len(sys.argv)==3:
    if sys.argv[1]=="-f" or sys.argv[1]=="--font":
        if sys.argv[2] in font_fig:
            s = input("Input: ")
            new_font = Figlet(font=sys.argv[2])
            print(new_font.renderText(s))
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

elif len(sys.argv)==1:
    s = input("Input: ")
    f = Figlet(font=random.choice(font_fig))
    print(f.renderText(s))
