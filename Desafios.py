nome = str(input("escreva um nome: "))
nomeMauis = nome.upper()
nommeMinu = nome.lower()
nomeSE = nome.replace(" ", "")
splitNome = nome.split()
len(nome)
print(f'{nome}, com letras maiusculas: {nomeMauis}, e com letras minusculas: {nommeMinu}, e o nome sem espaços é:  {nomeSE}, primeiro nome : {splitNome[0]}')

nomecity = str(input("digite o nome de uma cidade: "))
nomeCity1 = nomecity.lower()
sobCity = "santo"
splitCity = nomeCity1.split()
verificacaoCity = sobCity in splitCity[0] 
print(f'essa cidade começa com Santo? {verificacaoCity}')

nome1 = str(input('digite um nome: '))
nome2 = nome1.lower()
sobreNome = 'silva'
verificacaoNome = sobreNome in nome2 
print(f'esse nome tem silva? {verificacaoNome}')

teclado = str(input('digite uma palavra: '))
letra = "a"
teclado1 = teclado.lower()
qtdLetrasa = teclado1.count(letra)
posicaoPalavra = teclado1.find(letra)
posicaoPalavra2 = teclado1.rfind(letra)
print(f'A quantidade de letra A é: {qtdLetrasa} e {letra} posição é: {posicaoPalavra+1}, e a posição da ultima {letra} é: {posicaoPalavra2+1} ')

nomeComp = str(input("digite nome completo "))
lNome = nomeComp.split()
print(f'O primeiro nome é: {lNome[0]}')
print(f'O ultimo nome é: {lNome[-1]}')