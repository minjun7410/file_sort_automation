# 21-6-25 문제가 있는데 우리가 찾는 것은 문제 창에서 "문제 분류"가 필요한데
# 문제 분류가 로그인을 해야 접근할 수 있다. 아이디, 비밀번호만 치는 경우면 문제가 없는데
# 캡차같은 이중 보안 구조면 아예 셀레니움으로 로그인을 못한다.
# 구글링 해봤는데 열려있는 크롬 창으로 스크래핑하는 방법이 있었다.
# https://jakpentest.tistory.com/39 <- 참고

import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def crawling(number):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    browser.get("http://acmicpc.net/problem/" + number)
    try:
        show_spoiler = browser.find_element_by_xpath('//*[@id="problem_tags"]/div[2]/p/a')
        # showspoiler 가 없다면 패스
        show_spoiler.click()
        elements = browser.find_elements_by_xpath('//*[@id="problem_tags"]/div/ul/li/a')
    except selenium.common.exceptions.NoSuchElementException:
        elements = browser.find_elements_by_xpath(('//*[@id="problem_tags"]/ul/li/a'))
        pass
    result = list(map(lambda x: x.text, elements))
    print(number + '번 문제의 문제 분류는 ', *result, '입니다.')
    browser.quit()
    return result