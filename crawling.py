from selenium import webdriver
browser = webdriver.Chrome("./chromedriver.exe")
def crawling(number):
    browser.get("https://www.acmicpc.net/problem/" + number)
crawling("1000")