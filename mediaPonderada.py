def calcular_media_ponderada(nota1, peso1, nota2, peso2):

    media = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)
    return media
    
    
nota1 = float(input('Digite a Primeira Nota:'))
peso1 = int(input('Digite o peso da primeira nota:'))
nota2 = float(input('Digite a Segunda nota:'))
peso2 = int(input('Digite o peso da segunda nota:'))

media = calcular_media_ponderada(nota1, peso1, nota2, peso2)
print(f'A media ponderada e: {media:.2f}')
