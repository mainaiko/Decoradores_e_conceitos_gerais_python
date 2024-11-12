"""
Recapitulando
Funçoes em python sao objetos de primeira classe. Isso significa que as funçoes podem ser passadas
e usadas como argumentos.
"""
def dizer_oi(nome):
    return f"Ola {nome}"

def incentivar_aprender(nome):
    return f"Vamos aprender python juntas {nome}"

def mensagem(funcao, main_name):
    return funcao(main_name)

print (mensagem(dizer_oi, "aiko"))
print (mensagem(incentivar_aprender, "aiko"))

"""
Inner functions
É possivel definir funçoes dentro de outras funçoes. Tais funçoes sao chamadas de funçoes internas
"""
def pai():
    print ("escrevendo da pai() função")

    def filho1():
        print ("escrevendo da filho1() função")

    def filho2():
        print ("escrevendo da filho2() função")

    filho1()
    filho2()

pai()

"""
Retornando funçoes de funçoes
Python tambem permite que voce use funçoes como valores de retorno
"""

def caucular(operacao):
    def somar(a, b):
        return a+b
    def subtrair(a, b):
        return a-b
    def multi(a, b):
        return a*b
    def div(a, b):
        return a/b
    
    match operacao: #estrutura parecida com o Swith case de outras linguagens
        case "+":
            return somar
        case "-":
            return subtrair
        case "*":
            return multi
        case "/":
            return div
        
    
print (caucular("+")(1,14))


"""
Decoradores simples
Agora que entendemos que funçoes sao como qualquer outro objeto em python, podemos seguir em frente
e ver a magica que é o decorador python
"""

def meu_decorador(funcao):#passando a funçao ola mundo de parametro para o decorador
    def envelope():
        print ("faz algo antes")
        funcao()
        print ("faz algo depois")

    return envelope

def ola_mundo():
    print ("Ola mundo")

ola_mundo = meu_decorador(ola_mundo)

ola_mundo()


print ("_________________________________________")
"""
Açucar sintatico
O pyhton permite que voce use decoradores de maneira mais simples com o simbolo @
"""
def meu_decorador(funcao):
    def envelope():
        print ("faz algo antes")
        funcao()
        print ("faz algo depois")

    return envelope# Posso retornar quantas funçoes eu quiser

@meu_decorador
def ola_mundo():
    print ("Ola mundo")

ola_mundo()

