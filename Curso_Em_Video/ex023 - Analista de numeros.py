print('{:.^40}'.format('EX023'))
n = input("Digite um número entre 0 e 9999: ")
if len(n) > 3:
    print(
        "O número {} é composto por\nUnidade: {}\nDezenas: {}\nCentenas: {}\nMilhar: {}".format(n, n[3], n[2], n[1], n[0]))
else:
    print("O número {} é composto por\nUnidade: {}\nDezenas: {}\nCentenas: {}".format(n, n[2], n[1], n[0]))
