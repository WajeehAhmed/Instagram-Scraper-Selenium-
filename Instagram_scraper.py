from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import time
import csv
import xlsxwriter 
browser = webdriver.Chrome('C:/chromedriver_win32/chromedriver')#path to chrome webdriver
workbook = xlsxwriter.Workbook('France.xlsx')#filename
worksheet = workbook.add_worksheet('France')#worksheet name
worksheet.write(0,0,'User Names')
worksheet.write(0,1,'Bio')
roww = 1
with open('Book1.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    for row in reader:
        print(row[0].replace('ï»¿',''))
        lst = ''
        try:
            browser.get('https://www.instagram.com/'+row[0].replace('ï»¿',''))
            time.sleep(5)
            details = browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[2]').text
            #lst = re.findall('\S+@\S+', details)#if you just want to scrap emails from bio
            
        except:
            pass
        
        if(len(lst)!=0):
            #print(lst)
            worksheet.write(roww,0,row[0].replace('ï»¿',''))
            #worksheet.write(roww,1," ".join(str(x) for x in lst)) #for emails only
            worksheet.write(roww,1,str(details))
            roww+=1
        else:
            worksheet.write(roww,0,row[0].replace('ï»¿',''))
            roww+=1
            pass
        
        
workbook.close()