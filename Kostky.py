def hod():
    import random as rd
    pocet = 1
    
    while True:
        kostka = rd.randrange(1,7,1)
        
        if kostka != 6:
            pocet += 1
            print(kostka,end = " ")
                        
            
        else:
            print(kostka,end = " ")
            print(" -- ", end = "")
            print(f"Pocet hodu: {pocet}")
            return pocet

def vitez(a,b,c,d):
    
    

def hra():
    
    hrac1 = hod()
    hrac2 = hod() 
    hrac3 = hod() 
    hrac4 = hod() 

hra()