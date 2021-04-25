from selenium import webdriver as wb
import time, json
from functions import *

quantidade,nomeArquivo = captarEntradas()

wbD = iniciarDriver()
arquivoJson = {}

#Cria os usuários
criaçãoDeItem(wbD,quantidade,arquivoJson,'usuario',
'body > div.page-password-generator > div.lp-pg.lp-ug > div.lp-pg-generated-password > div.lp-pg-generated-password__icon-wrapper > button.lp-pg-generated-password__icon.lp-pg-generated-password__icon-generate',
'username-generator')

#Cria as senhas
criaçãoDeItem(wbD,quantidade,arquivoJson,'senha',
'body > div.page-password-generator > div.lp-pg > div.lp-pg-generated-password > div.lp-pg-generated-password__icon-wrapper > button.lp-pg-generated-password__icon.lp-pg-generated-password__icon-generate',
'password-generator')

gerarArquivoJson(nomeArquivo,arquivoJson)
wbD.close()
