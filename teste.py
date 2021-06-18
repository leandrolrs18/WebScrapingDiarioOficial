from selenium import webdriver
import time
import xlsxwriter
import xlrd
from datetime import  date



def abrir_arquivo(arquivo):
    data = []
    #Abra e leia um arquivo Excel
    workbook = xlrd.open_workbook(arquivo ,   on_demand = True)
    # obter a primeira planilha
    worksheet = workbook.sheet_by_index(0)
    for row in range(0, worksheet.nrows):
        #obtem a informação que tem numa linha
        data.append(worksheet.row_values(row))
    return data, worksheet


if __name__ == '__main__':
    data = []
    ndata = []
    data, worksheet = abrir_arquivo ('2021-06-17.xlsx')
    #print(str(data[0]))
    print('a', data[0][0])
    print(type(data[0]))
    print(str(data[2][0]))

    array = data[19][0].split('\n')
    ndata.append(array)
    print('a', ndata[0][1])
    print('a', ndata[0][1])
    index = ndata[0][1].find("viver")
    print(index)

    #http://diariooficial.rn.gov.br/dei/dorn3/docview.aspx?id_jor=00000001&data=20210617&id_doc=726957
    # padro n deve ser seguido: http://diariooficial.rn.gov.br/dei/dorn3/docview.aspx?id_jor=00000001&data=20210617&id_doc=726944
    # http://diariooficial.rn.gov.br/dei/dorn3/docview.aspx?id_jor=00000001&data=20210617&id_doc=726864
