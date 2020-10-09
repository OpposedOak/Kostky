import random as rd

def hod(hrac):
    
    pocet = 1
    
    while True:
        kostka = rd.randrange(1,7)
        
        if kostka != 6:
            pocet += 1
            print(kostka,end = " ")
                        
        else:
            print(kostka,end = " ")
            print("", end = "\n")
            return pocet

def hra():
    
    body = 0
    
    for hrac in range(1,5):

        pocet = hod(hrac)
        print(f"Hráč {hrac} získal: {pocet}")
        
        if pocet > body:
        
            vitez = hrac
            body = pocet
            
    print(f"Vítězem je hráč: {vitez}")

hra()
