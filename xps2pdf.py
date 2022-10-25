import os
import fitz
import configparser
import datetime

# CONFIGPARSER CONFIGURADO PARA LER O ARQUIVO COMPLEMENTAR DO SISTEMA, ARQUIVO COM AS VÁRIÁVEIS DE SISTEMA COMO CAMINHO DOS DIRETÓRIOS
cfg = configparser.ConfigParser()
cfg.read('config.ini')

timeLog = datetime.datetime.now()

# DIRETÓRIO DE ARQUIVOS XPS(IN)
inputXps = cfg.get('DEFAULTPATH', 'file_in')
# DIRETÓRIO DE ARQUIVOS PDF(OUT)
outputPdf = cfg.get('DEFAULTPATH', 'file_out')

# LISta DIRETORIO OUTPUT PDF
repo_pdf = os.listdir(outputPdf) 

# LISTA DIRETÓRIO INPUT XPS
repo = os.listdir(inputXps)

# FUNÇÃO PARA REGISTRAR ARQUIVOS CONVERTIDOS
def recordLog(namereglog):    
    with open('receive.log', 'a+') as file:
        file.write(f'{timeLog} - {namereglog} CONVERTIDO COM SUCESSO PARA PDF. \n')
        file.seek(0)  

def recordLogError(namereglog):    
    with open('error.log', 'a+') as file:
        file.write(f'{timeLog} - {namereglog} ERRO AO CONVERTER O ARQUIVO. \n')
        file.seek(0)

for fileX in repo:
    # ABRE O ARQUIVOS E CAPTURA O NOME(BINÁRIO)
    binName = open(inputXps + fileX,'rb')
    # ABRE O ARQUIVO XPS
    xpsOpen = fitz.open(binName)    
    # CONVERTE O AQUIVO XPS PARA PDF E ARMAZENA NA VARIÁVEL 'xpsData'
    xpsData = xpsOpen.convert_to_pdf()
    # SALVA A CONVERSÃO EM PDF
    pdfData = fitz.Document("pdf", xpsData)   
    pdfData.save(outputPdf + fileX + '.pdf')    
    recordLog(fileX)
    print('Convertendo arquivo ', fileX)

