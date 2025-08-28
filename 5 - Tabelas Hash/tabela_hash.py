# Em Python, a Tabela Hash é implementada nativamente através do tipo de dado "dicionário" (dict).

# Exemplo 1: Usando uma tabela hash para uma lista de preços
livro_de_precos = {}
livro_de_precos["maçã"] = 0.67
livro_de_precos["leite"] = 1.49
livro_de_precos["abacate"] = 1.49

print("Exemplo de Lista de Preços:")
print(livro_de_precos)
print(f"O preço do abacate é: {livro_de_precos['abacate']}")
print("-" * 20)

# Exemplo 2: Usando uma tabela hash como cache para evitar trabalho duplicado
votaram = {}


def verifica_eleitor(nome):
    """Verifica se uma pessoa já votou. Se não, registra o voto."""
    if votaram.get(nome):
        print(f"Mande embora! {nome} já votou.")
    else:
        votaram[nome] = True
        print(f"Deixe {nome} votar!")


print("Exemplo de Cache de Votos:")
verifica_eleitor("tom")
verifica_eleitor("mike")
verifica_eleitor("tom")  # Tentando votar novamente
