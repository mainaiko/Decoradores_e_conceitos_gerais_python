"""
Vamos aprender sobre iteradores e geradores em python. Esses sao conceitos poderosos que nos permitem trabalhar
com sequencias de maneira eficiente.
"""
"""
Em python, um iterador é um objeto que contem um numero contavel de valores que podem ser iterados, o que significa que voce pode 
percorrer todos os valores. O protocolo do iterador é uma maneira do python fazer a iteraçao de um objeto, que consiste em dois metodos especiais
"__iter__()" e "__next__()"

Exemplo de uso:

- Economizar memoria evitando carregar todas as linhas do arquivo
- Iterar linha a linha do arquivo
"""
#class Fileiterator:
#    def __init__(self, filename):
#      self.file = open(filename)
#
#    def __iter__(self):
#      return self
#    
#    def __next__(self):
#       line = self.file.readline()
#       if line != "":
#          return line
#       else:
#          self.file.close()
#          raise StopIteration
#       
#for line in Fileiterator("large_file.txt"):
#   print (line)

#_________________________________________________

class Meuiterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0
        

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return  numero * 2
        except IndexError:
            raise StopIteration



for i in Meuiterador(numeros= [25,58,45,52,47,85]):
    print (i)
