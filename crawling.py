# 21-6-25 문제가 있는데 우리가 찾는 것은 문제 창에서 "문제 분류"가 필요한데
# 문제 분류가 로그인을 해야 접근할 수 있다. 아이디, 비밀번호만 치는 경우면 문제가 없는데
# 캡차같은 이중 보안 구조면 아예 셀레니움으로 로그인을 못한다.
# 구글링 해봤는데 열려있는 크롬 창으로 스크래핑하는 방법이 있었다.

# 1. cmd 창에서 C:\Program Files\Google\Chrome\Application\ 디렉토리로 이동 후
# 2. chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"
# (9222 포트로 크롬을 디버깅 모드로 실행한다는 뜻.  위의 구문은 temp파일을 C:/ChromeTEMP 폴더를 만들어서 보관하는 것.
# * 크롬 창이 뜨면 닫지 않고 기달린다.
# 3.
# https://jakpentest.tistory.com/39

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def crawling(number):
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome("chromedriver.exe", options=chrome_options)
    browser.get("http://acmicpc.net/problem/" + number)
    show_spoiler = browser.find_element_by_xpath('//*[@id="problem_tags"]/div[2]/p/a')
    print(show_spoiler.get_attribute())
    # show_spoiler 가 있는 경우 없는 경우가 있기 때문에 예외 처리가 필요하다.
    elements = browser.find_element_by_xpath('//*[@id="problem_tags"]/ul')
    print(elements.text)
    browser.quit()

crawling("1000")