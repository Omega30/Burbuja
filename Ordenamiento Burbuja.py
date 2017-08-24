lista = [15,78,22,44,12,95,35,1,66,0,50];

for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j+1] < lista[j]):
                aux=lista[j];
                lista[j]=lista[j+1];
                lista[j+1]=aux;     
print(lista);