import csv
from selenium import webdriver

driver=webdriver.Chrome(executable_path="chromedriver.exe");
driver.get("https://finance.yahoo.com/quote/BTC-EUR/history/")

dates = []
closes = []

for i in range(1, 11):
  dates.append(driver.find_element_by_xpath(f'//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[{i}]/td[1]').text)
  closes.append(driver.find_element_by_xpath(f'//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[2]/table/tbody/tr[{i}]/td[5]').text)

with open('eur_btc_rates.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    writer.writerow(['Date', 'Close'])

    for i in range(10):
      writer.writerow([dates[i], closes[i]])

driver.close()
driver.quit()