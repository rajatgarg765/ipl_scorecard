# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:29:30 2021

@author: info
"""



import os
import time
import requests
import sys


def retrieve_html():
    for year in range(2019,2022):
        url='https://www.firstpost.com/firstcricket/points-table/series/ipl-{}.html'.format(year)
            
                #url='https://www.firstpost.com/firstcricket/points-table/series/ipl-{}.html'.format(year)
        
            
        texts=requests.get(url)
        text_utf=texts.text.encode('utf-8')
            
        if not os.path.exists("Data/html_Data/{}".format(year)):
            os.makedirs("Data/html_Data/{}".format(year))
        with open("Data/html_Data/{}/{}.html".format(year,year),"wb") as output:
            output.write(text_utf)
        
        sys.stdout.flush()
        
if __name__=="__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time Taken {}".format(stop_time-start_time))
    