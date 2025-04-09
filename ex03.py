intervalodentro = 0
intervalofora = 0
for x in range(1,11) :
    num = int(input("Digite um número: "))
    if num >= 10 and num <= 20:
        intervalodentro = intervalodentro + 1
    else:
        intervalofora = intervalofora + 1
print(f"Números dentro do intervalo: {intervalodentro} e números fora: {intervalofora}")