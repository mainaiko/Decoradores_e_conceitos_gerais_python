"""
O que sao geradores?
Sao tipos especiais de iteradores, ao contrario das listas ou outros iteraveis, nao armazenam todos os seus valores
na memoria.
Sao definidos usando funçoes regulares, mas, ao inves de retornar valores usando "return" utilizam "yield"
"""
"""
Caracteristicas:

- Uma vez que um item gerado é consumido, ele é esquecido e nao pode ser acessado novamente

- O estado interno de um gerador é mantido entre chamadas

- A execussao de um gerador é pausada na declaraçao "yield" e retomada dai na proxima vez que ele for chamado
"""
#Exemplo de uso

#import requests
#
#def fetch_products(api_url, max_pages = 100):
#    page = 1
#    while page != max_pages:
#        response = requests.get(f"{api_url}?page={page}")
#        data = response.json()
#        
#        for product in data["products":]:
#            yield product
#        
#        if "next_page" not in data:
#            break
#        page +=1
#
#for product in fetch_products("https"):
#    print (product["name"])

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2




for i in meu_gerador(numeros= [1,2,3]):
    print (i)