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

time.sleep(4)

PalavraChave = "Extrato"
Pchave = web.find_element_by_xpath('//*[@id="input-bs-keyword"]')
Pchave.send_keys(PalavraChave);

Submit = web.find_element_by_xpath('//*[@id="submit-busca-simples"]')
Submit.click()
time.sleep(70)

links = []
print(get_all_links(web))
links = get_all_links(web);
print(len(links))
#elems = web.find_elements_by_tag_name('a')
#for elem in elems:
#    href = elem.get_attribute('href')
#    if href is not None:
#        print(href)

#for i in links:
#    print('a ' + links)

#for elem in range (30,40):
#    print(elems(elem))
#LinkEstratos = []
#LinkExtratos [1] = web.find_element_by_id('a href')
#print(LinkExtratos[1])
