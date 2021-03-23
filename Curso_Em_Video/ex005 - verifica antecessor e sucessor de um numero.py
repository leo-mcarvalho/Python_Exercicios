while True:
    n = input('Digite um número inteiro ')
    if n.isnumeric():
        n = int(n)
    break
print('O número digitado foi {}, o número antecessor dele é {} e o sucessor é {}'.format(n, n - 1, n + 1))
