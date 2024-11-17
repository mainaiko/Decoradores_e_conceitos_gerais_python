"""
Funçao de decoraçao com argumentos
Podemos usar *args e **kwargs na funçao interna, com isso ela aceitara um numero arbitrario de argumentos
posicionais e de palavras chave
"""
def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)

    return envelope

@duplicar
def aprender(tecnologia, plataforma):
    print (f"Estou aprendendo {tecnologia} na {plataforma}")

aprender("python", "DIO")

"""
Retornando valores de funçoe decoradas
O decorador pode decidir se retorna o valor da funçao decorada ou nao. Para que 
o valor seja retornado a funçao de envelope deve retornar o valor da funçao decorada
"""
def duplicar(func):
    def envelope(*args, **kwargs):
        return func(*args, **kwargs)

    return envelope

@duplicar
def aprender(tecnologia):
    print (f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

tecnologia = aprender("Java")

print (tecnologia)

"""
Introspecçao
É a capacidade de um objeto saber sobre seus proprios atributos em tempo de execução
"""

print (aprender.__name__)
import functools

def duplicar(func):
    @functools.wraps(func)
    def envelope(*args, **kwargs):
        return func(*args, **kwargs)

    return envelope

@duplicar
def aprender(tecnologia):
    print (f"Estou aprendendo {tecnologia}")
    return tecnologia.upper()

print (aprender.__name__)