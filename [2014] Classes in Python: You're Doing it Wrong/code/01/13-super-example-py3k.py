class ListaLogger(list):
    def append(self, x):
        print("Esto también añade", x)
        super().append(x)

numeros = ListaLogger([4, 5])
numeros.append(-1)
print(numeros)
