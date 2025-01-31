faturamento = input(" Digite o valor total de vendas: ")
custo = input(" Digite o valor total dos insumos: ")

vendas_apos = input(" Houveram novas vendas desde o ultimo fechamento? : ")
Sim = True
Não = False
if True:
    print("Adicionar os valor das novas vendas: ")
    novas_vendas = input("Digite o valor das vendas: ")


faturamento = faturamento + novas_vendas  # aditivo a variavel

impostos = (
    faturamento * 0.04
)  # (calculo da aliquota de imposto de 4% simples nacional )
lucro = faturamento - custo - impostos


margem_lucro = lucro / faturamento


print("O faturamento foi de: ", faturamento)
print("O custo foi de: ", custo)
print("O Lucro foi de:", lucro)
print(
    " A margem de lucro foi de", round(margem_lucro, 2)
)  # uso da função Round para arredondar o valor quebrado

mensagem = " O Faturamento da loja foi de: "
