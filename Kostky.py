def hod(hrac):
    import random as rd
    pocet = 1
    
    while True:
        kostka = rd.randrange(1,7,1)
        
        if kostka != 6:
def hod(hrac):
    import random as rd
    pocet = 1
    
    while True:
        kostka = rd.randrange(1,7,1)
        
        if kostka != 6:
            pocet += 1
            print(kostka,end = " ")
                        
            
        else:
            print(kostka,end = " ")
            print("", end = "\n")
                        
            return pocet

def vitez(a,b,c,d):

    hraci = [a,b,c,d]
    
    
    vitez = max(hraci)
    print(f"Vitezem je {vitez}")
    
    

def hra():
    for hrac in range(1,5):
        
        pocet = hod(hrac)
        print(f"Hráč {hrac} získal: {pocet}")
    
    

hra()
