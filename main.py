import lotteri
import os


lotteriet = lotteri.Lotteri()

looping = True

while looping:

    os.system("cls" if os.name == "nt" else "clear")
    antal_lotter = input("\n\t\t hur Många Lotter Vill Du Ha? Max 3st!")


    try:
        int_antal_lotter = int(antal_lotter)
        i = 0

        if(int_antal_lotter < 4):
            os.system("cls" if os.name == "nt" else "clear")
            print("\n\t\t STORT GRATTIS! DU VANN:")

            while i < int_antal_lotter:
                vinst = lotteriet.get_vinst()
                print("\n\t\t" + vinst)
                i+=1

        elif(int_antal_lotter > 3):
            print("\n\t\t Du Har Valt Förmånga Lotter!")


    except ValueError:
        print("\n\t\t Error")



    print("----------------------------------------------")
    spela_igen = input("\n\t\tVill Du Spela Igen? J/N ")
    if(spela_igen == "n"):
        break