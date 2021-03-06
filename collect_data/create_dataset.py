import pandas as pd
from collect_data import stock_values_connector as stock_prices_class
from stock_movement_prediction import prophet_prediction as prophet_predict




def create_data(ticker):
    #Get All values from stock daily
    stock_values = prophet_predict.prophet_prediction(ticker)
    stock_values['Ticker'] = ticker
    stock_values.to_csv('stock_values.csv')

    #Get annual income statement from stock
    annual_income_statement = stock_prices_class.annual_income_statement(ticker)

    #Get financial ratios from stock
    financial_ratios = stock_prices_class.annual_financial_ratios(ticker)


    #Join financial tables
    frames = [annual_income_statement, financial_ratios]
    financial_dataframe = pd.concat(frames)
    financial_dataframe = financial_dataframe.reset_index()
    financial_dataframe = financial_dataframe.rename(columns={'index': 'Indicator'})
    financial_dataframe = pd.melt(financial_dataframe, id_vars=['Indicator'], value_vars=['2016','2017','2018','2019','2020'])
    financial_dataframe = financial_dataframe.rename(columns={'value': 'Indicator_value','variable':'Year'})
    indexNames = financial_dataframe[financial_dataframe['Indicator'] == 'reportedCurrency'].index
    indexNames1 = financial_dataframe[financial_dataframe['Indicator'] == 'fillingDate'].index
    indexNames2 = financial_dataframe[financial_dataframe['Indicator'] == 'acceptedDate'].index
    indexNames3 = financial_dataframe[financial_dataframe['Indicator'] == 'period'].index
    indexNames4 = financial_dataframe[financial_dataframe['Indicator'] == 'link'].index
    indexNames5 = financial_dataframe[financial_dataframe['Indicator'] == 'finalLink'].index
    financial_dataframe.drop(indexNames, inplace=True)
    financial_dataframe.drop(indexNames1, inplace=True)
    financial_dataframe.drop(indexNames2, inplace=True)
    financial_dataframe.drop(indexNames3, inplace=True)
    financial_dataframe.drop(indexNames4, inplace=True)
    financial_dataframe.drop(indexNames5, inplace=True)
    financial_dataframe['Ticker'] = ticker
    financial_dataframe.to_csv('financial_ratios.csv')

    #Get balance sheet
    balance_sheet = stock_prices_class.annual_balance_sheet(ticker)
    balance_sheet = balance_sheet.reset_index()
    balance_sheet = balance_sheet.rename(columns={'index': 'Indicator'})
    balance_sheet = pd.melt(balance_sheet, id_vars=['Indicator'], value_vars=['2016','2017','2018','2019','2020'])
    balance_sheet = balance_sheet.rename(columns={'value': 'Indicator_value','variable':'Year'})
    indexNames = balance_sheet[balance_sheet['Indicator'] == 'reportedCurrency'].index
    indexNames1 = balance_sheet[balance_sheet['Indicator'] == 'fillingDate'].index
    indexNames2 = balance_sheet[balance_sheet['Indicator'] == 'acceptedDate'].index
    indexNames3 = balance_sheet[balance_sheet['Indicator'] == 'period'].index
    indexNames4 = balance_sheet[balance_sheet['Indicator'] == 'link'].index
    indexNames5 = balance_sheet[balance_sheet['Indicator'] == 'finalLink'].index
    balance_sheet.drop(indexNames, inplace=True)
    balance_sheet.drop(indexNames1, inplace=True)
    balance_sheet.drop(indexNames2, inplace=True)
    balance_sheet.drop(indexNames3, inplace=True)
    balance_sheet.drop(indexNames4, inplace=True)
    balance_sheet.drop(indexNames5, inplace=True)

    balance_sheet['Ticker'] = ticker
    balance_sheet.to_csv('balance_sheet.csv')

    #Get Cash Flow
    cash_flow = stock_prices_class.annual_cash_flow(ticker)
    cash_flow = cash_flow.reset_index()
    cash_flow = cash_flow.rename(columns={'index': 'Indicator'})
    cash_flow = pd.melt(cash_flow, id_vars=['Indicator'], value_vars=['2016','2017','2018','2019','2020'])
    cash_flow = cash_flow.rename(columns={'value': 'Indicator_value','variable':'Year'})
    indexNames = cash_flow[cash_flow['Indicator'] == 'reportedCurrency'].index
    indexNames1 = cash_flow[cash_flow['Indicator'] == 'fillingDate'].index
    indexNames2 = cash_flow[cash_flow['Indicator'] == 'acceptedDate'].index
    indexNames3 = cash_flow[cash_flow['Indicator'] == 'period'].index
    indexNames4 = cash_flow[cash_flow['Indicator'] == 'link'].index
    indexNames5 = cash_flow[cash_flow['Indicator'] == 'finalLink'].index
    cash_flow.drop(indexNames, inplace=True)
    cash_flow.drop(indexNames1, inplace=True)
    cash_flow.drop(indexNames2, inplace=True)
    cash_flow.drop(indexNames3, inplace=True)
    cash_flow.drop(indexNames4, inplace=True)
    cash_flow.drop(indexNames5, inplace=True)
    cash_flow['Ticker'] = ticker
    cash_flow.to_csv('cash_flow.csv')
