from selenium import webdriver as wb
import time, json

def iniciarDriver():
  return wb.Chrome('./chromedriver')
  
def encontrarInput(wbD):
  return wbD.find_element_by_css_selector('#GENERATED-PASSWORD')

def acessarSite(wbD,endpoint):
  wbD.get(f'https://www.lastpass.com/pt/{endpoint}')

def gerador(wbD,saida,chave,arquivo,item,botaoGerarSelector):
  valor = saida.get_attribute('value')
  if item == 'usuario':
    arquivo[chave]= { item : valor }
  else:
    arquivo[chave].update({ item : valor })
  generateButton = wbD.find_element_by_css_selector(botaoGerarSelector)
  generateButton.click()
  return

def captarEntradas():
  try:
    quantidade = int(input("Digite a quantidade de usuário que você deseja gerar: "))
    nomeArquivo = input("Digite o nome do arquivo json a ser gerado: ")
    return quantidade,nomeArquivo
  except:
    print("O valor inserido é inválido.")

def gerarArquivoJson(nomeArquivo,arquivoJson):
  with open(f'{nomeArquivo}.json','w') as dic:
    json.dump(arquivoJson,dic)
    dic.close()

def criaçãoDeItem(wbD,quantidade,arquivoJson,nomeItem,selector,endpoint):
  acessarSite(wbD,'username-generator')
  inputGerador = encontrarInput(wbD)
  time.sleep(1.2)
  for i in range(quantidade):
    gerador(wbD,inputGerador,i,arquivoJson,nomeItem,selector)