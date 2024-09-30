"""

editor : Kim Gwang=Jae
date : 2024-09-30

이 파이썬 파일은 사칙연산을 하는 계산기 클래스 Calculator 와 Calculator에 공학용 계산 기능을 추가한 EngineeringCalculator로 이루어져있다.
이 파이썬 파일은 주말 과제였고 꾀나 힘들었다.
Calculator 클래스의 add, subtract, multiply, divide 매서드는 사칙연산을 위한 매서드이다.
get_kwarg, prec, fl 는 사칙연산 매서드들의 코드에서 공통적으로 계속 쓰인 코드들은 매서드로 만들어 코드의 길이를 줄이고 보기 쉽게 정리하기 위해 만들었다.
divide 매서드는 0나누기 오류를 방지하는 코드가 들어가있다.
precision은 소수점 자릿수를 결정하는 입력이고 return_float는 결과를 실수(True) 혹은 정수형(False)으로 변환하는데 쓰이는 입력이다.
precision의 초기값은 0, return_float의 초기값은 False이다.

EngineeringCalculator는 Calculator의 확장 버전으로 공학계산 기능이 추가되어있다.
EngineeringCalculator의 매서드들은 대부분 math 라이브러리의 기능을 이용해 만들었고, 소수점 결정 기능과 실수형 변환 기능이 들어가있다.
"""

import math  # 곱셈, 나눗셈, 공학용 함수 작성용


class Calculator:
    def init(self, *args, **kwargs):
        pass

    # precision, return_float 값들 추출하는 매서드. r=precision, f=return_float
    def get_kwarg(self, **kwargs):
        r = 0   # precision의 기본값(소수점은 없다!)
        f = False   # return_float의 기본값(float가 아님!)
        for key, value in kwargs.items():
            if key == 'precision':
                r += value
            elif key == 'return_float':
                f = value
        return r, f

    # r=precision 에 맞춰 소수점을 맞춰주는 함수. 값을 문자열로 변환해서 0값을 소수점에 추가함
    def prec(self, result, r):

        #precision 값이 주어진다면 소수점 자릿수 맞추기 실행
        if r:
            result = round(result,r) # 소수점을 먼저 맞춤
            result = str(result) # 소수점 자릿수를 맞추기 위해 문자열 형태로 변환
            
            # 정수형이면 소수점 갯수만큼.0 을 붙임. 아니면 자릿수 맞춰서 0 붙임
            if result.find(".") == -1:
                result = result + '.' + r*'0'
            else:
                dot = result.find(".") # 점의 위치를 찾음
                zeros = len(result[dot+1:]) # 점의 위치로 뒤의 숫자가 몇개있는지 확인함
                result = result + (r-zeros)*"0" # 뒤의 숫자도 고려해 0붙이기
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

    """
    add, subtract, multiply, divide 매서드는 차례대로 덧셈, 뺄셈, 곱셈, 나눗셈을 처리하는 함수이다.
    위 매서드들은 *args을 써서 여러 숫자들을 입력으로 받는다.
    또한 **kwargs을 써서 조건을 지정해 줄 수 있다.
    
    사칙연산들은 이러한 순서로 동작한다.
    1.get_kwarg을 통해 초기조건들을 불러온다.
    2. 계산을 실시한다.
    3. prec을 통해 소수점 자릿수를 결정짓는다.
    4. fl을 통해 출력의 실수형, 정수형을 결정짓는다.
    5. 변환된 결과를 출력한다.
    
    """


    def add(self, *args, **kwargs):
        r, f = self.get_kwarg(**kwargs)

        result = sum(args)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result

    # args[0]은 처음 값, sum(args[1:])는 빼야할 값들의 합으로 퉁쳐서 뺌
    # 명확히 할려면 args[0] 대신 새로운 변수를 만들 수 있으나 매서드 입력의 통일성을 위해 *args, **kwargs로 통일함
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
    # 명확히 할려면 args[0] 대신 새로운 변수를 만들 수 있으나 매서드 입력의 통일성을 위해 *args, **kwargs로 통일함
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

class EngineeringCalculator(Calculator):
    def init(self, **kwargs):
        pass

    """
    square_root, power, log, ln, sin, cos, tan 매서드는 차례대로 제곱근, 거듭제곱, 로그, 자연로그, 사인, 코사인, 탄젠트을 처리하는 함수이다.
    위 매서드들은 x을 써서 숫자를 입력으로 받는다.
    power의 입력 y는 거듭제곱을 의미한다.
    또한 **kwargs을 써서 조건을 지정해 줄 수 있다. 
    sin, cos, tan 매서드는 angle_unit으로 입력값이 degree인지, raidans인지 표시해주는 키워드가 있으며 기본값은 degree이다.
    angle_raidans 매서드는 degree로 받은 입력x를 raidans으로 변환해주는 함수이다.
    
    
    매서드들은 이러한 순서로 동작한다.
    1.get_kwarg을 통해 초기조건들을 불러온다.
    1-2. sin, cos, tan은 angle_raidans 매서드를 거쳐 키워드를 통해 입력이 각도인지, 라디안인지 확인하고 각도이면 라디안으로 변환한다.
    2. 계산을 실시한다.
    3. prec을 통해 소수점 자릿수를 결정짓는다.
    4. fl을 통해 출력의 실수형, 정수형을 결정짓는다.
    5. 변환된 결과를 출력한다.
    """

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
    def log(self, x, **kwargs): 
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
    
    # 디그리로 설정된 각도(입력x)를 라디안으로 변환해 출력하는 매서드. 키워드 파라미터kwargs 를 이용한다.
    def angle_raidans(self,x, **kwargs):
        for key,value in kwargs.items():
            if key == 'angle_unit' and value == 'degree':
                x = math.radians(x)
            else : 
                pass
                
        return x

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
    

# 클래스 테스트용 코드
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