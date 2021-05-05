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

for link in linkcerto:
    web.get(link)
    time.sleep(1)


# falta (3): pegar as informações  

