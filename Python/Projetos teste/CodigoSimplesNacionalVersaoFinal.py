print ("Olá! Vamos Calcular a sua margem de lucro e o DAS de suas Vendas")


def obter_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida! Digite um número válido.")


faturamento = obter_numero("Digite o valor total de vendas: R$ ")
custo = obter_numero("Digite o valor total dos insumos: R$ ")

# faltava a identação correta para as floats, uso da função def com return  para evitar que desse quebra caso fosse enviado uma palavra ao inves de um numero

while True:
    vendas_apos = input("Houveram novas vendas desde o último fechamento? (Sim/Não):")
    if vendas_apos.lower() in ["sim", "não"]:
        break
    else:
        print("Comando inválido ! Digite sim ou não.")
# uso do laço while para receber as respostas do usuario, acompanhado de if e else para garantir dados validos

if vendas_apos.lower() in ["sim"]:
    novas_vendas = float(input("Digite o valor das novas vendas: R$ "))
    faturamento += novas_vendas

if vendas_apos.lower() in ["sim"]:
    novo_custo = float(input("Digite o valor de novos insumos: R$ "))
    faturamento += novo_custo

# uso de lower para que as variações SIM,sim e Sim se tornassem validas
# adição de formulas caso haja novo custo e novas vendas

impostos = faturamento * 0.04
# (calculo da aliquota de imposto de 4% simples nacional )


lucro = faturamento - custo - impostos


if faturamento > 0:
    margem_lucro = lucro / faturamento
else:
    margem_lucro = 0
# Para evitar a quebra quando o valor for 0 já que em python não é possivel


print("O faturamento foi de: R$", faturamento)
print("O custo foi de: R$ ", custo)
print("O Lucro foi de: R$ ", lucro)
print(" A margem de lucro foi de", round(margem_lucro, 2))
print("Saldo de imposto a pagar:R$ ", round(impostos,1))
# uso da função Round para arredondar o valor quebrado
# Adição de saldo de imposto da pagar e de R$ para cada resultado em dinheiro
