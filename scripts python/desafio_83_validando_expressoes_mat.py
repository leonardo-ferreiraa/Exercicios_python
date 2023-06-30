expressao = str(input("Digite uma expressão: "))
# lista
pilha = []
# vai pegar cada um dos Simbolos da variável expressão
for simbolo in expressao:
    if simbolo == '(':
        # insere o parênteses '(' na lista
        pilha.append('(')
    elif simbolo == ')':
        # se o tamanho da pilha foi maior do que 0
        if len(pilha) > 0:
            # remove o último elemento da lista
            pilha.pop()
        else:
            # isso vai servir para fazer com que tenha a mesma quantidade de parênteses '(' ')'
            pilha.append(')')
            break
if len(pilha) == 0:
    print("A expressão está correta!")
else:
    print("A expressão está incorreta!")