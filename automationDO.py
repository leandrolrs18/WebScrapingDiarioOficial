from selenium import webdriver
import time

web = webdriver.Chrome()

web.get('http://diariooficial.rn.gov.br/dei/dorn3/Search.aspx')

time.sleep(4)

PalavraChave = "Extrato"
Pchave = web.find_element_by_xpath('//*[@id="input-bs-keyword"]')
Pchave.send_keys(PalavraChave);

Submit = web.find_element_by_xpath('//*[@id="submit-busca-simples"]')
Submit.click()
time.sleep(70)

elems = web.find_elements_by_tag_name('a')
for elem in elems:
    href = elem.get_attribute('href')
    if href is not None:
        print(href)

#for elem in range (30,40):
#    print(elems(elem))
#LinkEstratos = []
#LinkExtratos [1] = web.find_element_by_id('a href')
#print(LinkExtratos[1])