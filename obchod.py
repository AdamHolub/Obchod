
print("Vítejte v obchodu")

loop=True
celkovaCena=0
list = [["Rohlik", 0, 3], ["Houska", 0, 4], ["Bageta", 0, 10],
        ["Paprika", 0, 20], ["Okurka", 0, 25], ["Brokolice", 0, 30],
        ["Hovězí", 0, 75], ["Skopové", 0, 90], ["Vepřové", 0, 85]]

while loop:
    
    print("1. pečivo")
    print("2. zelenina")
    print("3. maso")
    print("4. odcházíte k pokladně")
    vyber = int(input())
    
    if(vyber==1):
        while True:
            print("1. rohlík")
            print("2. houska")
            print("3. bageta")
            print("4. Zpět ")
            vyberPecivo = int(input())
        
            if(vyberPecivo==1):
                pocetRohlik = int(input("Kolik chcete rohlíků?\n"))
                list[0][1]+=pocetRohlik
            elif(vyberPecivo==2):
                pocetHouska = int(input("Kolik chcete housek?\n"))   
                list[1][1]+=pocetHouska
            elif(vyberPecivo==3):
                pocetBageta = int(input("Kolik chcete baget?\n"))
                list[2][1]+=pocetBageta
            elif(vyberPecivo==4):
                print("Vracíte se na výběr kategorii")
                print("")
                break
            else:
                print("Error")
                        
    elif(vyber==2):
        while True:
            print("1. paprika")
            print("2. okurka")
            print("3. brokolice")
            print("4. Zpět")
            vyberZelenina = int(input())
        
            if(vyberZelenina==1):
                pocetPaprika = int(input("Kolik chcete paprik?\n"))
                list[3][1]+=pocetPaprika
            elif(vyberZelenina==2):
                pocetOkurka = int(input("Kolik chcete okurek?\n"))
                list[4][1]+=pocetOkurka
            elif(vyberZelenina==3):
                pocetBrokolice = int(input("Kolik chcete brokolice?\n")) 
                list[5][1]+=pocetBrokolice
            elif(vyberZelenina==4):
                print("vracíte se na výběr kategorii")
                print("")
                break
            else:
                print("Error")
            
    elif(vyber==3):
        while True:
            print("1. hovezí")
            print("2. skopové")
            print("3. vepřové")
            print("4. Zpět")
            vyberMaso = int(input())
            if(vyberMaso==1):
                pocetHovezi = int(input("Kolik chcete kg hovězího?\n"))
                list[6][1]+=pocetHovezi
            elif(vyberMaso==2):
                pocetSkopove = int(input("Kolik chcete kg skopového?\n"))
                list[7][1]+=pocetSkopove
            elif(vyberMaso==3):
                pocetVeprove = int(input("Kolik chcete kg vepřového?\n"))
                list[8][1]+=pocetVeprove
            elif(vyberMaso==4):
                print("vracíte se na výběr kategorii")
                print("")
                break
            else:
                print("Error")
            
    elif(vyber==4):        
        loop=False
        print("")
    else:
        print("Error")
        
for z in list:
    if not z[1]==0:
        print(f"{z[0]} {z[1]}x = {z[1]*z[2]} Kč")
        
for x in list:
    if not x[1]==0:
        vyslednaCena=x[1]*x[2]
        celkovaCena+=vyslednaCena
        
print("")
print(f"Celková cena je: {celkovaCena} Kč")
print("")
print("Děkujeme za nákup\n")
        
