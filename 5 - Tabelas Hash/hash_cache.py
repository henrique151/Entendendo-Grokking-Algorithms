cache = {}


def paga_dados_do_servidor(url):
    return f"Dados obtidos de {url}"


def pega_pagina(url):
    if cache.get(url):
        print("Usando cache...")
        return cache[url]
    else:
        print("Buscando dados do servidor...")
        dados = paga_dados_do_servidor(url)
        cache[url] = dados
        return dados


print(pega_pagina("https://exemplo2.com"))
print(pega_pagina("https://exemplo.com"))
print(pega_pagina("https://exemplo.com"))
print(pega_pagina("https://exemplo2.com"))
