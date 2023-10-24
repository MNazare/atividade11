# Exercício Python 11: Desenvolva um programa que pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
# viagens de até 200Km e R$0,45 parta viagens mais longas.

import time
print("bom dia! seja bem vindo ao CALCULADOR DE PASSAGEM 3000 \nem instantes iremos calcular sua passagem, para isso responda as nossas perguntas.")
time.sleep(1)
distancia = float(input("qual é a distância em km da sua viagem? "))
cobrar1 = 0.50
cobrar2 = 0.45
if distancia < 200:
    preco = distancia * cobrar1
else:
    preco = distancia * cobrar2
time.sleep(1)
print("aguarde um pouco...")
time.sleep(1)
print("aguarde um pouco...")
time.sleep(1)
print("aguarde um pouco...")
time.sleep(1)
print("o preço da sua passagem esta saindo por APENAS ", preco,"REAIS!!! \nEU DISSE POR APENAS ", preco,"REAIS!!!")