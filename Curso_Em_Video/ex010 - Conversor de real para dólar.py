import requests

print('{:.^40}'.format('EX010'))
n = float(input('quantos reais você tem na carteira? R$'))
requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
cotacao = requisicao.json()
print('Valor atual: R$' + cotacao['USD']['bid'])
d = cotacao['USD']['bid']
d = float(d)
print('R${:.2f}, convertido para dólar, hoje, você compraria aproximadamente ${:.2f}'.format(n, n/d))
