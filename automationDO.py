from selenium import webdriver
import time
import xlsxwriter
from datetime import  date
from cx_Freeze import setup, Executable
import sys

def get_all_links(driver):
    links = []
    texto = []
    elements = driver.find_elements_by_tag_name('a')
    for elem in elements:
        href = elem.get_attribute("href")
        texto.append(elem.text)
        links.append(href)
    return links, texto

def start(P_chave, paginas):
    links = []
    linkcerto = []
    novolink = []
    texxto = []
    i = 0
    web = webdriver.Chrome()
    web.get('http://diariooficial.rn.gov.br/dei/dorn3/Search.aspx')
    time.sleep(2)
    PalavraChave = P_chave
    Pchave = web.find_element_by_xpath('//*[@id="input-bs-keyword"]')
    Pchave.send_keys(PalavraChave)

    Submit = web.find_element_by_xpath('//*[@id="submit-busca-simples"]')
    Submit.click()
    time.sleep(60)

    while True:
        links, texxto = get_all_links(web);   
        for link in links :
            if link is not None:
                if 'docview' in link:
                    linkcerto.append(link)
        t = web.find_element_by_xpath('//*[@id="Form1"]/section[2]/div/div[2]/a[2]')
        t.click() 
        i = i + 1            
        if(i == paginas):
            break

    linkcerto = list(dict.fromkeys(linkcerto))
    print('a', linkcerto)
    for link in linkcerto:
        d = link.split("data=", 1)[1]
        n = d.split("&", 1)[0]
        l = link.split("doc=", 1)[1]
        novolink.append('http://diariooficial.rn.gov.br/dei/dorn3/documentos/00000001/'+n+'/'+l+'.htm')
    return novolink, web    

def informacoes(links, web):
    result = []
    for i in links:
        web.get(i)
        time.sleep(2)
        conteud = web.find_elements_by_class_name("WordSection1")
        for element in conteud:
            result.append(element.text)
           
    return result      
    
def gerarExcel (texto):
    today = date.today()
    today = str(today) +'.xlsx'
    print(today)
    with xlsxwriter.Workbook(today) as workbook:
        worksheet = workbook.add_worksheet()

        for row_num, data in enumerate(texto):
            print(row_num, data)
            worksheet.write_string(row_num, 0 , data)

if __name__ == '__main__':
    
    links = []
    texto = []
    links, web = start("Extrato", 7)  # parametros: palavra de pesquisa e numero de pag pesquisadas 
    texto = informacoes(links, web)  
    gerarExcel(texto)
    


#falta criar um executável
# usar regex caso queira salvar o texto de um jeito diferente 
