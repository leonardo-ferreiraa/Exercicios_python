palavras = ("boca", "calça", "escuro", "passageiro", "respeito","calopsita","esquecimento", "linguagem")
for p in palavras:
    print(f"\nA palavra {p} temos:", end=" ")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=" ")
