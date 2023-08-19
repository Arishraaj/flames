#flames

while True:
    t=input("Do u want to play (yes/no) : ").lower()
    if t=="yes":
        boyname=input("Enter the Boy name : ").lower()
        girlname=input("Enter the Gurl name : ").lower()
        for x in boyname:
            if x in girlname:
                boyname=boyname.replace(x,"")
                girlname=girlname.replace(x,"")
        name=boyname+girlname
        l=len(name)
        r=l%6
        if r==0:
            print("Friends")
        elif r==1:
            print("Love 💘")
        elif r==2:
            print("Affection 🤍")
        elif r==3:
            print("Marriage 💍")
        elif r==4:
            print("Enemy 💔")
        elif r==5:
            print("Sister ")
    elif t=="no":
        print("Thank you")
 #       quit()
        break
    else:
        print("Invalid..Try again")
