#numeros primos
#problema: establecer que numerosprimos hay en un rangodefinido porel usuario
# y al finalizar publicar una lista con los resultados

#1-establecer rango
rinicial=int(input(f"Ingrese rango inicial: "))
rfinal=int(input(f"Ingrese rango final: "))
losprimos=[]
for i in range(rinicial,rfinal+1) :
    esprimo= True
    for j in range(2,i) :
        if i%j == 0 :
            esprimo= False        
    if esprimo == True and i != 1:
        losprimos.append(i)
        j=2

print(f"Liata de numeros primos en el rango de {rinicial} a {rfinal} : \n{losprimos}")
