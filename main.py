# -*- coding: utf-8 -*-
"""stock_investment_assistance.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CYIFPs0UYc8GgcN_SSXOALthaIk_eUEI

# 1. Environment&Import
"""
import usia
start='2023-01-01'
end='2023-06-20'

"""1. Create portfolio from csv"""
# path="data\public.csv"
# portfoilo=usia.portfolio(path,start,end)
# portfoilo.implement()
"""2. Search Tickers"""
# searched=usia.tickerSearch('NASDAQ','헬스케어 장비 및 용품').download(start,end,filter_percent=0.1)
# print(searched)
# tickers=searched.index

"""3. Compare Financials"""
watchlist=['PANW','AMZN','RCM','STEM']
sample=['AAPL','F','DIS','AMZN','KO','GOOG','XOM']
result=usia.financialCompare(sample).keyFinancialTable()
print(result)

