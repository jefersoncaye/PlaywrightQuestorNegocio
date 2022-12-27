import os
lista = []
pasta = 'test-results/'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        imagem = (os.path.join(diretorio, arquivo))
        lista.append(imagem)


print(lista)