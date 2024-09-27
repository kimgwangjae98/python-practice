"""

작성자 : 김광재
날짜 : 2024.09.27

이 예제는 딕셔너리의 key값과 value값의 위치를 서로 바꾸는 함수이다. 

"""


def swap_dict(d):
    return dict(map(lambda t: (t[1], t[0]), d.items()))
original_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = swap_dict(original_dict)
print(swapped_dict)  # 출력: {1: 'a', 2: 'b', 3: 'c'}

'''
코드해석
dict() : 딕셔너리를 생성하는 함수. dict(1='a',2='b',3='c') -> {1: 'a', 2: 'b', 3: 'c'}
d.items() : d 라는 딕셔너리에서 key:value 값 쌍을 모두 출력함
d.items() = dict_items([('a', '1'), ('b', '2')]) -> 결국 리스트 형식으로 출력함.
map은 리스트를 입력받으면 리스트값들 하나씩 함수에 집어넣어줌.
lambda는 함수를 정의하며 입력: 출력 형식으로 사용함.
딕셔너리에 저장된 데이터 쌍을 람다 함수에 넘긴다. 람사 함수에선 key:value 쌍을 value:key로 뒤집는다
map 함수로 딕셔너리의 데이터 쌍들을 튜플 쌍으로 전부 바꾼다.
dict 함수를 사용해 튜플 쌍들을 딕셔너리로 변환한다.



https://tykimos.github.io/2020/01/01/Python_Lambda_Map/
이건 map이랑 lambda 설명 페이지
https://wikidocs.net/64

lambda 사용법
lambda 인자: 표현식
def is_even(x):  return x % 2 == 0
->
is_even = lambda x : x % 2 == 0
                인자(입력) : 표현식(출력)

def swap(t):
    return (t[1], t[0])
dict(map(swap(t), d.items()))
->
dict(map(lambda t: (t[1], t[0]), d.items()))

map 사용법
map(함수, 리스트나 튜플)
for문을 map 함수를 써서 간략화 시킬 수 있음
리스트나 튜플에서 받은 입력을 함수를 거치게 하여 리스트 혹은 튜플 형식으로 출력시킴

https://dotiromoook.tistory.com/28


myList = [1, 2, 3, 4, 5]

# for 반복문 이용
result1 = []
for val in myList:
    result1.append(val + 1)
print(f'result1 : {result1}')


# map 함수 이용
def add_one(n):
    return n + 1
result2 = list(map(add_one, myList))  # map반환을 list 로 변환
                    함수, 리스트
print(f'result2 : {result2}')

map은 리스트나 튜플과 함께 사용됨 - list(map(,))


def swap(t):
    return (t[1], t[0])
for key in d:
    swap(d.items(),)
    
dict(map(swap(t), d.items()))
->
def swap(t):
    return (t[1], t[0])
dict(map(swap(t), d.items()))
->
dict(map(lambda t: (t[1], t[0]), d.items()))


def swap_dict(d):
    return dict(map(lambda t: (t[1], t[0]), d.items()))
original_dict = {'a': 1, 'b': 2, 'c': 3}
swapped_dict = swap_dict(original_dict)
print(swapped_dict)  # 출력: {1: 'a', 2: 'b', 3: 'c'}



출처: https://blockdmask.tistory.com/531 [개발자 지망생:티스토리]


# 

'''




#딕셔너리 만들기
diction = { 'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6'}


# 새 딕션 생성
diction_reverse = {}

# key값과 value값 자리 바꾸기
for key in diction.keys():
    value = diction[key] # value값 얻기
    diction_reverse[value] = key # 자리바꾸기
print("diction = ", diction)
print("diction_reverse = ",diction_reverse)

def reverse(dicti):
    return dict(map(lambda r: (r[1],r[0]), dicti.items()))
diction_reverse = reverse(diction)
print(diction_reverse)

