import os


f = ("""
""")

while True:



    x = input("vad vill du göra \n").lower()

    if x == "lägga till":
        y = input("vad ska koordinaten heta \n")
        z = input("vilka koordinater är det \n")
        w = open(y + ".config", "a")
        w.write(y + " = " + z + f)
        w.close()
        
        
    elif x == "visa":
        r = input("Vilken koordinat vill du visa \n")
        w = open(r +".config")
        print("\n" + w.read())
        w.close()
    


    elif x == "ta bort":
        h = input("Vilken koordinat vill du ta bort \n")
        if os.path.exists(h + ".config"):
            os.remove(h + ".config")
        else:
            print("filen finns inte")