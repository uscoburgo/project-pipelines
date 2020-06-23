import pandas as pd
import numpy as np
import re
import requests
from bs4 import BeautifulSoup
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
from plots_stocks import plotSentiment
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os
from dotenv import load_dotenv
load_dotenv()


def CreateReport(stock=None):
    #Creates a report filtering the database according to the parameters given
    data = pd.read_csv("../INPUT/df_analysis.csv") 
    df = pd.DataFrame(data)      
    outputString=''            
    
    if stock:
        try:
            df_stock = df[df['Ticker'] == stock]
            positive=df_stock.iloc[0,1]
            negative=df_stock.iloc[0,2]
            low=df_stock.iloc[0,3]
            high=df_stock.iloc[0,4]
            outputString += f'For {stock}, we found {positive} tweets with positive sentiment and {negative} with negative sentiment.\n'
            outputString += f'The high price for {stock} was {high} and the low price was {low}.\n'
            

            return outputString

        except:
            return "The ticker you entered has no sentiment analysis available"

   

    #plot sentiment
    res=plotSentiment(df_stock)
    print(res)
    print("\n") 



    
    
     
"""
    #-------------------------------------------------------------------------
    #basic statistics    
    mean=df_analysis['DELAY'].mean()
    outputString += f'mean delay = {mean}\n'    
    
    
    maxd=df_analysis['DELAY'].max()#show the maximum delay
    outputString += f'max delay = {maxd}\n'
        
       
    mind=df_analysis['DELAY'].min()#show the minimum delay
    outputString += f'min dealy = {mind}\n'
    
    stdd=df_analysis['DELAY'].std()
    outputString += f'std delay = {stdd}\n'
    
    #if the dataframe is empty it means the input parameters were not a valid input
    if df_analysis.shape[0]==0:
        outputString='There is no flight connection between these airports'
    
    print(outputString + '\n')
    """
    
    #------------------------------------------------------------------------------
  

"""
    #plotBestAirport
    if best:
        res=plotBestAirport(df_analysis)
        print(res)
        print('\n')
    else:
        res=plotWorstAirport(df_analysis)
        print(res)
        print('\n')
    ##################################################################################
    #PDF GENERATION
    
    generatePDF1()
    
    ##################################################################################
    #email 

    filename = "OUTPUT/report.pdf"
    #address='tzvuccyseraf@gmail.com'
    address=input('insert your e-mail address: ')
    sendMail(address,filename,outputString)
"""