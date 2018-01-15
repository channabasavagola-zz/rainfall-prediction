import pandas as pd

url = "http://bangalore.citizenmatters.in/articles/100-years-of-rainfall-data-for-bengaluru"
rainfall_data = pd.read_html(url)[0]
# print(rainfallData)
months = ['Year/Month', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall_data.columns = months
rainfall_data = rainfall_data.drop(0).drop(101).drop(102)
rainfall_data.set_index('Year/Month', inplace=True)
rainfall_data = rainfall_data.astype('float64')
rainfall_data.to_excel("data/rainfallData.xlsx")
