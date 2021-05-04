from selenium import webdriver
import time

from selenium import webdriver
import time

def get_all_links(driver):
    links = []
    elements = driver.find_elements_by_tag_name('a')
    for elem in elements:
        href = elem.get_attribute("href")
        links.append(href)
    return links





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
links = get_all_links(web);
print(len(links))
print( type(links))

linkcerto = []
for link in links :
    if link is not None:
        if 'docview' in link:
            linkcerto.append(link)
            #print(link)

print( linkcerto)
print('link certo posição 1: ' , linkcerto[1])

for link in linkcerto:
    web.get(link)
    time.sleep(5)
    

    
# falta (1): abrir proximas páginas e guardar os links certos
# falta (2): selecionar informações apenas de links corretos 
# falta (3): pegar as informações  