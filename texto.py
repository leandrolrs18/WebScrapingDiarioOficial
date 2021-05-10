from selenium import webdriver
import time

web = webdriver.Chrome()
link = 'http://diariooficial.rn.gov.br/dei/dorn3/docview.aspx?id_jor=00000001&data=20210508&id_doc=722595'
s = link.split("data=", 1)[1]
print(s)
p = s.split("&", 1)[0]
print(p)
l = link.split("doc=", 1)[1]
print(l)
novolink = 'http://diariooficial.rn.gov.br/dei/dorn3/documentos/00000001/'+p+'/'+l+'.htm'
print(novolink)
web.get(novolink)
time.sleep(10)

conteudo = web.find_elements_by_class_name("WordSection1")
print(conteudo)

b = web.find_elements_by_class_name('WordSection1')

for title in b:
    print('b', title.text)


#regex

#talvez tenha como pegar de outro jeito, levando em consideração a página embutida iframe