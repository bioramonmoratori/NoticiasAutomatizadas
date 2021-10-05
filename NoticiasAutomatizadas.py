#Noticias Automaticas 
#Autor: Ramon Moratori

import smtplib
import email.message
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import random
from selenium.webdriver.common.keys import Keys
import time
import numpy as np
import datetime

data = str(datetime.datetime.now().date())

################################################################################

#Configurando o Selenium e abrindo o Google Noticias

#Definindo o Navegador
browser = webdriver.Chrome(ChromeDriverManager().install())

#Abre a URL - Coloque aqui um link da aba 'noticias' do Google. Pesquise algum tema de sua escolha
browser.get('https://www.google.com/search?q=tecnologia&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiJl5_An7HzAhUiqJUCHf8qCnoQ_AUoAXoECAEQAw&biw=982&bih=708&dpr=1.25')

################################################################################

#Salvando os hiperlinks em uma lista chamada 'urls'

urls = []

clicar0 = browser.find_elements_by_xpath("//a[@href]")
for elem in clicar0:
    urls.append(elem.get_attribute("href"))
    
#Encontrar links do G1, Estadao, Tecmundo, O Globo e BBC

encontradosestadao = [ s for s in urls if 'estadao' in s ]
print(encontradosestadao)

encontradostecmundo = [ s for s in urls if 'tecmundo' in s ]
print(encontradostecmundo)

encontradosglobo = [ s for s in urls if 'g1' in s ]
print(encontradosglobo)

encontradosbbc = [ s for s in urls if 'bbc' in s ]
print(encontradosbbc)

#################################################################################

#Cria variaveis de condicao para caso encontrou o link ou nao

estadao=1
tecmundo=1
globo=1
bbc=1

#Conferir se foi encontrado os respectivos links e atribuir um valor a cada condicao

if(encontradosestadao == []): estadao = 0


if(encontradostecmundo == []): tecmundo = 0
        
if(encontradosglobo == []): globo = 0

if(encontradosbbc == []): bbc = 0

################################################################################

#Abre cada link presente em cada lista, pega a manchete e salva em um array 
#Array: [[Manchete1, Link1] [Manchete2, Link2] ...]
#OBS: O primeiro elemento do array esta vazio [Manchete1: '', Link1: '']


manchetes = np.array([['','']])

#ESTADAO
if(estadao == 1):
    #Abre todas as URL's do Estadao e pega os H1 presentes
    for i in range(0,len(encontradosestadao)):
        browser.get(encontradosestadao[i])
        time.sleep(5)
        get_title = browser.title
        print(get_title)        
        manchetesestadao = np.array([[get_title, str(encontradosestadao[i])]])
        manchetes = np.concatenate((manchetes, manchetesestadao))
        time.sleep(2)


#TECMUNDO
if(tecmundo == 1):
    #Abre todas as URL's do TecMundo e pega os H1 presentes
    for i in range(0,len(encontradostecmundo)):
        browser.get(encontradostecmundo[i])
        time.sleep(5)
        get_title = browser.title
        print(get_title)
        manchetestecmundo = np.array([[get_title, str(encontradostecmundo[i])]])
        manchetes = np.concatenate((manchetes, manchetestecmundo))
        time.sleep(2)
        

#GLOBO
if(globo == 1):
    #Abre todas as URL's do Globo e pega os H1 presentes
    for i in range(0,len(encontradosglobo)):
        print('I globo: ',i)
        print('len globo: ', len(encontradosglobo))
        browser.get(encontradosglobo[i])
        time.sleep(5)
        get_title = browser.title
        print(get_title)
        manchetesglobo = np.array([[get_title, str(encontradosglobo[i])]])
        manchetes = np.concatenate((manchetes, manchetesglobo))
        time.sleep(2)


#BBC
if(bbc == 1):
    #Abre todas as URL's da BBC e pega os H1 presentes
    for i in range(0,len(encontradosbbc)):
        browser.get(encontradosbbc[i])
        time.sleep(5)
        get_title = browser.title
        print(get_title)
        manchetesbbc = np.array([[get_title, str(encontradosbbc[i])]])
        manchetes = np.concatenate((manchetes, manchetesbbc))
        time.sleep(2)


print('Manchetes: ', manchetes)

################################################################################

#Percorrer o Array, organizar e guardar em apenas uma string 

textoemailinicio = f"""<p><h1 align='center'>Python News - Notícias Diárias ({data})</h1></p>
<p><h2 align='center'>Compilado de manchetes das notícias mais recentes, utilizando automação Python</h2></p>
<p><h3 align='center'>__________________________________________________________________________________________</h3></p>
<p></p>
<p></p>
    """

print(textoemailinicio)


#Comecamos o range do 1 pois o primeiro elemento do array esta vazio
for i in range(1,len(manchetes)):
    novamanchete = str(textoemailinicio) + "<p><h3 align='center'>" + str(manchetes[i][0]) + "</h3></p><p><h5 align='center'>" + str(manchetes[i][1]) + "</h5></p><p></p><p><h3 align='center'>__________________________________________________________________________________________</h3></p>" 
    textoemailinicio = novamanchete    
    
print(novamanchete)    
    

################################################################################

#Configurando o E-mail

def enviar_email():  
    corpo_email = novamanchete

    msg = email.message.Message()
    msg['Subject'] = "Python News - Noticias Diarias"
    msg['From'] = 'Digite aqui o seu E-mail (Remetente)'
    msg['To'] = 'Digite aqui o Destinatario1, Digite aqui o Destinatario2'
    password = 'Digite aqui a senha do seu E-mail (Remetente)' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
  
#Chamo a funcao e envio o E-mail
enviar_email()