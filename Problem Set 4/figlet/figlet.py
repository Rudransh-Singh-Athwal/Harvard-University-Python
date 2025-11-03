import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    f = random.choice(fonts)
    figlet.setFont(font = f)
    
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = sys.argv[2]
        if f in fonts:
            figlet.setFont(font = f)
        else:
            print("Invalid usage")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1) 
        
else:
    print("Invalid usage")
    sys.exit(1)
        
x = input("Input: ")
y = figlet.renderText(x)
print(y)