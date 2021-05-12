from selenium import webdriver
import time


def get_all_links(driver):
    links = []
    texto = []
    elements = driver.find_elements_by_tag_name('a')
    for elem in elements:
        href = elem.get_attribute("href")
        texto.append(elem.text)
        links.append(href)
    return links, texto


web = webdriver.Chrome()
web.get('http://diariooficial.rn.gov.br/dei/dorn3/Search.aspx')
time.sleep(2)

PalavraChave = "Extrato"
Pchave = web.find_element_by_xpath('//*[@id="input-bs-keyword"]')
Pchave.send_keys(PalavraChave)

Submit = web.find_element_by_xpath('//*[@id="submit-busca-simples"]')
Submit.click()
time.sleep(60)


links = []
linkcerto = []
texto = []
i = 0

while True:
    links, texto = get_all_links(web);
    
    for link in links :
        if link is not None:
            if 'docview' in link:
                linkcerto.append(link)
    t = web.find_element_by_xpath('//*[@id="Form1"]/section[2]/div/div[2]/a[2]')
    t.click() 
    i = i + 1            
    if(i == 5):
        break
    
print( linkcerto)
print('link certo posição 1: ' , linkcerto[1])


linkcerto = list(dict.fromkeys(linkcerto))
print('aa', linkcerto)
novolink = []
conteudo = []
for link in linkcerto:
   # web.get(link)
    d = link.split("data=", 1)[1]
    n = d.split("&", 1)[0]
    l = link.split("doc=", 1)[1]
    novolink.append('http://diariooficial.rn.gov.br/dei/dorn3/documentos/00000001/'+n+'/'+l+'.htm')

print(novolink)
result = []
resultado = ()
for i in novolink:
    web.get(i)
    time.sleep(2)
    conteud = web.find_elements_by_class_name("WordSection1")
    for element in conteud:
        print('dgr', element.text)
        result.append(element.text)
        
    resultado = tuple(result)    

print("resultado: ", result)


#salvar no excel resultado 
# usar regex caso queira salvar de um jeito diferente 
# aumentar o numero de pag extraidas
# pra colocar funções e main: https://stackoverflow.com/questions/42880916/selenium-is-not-printing-the-text#comment72865499_42880935