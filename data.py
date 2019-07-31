# python_study Cp.1 String
# 파이썬은 ;을 필요로 하지 않는다
# 제일 기본적인 Hello World를 출력하는 방법이다
message1 = "Hello World"

print(message1)
# '을 텍스트로 넣고 싶을 때는 '앞에 \를 붙인다
# message2 = 'HyunKi's World' 이렇게 할시 2번째 '를 string의 끝으로 봐 오류가 생김
# 아니면 "Hyunki's World"로 사용
message2 = 'HyunKi\'s World' 

print(message2)

# 줄 바꿈을 하고 싶을 때 \n을 붙여야하지만
# "을 3번 붙이면 \n을 붙이지 않아도 엔터를 누르면 자동으로 줄바꿈이 됨

message3 = """My world is
best world"""

print(message3)

# len함수 : string의 길이
# "H" "e" "l" "l" "o" " " "W" "o" "r" "l" "d"총 11개 
message4 = "Hello World"

print(len(message4))

#0부터 시작하기 때문에 11번째 문자를 불러오고 싶으면 10을 불러오면됨
print(message4[10])

# [0:5]는 1번째 문자부터 6번째까지를 뜻함
# 처음부터 불러오는 것이면 0을 지우고 [:5]로 써도 됨
# 비슷하게 중간부터 마지막까지 불러오고 싶으면 뒤를 지우고 [6:]로 써도 됨
print(message4[0:5])

# .upper() : 모든 문자 대문자로
# .lower() : 모든 문자 소문자로
# .count(string) : 그 string이 message안에 얼마나 들어있는지 세줌
# .find(string) : 그 string이 message안에 몇 번째 index에 있는지 찾아줌, 없을 시 -1값 반환
print(message4.upper())

print(message4.lower())

print(message4.count("l"))

print(message4.find("World"))
print(message4.find("HyunKi"))

# .replace(바꾸고 싶은 string, 바꿀 string)

message5 = "Hello World"

message5.replace("World","Universe")

print(message5)