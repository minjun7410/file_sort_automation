# 디렉토리 안에 있는 파이썬 파일들 이름으로 백준 사이트의 문제 분류대로 정렬하는 프로그램 만들기

# 순서

# 1. 현재 작업 공간에 남아있는 file 들 이름을 조사(문제 번호만 슬라이싱)[아래 문장 반복]
# 2. 문제 번호를 가지고 "https://www.acmicpc.net/problem/" + "문제 번호" 주소
# 사이트에서 '알고리즘 분류' 탭의 정보들을 스크래핑 [알고리즘 분류 리스트 가지고 아래 문장 반복]
# 3. 스크래핑한 정보가 현재 작업 공간의 directory 중에 있는 지 조사
# 3-1. 없으면 만들고(os.mkdir) 그 안에 현재 파일 복붙
# 3-2. 있으면 그 안에 현재 파일 복붙
# 4. 현재 파일 삭제(os.remove)

import os
print(os.getcwd()) # 현재 작업 공간
for root, dir, files in os.walk('.'):
    print(root, dir, files)
