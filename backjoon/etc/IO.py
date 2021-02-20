"""
변수1, 변수2 = map(int, input().split())
변수1, 변수2 = map(int, input().split(기준문자))
변수1, 변수2 = map(int, input(문자열).split())
변수1, 변수2 = map(int, input(문자열).split(기준문자))
"""

a, b = map(int, input('숫자 두 개를 입력하세요: ').split(',')) # 입력받은 값을 콤마를 기준으로 분리