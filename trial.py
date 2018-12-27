from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://google.com")

driver.maximize_window()

title = driver.title
print(title)