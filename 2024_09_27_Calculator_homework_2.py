import math  # 곱셈, 나눗셈 함수 작성용


class Calculator:
    def init(self, *args, **kwargs):
        pass

    # precision, return_float 값들 추출하는 매서드. r=precision, f=return_float
    def get_kwarg(self, **kwargs):
        r = 0
        f = False
        for key, value in kwargs.items():
            if key == 'precision':
                r += value
            elif key == 'return_float':
                f = value
        return r, f

    # r=precision 에 맞춰 소수점을 맞춰주는 함수. 값을 문자열로 변환해서 0값을 소수점에 추가함
    def prec(self, result, r):

        if r:
            result = round(result,r)
            result = str(result)
            
            # 정수형이면 소수점 갯수만큼.0 을 붙임
            if result.find(".") == -1:
                result = result + '.' + r*'0'

            else:
                dot = result.find(".")
                # print(dot)
                zero = len(result[dot+1:])
                # print("zero_number = ", zero)
                result = result + (r-len(result[dot+1:]))*"0"
        else:
            pass
        return result

    # float 변환 함수. f=Ture이면 float로 변환
    def fl(self, result, f):
        if f:
            result = float(result)
        else:
            pass
        return result

    def add(self, *args, **kwargs):
        r, f = self.get_kwarg(**kwargs)

        result = sum(args)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result

    # args[0]은 처음 값, sum(args[1:])는 빼야할 값들의 합으로 퉁쳐서 뺌
    def subtract(self, *args, **kwargs):
        r, f = self.get_kwarg(**kwargs)

        result = args[0] - sum(args[1:])
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result

    # math.prod를 사용해서 곱셈합을 계산함
    def multiply(self, *args, **kwargs):
        r, f = self.get_kwarg(**kwargs)

        result = math.prod(args)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result

    # math.prod(args[1:]) 로 나눌 값들의 곱셈을 계산해서 합치고 처음값 args[0]에 나눠버림
    def divide(self, *args, **kwargs):
        r, f = self.get_kwarg(**kwargs)

        # 0나누기 오류 발생시 에러났다고 표시
        try:
            result = args[0] / math.prod(args[1:])
            result = self.prec(result=result, r=r)
            result = self.fl(result=result, f=f)
            return result
        except ZeroDivisionError as e:
            print(" 에러났습니다 : ",e)  # 출력: "Division by zero is not allowed"


        
'''
if self . second == 0 : •— 나누는 값이 0 인 경우 숫자 0을 돌려주도록 수정
re t urn 0
else :
ret urn self . fi rst / self . second
끝값을 처리하도록 만들면됨. 잘 할수있다.
try:
    print(eng_calc.divide(5, 0))
except DivisionByZeroError as e:
    print(e)  # 출력: "Division by zero is not allowed"
'''


class EngineeringCalculator(Calculator):
    def init(self, **kwargs):
        pass

    #  제곱근
    def square_root(self, x, **kwargs):
        r, f = self.get_kwarg(**kwargs)

        result = math.sqrt(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
   #  거듭제곱
    def power(self, x, y, **kwargs): 
        r, f = self.get_kwarg(**kwargs)

        result = math.pow(x,y)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
    # 로그 (기본값은 상용로그)
    def log(self, x, base=10, **kwargs): 
        r, f = self.get_kwarg(**kwargs)

        result = math.log10(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
        # 자연로그
    def ln(self, x, **kwargs):  
        r, f = self.get_kwarg(**kwargs)

        result = math.log(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
    def angle_raidans(self,x, **kwargs):
        for key,value in kwargs.items():
            if key == 'angle_unit' and value == 'degree':
                x = math.radians(x)
            else : 
                pass
                
        return x
    #angle_unit='degree'
       # 사인
    def sin(self, x, **kwargs):  
        r, f = self.get_kwarg(**kwargs)
        
        x=self.angle_raidans(x=x,**kwargs)

        result = math.sin(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
       # 코사인
    def cos(self, x, **kwargs):  
        r, f = self.get_kwarg(**kwargs)
        
        x=self.angle_raidans(x=x,**kwargs)
        
        result = math.cos(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
       #  탄젠트
    def tan(self, x, **kwargs): 
        r, f = self.get_kwarg(**kwargs)
        
        x=self.angle_raidans(x=x,**kwargs)

        result = math.tan(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    

    
"""
if self . second == 0 : •— 나누는 값이 0 인 경우 숫자 0을 돌려주도록 수정
re t urn 0
else :
ret urn self . fi rst / self . second

"""
    
"""
ture면 가급적 flaot,
false 면 정수형이면 int 아니면 float
pre는 없으면 정수형으로
있으면 float형으로

flaot pre -> 자릿수 맞춰서 반환. 자릿수 맞춰서 0 추가
float non -> float
ture pre -> 소수점 반환. float. 자릿수 맞춰서 0 추가
ture non -> int 반환

"""


"""
   - `add(*args, **kwargs)`: 덧셈
   - `subtract(*args, **kwargs)`: 뺄셈
   - `multiply(*args, **kwargs)`: 곱셈
   - `divide(*args, **kwargs)`: 나눗셈

"""
calc = Calculator()
print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
print(calc.multiply(2, 3, 4))  # 출력: 24
print(calc.divide(100, 2, precision=3))  # 출력: 50.000

eng_calc = EngineeringCalculator()
print(eng_calc.add(1, 2, 3, precision=2))  # 출력: 6.00
print(eng_calc.square_root(16, precision=3))  # 출력: 4.000
print(eng_calc.log(100, precision=4))  # 출력: 2.0000
print(eng_calc.sin(30, angle_unit='degree', precision=4))  # 출력: 0.5000

eng_calc.divide(5, 0)
# try:
#     print(eng_calc.divide(5, 0))
# except DivisionByZeroError as e:
#     print(e)  # 출력: "Division by zero is not allowed"


"""
6.00
5.0
24
50.000
6.00
4.000
2.0000
0.5000

"""

"""

문제 1: 기본 계산기 클래스 구현

`Calculator` 클래스를 만드세요. 이 클래스는 기본적인 산술 연산을 제공해야 합니다.

요구사항:
1. 다음 메서드를 구현하세요:
   - `add(*args, **kwargs)`: 덧셈
   - `subtract(*args, **kwargs)`: 뺄셈
   - `multiply(*args, **kwargs)`: 곱셈
   - `divide(*args, **kwargs)`: 나눗셈

2. 각 메서드는 위치 인자(`*args`)와 키워드 인자(`**kwargs`)를 받아야 합니다.

3. `**kwargs`에는 다음 키를 사용할 수 있어야 합니다:
   - `precision`: 결과의 소수점 자릿수 지정 (기본값: None, 즉 반올림하지 않음)
   - `return_float`: True일 경우 항상 float 타입 반환, False일 경우 가능하면 int 반환 (기본값: False)

4. 0으로 나누기 등의 에러 상황을 적절히 처리해야 합니다.

예시 사용법:
```python
calc = Calculator()
print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
print(calc.multiply(2, 3, 4))  # 출력: 24
print(calc.divide(100, 2, precision=3))  # 출력: 50.000
```

문제 2: 공학용 계산기 클래스 구현

`Calculator` 클래스를 상속받아 `EngineeringCalculator` 클래스를 만드세요. 이 클래스는 기본 계산기의 기능을 모두 포함하면서 추가적인 공학 계산 기능을 제공해야 합니다.

요구사항:
1. `Calculator` 클래스의 모든 메서드를 상속받으세요.

2. 다음 새로운 메서드를 추가하세요: --> 덮어쓰기
   - `square_root(x, **kwargs)`: 제곱근
   - `power(x, y, **kwargs)`: 거듭제곱
   - `log(x, base=10, **kwargs)`: 로그 (기본값은 상용로그)
   - `ln(x, **kwargs)`: 자연로그
   - `sin(x, **kwargs)`: 사인
   - `cos(x, **kwargs)`: 코사인
   - `tan(x, **kwargs)`: 탄젠트

3. 모든 메서드는 `**kwargs`를 통해 `precision`과 `return_float` 인자를 받아야 합니다.

4. `divide` 메서드를 오버라이드하여, 0으로 나누려고 할 때 사용자 정의 예외 `DivisionByZeroError`를 발생시키세요.

5. 각 삼각함수 메서드에 `angle_unit` 키워드 인자를 추가하여 'degree' 또는 'radian' 단위로 입력을 받을 수 있게 하세요. 기본값은 'radian'으로 설정하세요.

예시 사용법:
```python
eng_calc = EngineeringCalculator()
print(eng_calc.add(1, 2, 3, precision=2))  # 출력: 6.00
print(eng_calc.square_root(16, precision=3))  # 출력: 4.000
print(eng_calc.log(100, precision=4))  # 출력: 2.0000
print(eng_calc.sin(30, angle_unit='degree', precision=4))  # 출력: 0.5000
try:
    print(eng_calc.divide(5, 0))
except DivisionByZeroError as e:
    print(e)  # 출력: "Division by zero is not allowed"
```

추가 과제:
1. 타입 힌팅을 사용하여 모든 메서드와 함수의 입력 및 출력 타입을 명시하세요.
2. 두 계산기 클래스에 대한 간단한 문서화를 작성하세요. (클래스, 메서드, 예외 등)

"""