# janela para selecionar a pasta  usando bibliotecas python
import os
from tkinter.filedialog import askdirectory
import shutil

nome_da_pasta_selecionada = askdirectory()
print(
    f"Pasta selecionada: {nome_da_pasta_selecionada}"
)  # faltava a identação correta e f strings para seleção correta

lista_arquivos = os.listdir(nome_da_pasta_selecionada)
print(f"Arquivos encontrados: {lista_arquivos}")

nome_pasta_backup = "backup"
nome_completo_pasta_backup = f"{nome_da_pasta_selecionada}/{nome_pasta_backup}"
if not os.path.exists(nome_completo_pasta_backup):
    os.mkdir(nome_completo_pasta_backup)  # biblioteca para criação da pasta

for arquivo in lista_arquivos:
    nome_completo_arquivo = os.path.join(
        nome_da_pasta_selecionada, arquivo
    )  # path join substitui a f manual
    nome_final_do_arquivo = os.path.join(nome_completo_pasta_backup, arquivo)

    if os.path.isfile(nome_completo_arquivo):  # verificação se é um arquivo
        shutil.copytree(nome_completo_arquivo, nome_final_do_arquivo)
        shutil.copy2(
            nome_completo_arquivo, nome_final_do_arquivo
        )  # biblioteca para copiar os arquivos e colar
        print(f"Arquivo copiado: {arquivo}")
    elif (
        os.path.isdir(nome_completo_arquivo) and arquivo != nome_pasta_backup
    ):  # verificação se é uma pasta e evita copia da copia da pasta backup
        shutil.copytree(nome_completo_arquivo, nome_final_do_arquivo)
        print(f"Pasta copiada: {arquivo}")
