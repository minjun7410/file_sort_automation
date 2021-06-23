# 디렉토리 안에 있는 파이썬 파일들 이름으로 백준 사이트의 문제 분류대로 정렬하는 프로그램 만들기

# 순서

# 1. 현재 작업 공간에 남아있는 file 들 이름을 조사(문제 번호만 슬라이싱)[아래 문장 반복]
# 2. 문제 번호를 가지고 "https://www.acmicpc.net/problem/" + "문제 번호" 주소
# 사이트에서 '알고리즘 분류' 탭의 정보들을 크롤링 [알고리즘 분류 리스트 가지고 아래 문장 반복]
# 3. 스크래핑한 정보가 현재 작업 공간의 directory 중에 있는 지 조사
# 3-1. 없으면 만들고(os.mkdir) 그 안에 현재 파일 복붙
# 3-2. 있으면 그 안에 현재 파일 복붙
# 4. 현재 파일 삭제(os.remove)

import os
import shutil

def extraction(file):  # 문제 번호만 추출하는 함수
    result = ''
    for char in file:
        if char.isdigit():
            result += char
    return result
def classification(file, classfy_list):  # 파일을 폴더에 분류(copy)해주는 함수
    for target in classfy_list:
        if target in os.listdir('.'):  # 이미 같은 이름의 폴더가 있을 경우
            shutil.copy(file, target)
        else:  # 같은 이름의 폴더가 없는 경우
            os.mkdir(target)
            shutil.copy(file, target)
    return
def research_file():  # 1. 작업 공간에 있는 파일들을 반복문으로 조사하는 함수
    print(os.getcwd())  # 현재 작업 공간
    file_list = [target for target in os.listdir('.') if os.path.isfile(target)]
    print(file_list)
    for file in file_list:
        if file.find('.py') == 0: continue
        file_e = extraction(file)
        if file_e == '':  continue  # 문제 번호가 안적힌 파이썬 파일은 제외
        #classify_list = crawling(file_e)  # 2. 크롤링으로 알고리즘 분류 정보 받아오기
        classify_list = ['DFS', '그래프 이론']
        classification(file, classify_list)
        os.remove(file)
research_file()