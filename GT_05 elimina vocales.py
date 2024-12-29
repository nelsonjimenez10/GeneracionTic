#ingresa una palabra y retornarla sin vocales definiendo una funcion

def main():
    lapal=input("Ingrese la palabra: ")
    sinvoc=quitav(lapal)
    print("La palabra abreviada es: " + "".join(sinvoc))

def quitav(pal):
    pal=pal.lower()
    sal=[]
    for i in range(len(pal)) :
        if pal[i] not in ["a","e","i","o","u"," "]:
            sal.append(pal[i])
    return sal

if __name__ == "__main__":
    main()
    

