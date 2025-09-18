def criar_indice_invertido(documentos):
    indice = {}
    for doc_id, texto in documentos.items():
        for palavra in texto.lower().split():
            if palavra not in indice:
                indice[palavra] = set()
            indice[palavra].add(doc_id)
    return indice


if __name__ == "__main__":
    docs = {
        1: "O rato roeu a roupa do rei de Roma",
        2: "A raposa veloz pula sobre o cachorro preguiçoso",
        3: "O rei ordenou a roupa nova"
    }
    indice = criar_indice_invertido(docs)
    for palavra, doc_ids in indice.items():
        print(f"{palavra}: {doc_ids}")
