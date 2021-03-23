print('{:.^40}'.format('AULA01'))

# EX01 - Quadrado 2.0
entrada = "n1, n2, n3"
processamento = "soma = n1 + n2 + n3" \
                "resultado = soma*soma"
saida = "resultado"

# EX02 - Calculos
entrada = "n1, n2, n3, n4"
processamento = "multiplicacao = n1*n3" \
                "soma = n2+n4"
saida = "multiplicacao, soma"

# EX03 - Cotacao
entrada = "cotacao_dolar, reais"
processamento = "conversao = reais/cotacao_dolar"
saida = "conversao"

# EX04 - Abastacimento
entrada = "combustivel_litro,valor"
processamento = "resultado = valor/combustivel_litro"
saida = "resultado"

# EX05 - Temperatura
entrada = "celsius, fahrenheit"
processamento = "resultado = (celsius * 1.8) + 32"
saida = "resultado"

# EX06 - Volume
entrada = "altura, r"
processamento = "volume = 3.14 * (r*r) * altura"
saida = "volume"

# EX07 - Prestacao
entrada = "boleto, juros, atraso"
processamento = "resultado = boleto + (boleto * (juros/100)) * atraso"
saida = "resultado"

# EX08 - Milionario
entrada = "salario, despesas_mensais"
processamento = "sobra = salario - despesas_mensais" \
                "sobraAnual = sobra * 12" \
                "anos = 1000000/sobraAnual"
saida = "anos"


#Portugol

#EX01
'''
Algoritmo "EX01 - Quadrado 2.0"
var
    n1, n2, n3 : int
inicio
    escreval("Entre com o primeiro numero")
    leia(n1) 
    escreval("Entre com o segundo numero")
    leia(n2)
    escreval("Entre com o terceiro numero")
    leia(n3)
    soma := n1 + n2 + n3" 
    resultado = soma*soma
    escreva("O quadrado da soma dos números digitados é: ", resultado) 
Finalgoritmo


#EX02

Algoritmo "EX02 - Calculos"
var
    n1, n2, n3, n4 : int
inicio
    escreval("Entre com o primeiro numero")
    leia(n1) 
    escreval("Entre com o segundo numero")
    leia(n2)
    escreval("Entre com o terceiro numero")
    leia(n3)
    escreval("Entre com o quarto numero")
    leia(n4)
    multiplicacao = n1*n3" 
    soma := n2+n4"
    escreval("A multiplicação entre o primeiro numero digitado e o terceiro é: ", multiplicacao,
    "/n A soma entre segundo numero digitado e o quarto é:", soma) 
Finalgoritmo


#EX03

Algoritmo "EX03 - Cotacao"
var
    cotacao_dolar, reais : float
inicio
    escreval("Entre com a cotação do dolar")
    leia(cotacao_dolar) 
    escreval("Entre com o valor em reais que deseja realizar a conversão")
    leia(reais)
    conversao := reais/cotacao_dolar
    escreval("Com o valor de R$ ",reais, "você consegue comprar $ ", conversao) 
Finalgoritmo


#EX04

Algoritmo "EX04 - Abastecimento"
var
    combustivel_litro,valor : float
inicio
    escreval("Digite o preço do litro do combustível")
    leia(combustivel_litro) 
    escreval("Digite o valor que você deseja abastecer")
    leia(valor)
    resultado := valor/combustivel_litro
    escreval("Com o valor de R$ ",reais, "você consegue comprar ", resultado,"L") 
Finalgoritmo



#EX05

Algoritmo "EX05 - Temperatura"
var
    celsius, fahrenheit : float
inicio
    escreval("Entre com a quantidade de graus em celsius")
    leia(celsius) 
    resultado := (celsius * 1.8) + 32
    escreval(celsius,"º em fahrenheit é: ", resultado)
Finalgoritmo


#EX06

Algoritmo "EX06 - Volume"
var
    altura, r : float
inicio
    escreval("Entre com a altura")
    leia(altura) 
    escreval("Entre com o valor do raio")
    leia(r)
    volume := 3.14 * (r*r) * altura
    escreval("O volume do cilindro é:", volume) 
Finalgoritmo


#EX07

Algoritmo "EX07 - Prestacao"
var
    boleto, juros : float , atraso : int
inicio
    escreval("Entre com o valor do boleto")
    leia(boleto) 
    escreval("Entre com o juros cobrado")
    leia(juros)
    escreval("Entre com o numero de dias de atraso")
    leia(atraso)
    resultado := boleto + (boleto * (juros/100)) * atraso
    escreval("O novo valor a ser pago é de:", resultado) 
Finalgoritmo


#EX08

Algoritmo "EX - 08 - Milionario V2"
var
    salario, despesas_mensais : float
inicio
    escreval("Entre com o seu salário")
    leia(salario) 
    escreval("Entre com o valor das suas despesas")
    leia(despesas_mensais)
    sobra := salario - despesas_mensais"
    sobraAnual := sobra * 12
    anos := 1000000/sobraAnual
    escreval("Faltam ", anos, "para você ficar milionario") 
Finalgoritmo
'''