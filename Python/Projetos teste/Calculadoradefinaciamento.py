# Não calcular portecentagem usando %, pois se trata de um operador de python
# mod = resto de uma divisão
# EX:


tempo_contrato = 365
tempo_anos = 365 / 12
tempo_meses = 365 % 12

print(
    "Tempo em anos", int(tempo_anos)
)  # para evitar a quebra converter  o resultado de float para int
print("Tempo em meses: ", int(tempo_meses))

