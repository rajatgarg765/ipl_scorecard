# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:35:26 2021 

@author: info
""" 
import numpy as np
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup
import os
import csv

def met_data(year):
    
    file_html = open('Data/html_Data/{}/{}.html'.format(year,year), 'rb')
    plain_text = file_html.read()

    tempD = []
    finalD = []

    soup = BeautifulSoup(plain_text, "html.parser")
    for table in soup.find_all('table', {'class': 'general-tbl ipl-points-table'}):
        for data in table(['style','script']):
            data.decompose()
    a=(','.join(table.stripped_strings))
    l=a
    tempD=l.split(",")
  
    
    
                 #for data in table(['style','script']):
                     #data.decompose()
                     #a=(' '.join(table.stripped_strings))
                
    return tempD              
'''    rows = len(tempD) /9

    for times in range(round(rows)):
        newtempD = []
        for i in range(8):
            newtempD=tempD[0]
            tempD.pop(0)
        finalD.append(newtempD)

    length = len(finalD)


    return finalD
'''
'''def data_combine(year, cs):
    for a in pd.read_csv('Data/Real-Data/real_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist
'''

if __name__ == "__main__":
    if not os.path.exists("Data/Real-Data"):
        os.makedirs("Data/Real-Data")
    for year in range(2019, 2022):
        final_data = []
        with open('Data/Real-Data/real_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            wr.writerow(
                ['Pos','Team','Team Sym','Plyd','Won','LOst','tied','net rr','pts'])
        for rows in range(0, 9):
            temp = met_data(year)
            final_data = final_data + temp
      

        with open('Data/Real-Data/real_' + str(year) + '.csv', 'a') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')
            a=np.array(final_data)
            a=a[8:]
            for i in range(0,len(a),9):
                if a[i]=='Pos':
                    break
                else:
                    
                    wr.writerow(a[i:9+i])
            '''matrix=[]
            for i in range(10):
                for j in range(9):
                    s=[]
                    s.append(a)
                matrix.append(s)
                
            for i in range(10):
                for j in range(9):
                    wr.writerow(a)
                print()
                wr.writerow(a)
            '''                        
 
        
        

