"""

editor : Kim Gwang=Jae
date : 2024-10-1

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
    """
    add, subtract, multiply, divide 매서드는 차례대로 덧셈, 뺄셈, 곱셈, 나눗셈을 처리하는 함수이다.
    위 매서드들은 *args을 써서 여러 숫자들을 입력으로 받는다.
    또한 **kwargs을 써서 조건을 지정해 줄 수 있다.
    kwargs에는 precision = int값, return_float = True or False 값을 사용하며 각각 소수점 자릿수, 출력의 실수형, 정수형을 결정하는 키워드입니다. 
    사칙연산들은 이러한 순서로 동작한다.
    1.get_kwarg을 통해 초기조건들을 불러온다.
    2. 계산을 실시한다.
    3. prec을 통해 소수점 자릿수를 결정짓는다.
    4. fl을 통해 출력의 실수형, 정수형을 결정짓는다.
    5. 변환된 결과를 출력한다.
    
    """
    def init(self, *args:int, **kwargs: dict[str : any]):
        pass

    # precision, return_float 값들 추출하는 매서드. r=precision, f=return_float
    def get_kwarg(self, **kwargs: dict[str : any])->any:
        """
        키워드 파라미터를 입력받아 precision의 값(정수), return_float의 값(부울)을 r, f 변수로 반환합니다.
        r=precision, f=return_float 입니다.
        precision의 기본값(소수점은 없다!)을 0으로 설정했습니다.
        return_float의 기본값(float가 아님!)을 False로 설정했습니다.
        add, subtract, multiply, divide 매서드 내부에서 동작하는 매서드입니다.
        """
        r = 0
        f = False
        for key, value in kwargs.items():
            if key == 'precision':
                r += value
            elif key == 'return_float':
                f = value
        return r, f

    # r=precision 에 맞춰 소수점을 맞춰주는 함수. 값을 문자열로 변환해서 0값을 소수점에 추가함
    def prec(self, result:float, r:int)->any:
        """
        get_kwarg에서 출력된 r값과 사칙연산을 거친 출력값result을 입력받아 r=precision 에 맞춰 소수점을 맞춰 반환합니다.
        result의 소수점 자릿수 갯수가 r=precision의 값보다 작으면 작은 만큼 0을 채워 넣어서 반환합니다.
        반환값은 int, float, str로 다양합니다. 
        add, subtract, multiply, divide 매서드 내부에서 동작하는 매서드입니다.
        
        먼저 r값이 존재한다면 round함수로 소수점을 맞춰줍니다. r값보다 result값의 소수점 자릿수가 많으면 잘라주는 역할을 합니다.
        그다음 소수점 자릿수를 맞추기 위해 result 형식을 문자열 형태로 변환합니다.
        
        이후 result값이 정수형이라면 '.'까지 붙여서 소수점 자릿수를 0으로 채워줍니다.
        정수형이 아닌 부동소수점 형식이라면 자릿수도 계산한 후 빈 소수점 자릿수를 0으로 채워줍니다.
        """
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

    def fl(self, result:float, f:bool)->float:
        """
        get_kwarg에서 출력된 f값과 사칙연산을 거친 출력값result을 입력받아 f=return_float 에 맞춰 소수점을 맞춰 반환합니다.
        f는 True or False 값을 가지며 True 값이면 입력 result를 부동소수점으로 변환하여 반환합니다. 아니면 그대로 반환합니다. 
        
        """
        if f:
            result = float(result)
        else:
            pass
        return result


    def add(self, *args:int, **kwargs: dict[str, any])->any:
        '''
        덧셈합을 계산하는 매서드. add(1,2,3) = 1+2+3 = 6 을 반환함
        '''
        r, f = self.get_kwarg(**kwargs)

        result = sum(args)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result


    def subtract(self, *args:int, **kwargs: dict[str, any])->any:
        '''
        args[0]은 처음 값, sum(args[1:])는 빼야할 값들의 합으로 퉁쳐서 뺌.
        subtract(10,2,3) = 10-2-3 = 5 을 반환함.
        명확히 할려면 args[0] 대신 새로운 변수를 만들 수 있으나 매서드 입력의 통일성을 위해 *args, **kwargs로 통일함
        '''
        r, f = self.get_kwarg(**kwargs)

        result = args[0] - sum(args[1:])
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result

    def multiply(self, *args:int, **kwargs: dict[str, any])->any:
        '''
        math.prod를 사용해서 곱셈합을 계산함. multiply(3,4,5) = 3*4*5 = 60을 반환함
        '''
        r, f = self.get_kwarg(**kwargs)

        result = math.prod(args)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result

    def divide(self, *args:int, **kwargs: dict[str, any])->any:
        '''
        math.prod(args[1:]) 로 나눌 값들의 곱셈을 계산해서 합치고 처음값 args[0]에 나눠버림
        divide(100,2,5,2) = 100/2/5/2 = 5 을 반환함
        명확히 할려면 args[0] 대신 새로운 변수를 만들 수 있으나 매서드 입력의 통일성을 위해 *args, **kwargs로 통일함        
        '''
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
    """
    EngineeringCalculator는 square_root, power, log, ln, sin, cos, tan 가 Calculator에 추가된 클래스이다.
    square_root, power, log, ln, sin, cos, tan 매서드는 차례대로 제곱근, 거듭제곱, 로그, 자연로그, 사인, 코사인, 탄젠트을 처리하는 함수이다.
    위 매서드들은 x을 써서 숫자를 입력으로 받는다.
    power의 입력 y는 거듭제곱을 의미한다.
    또한 **kwargs을 써서 조건을 지정해 줄 수 있다. 
    kwargs에는 precision = int값, return_float = True or False 값을 사용하며 각각 소수점 자릿수, 출력의 실수형, 정수형을 결정하는 키워드입니다. 
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
    def init(self, **kwargs):
        pass

    def square_root(self, x:float, **kwargs: dict[str, any])->any: 
        '''
        제곱근. x=16 이면 결과로 4를 반환합니다.
        square_root(16) = 4
        '''
        r, f = self.get_kwarg(**kwargs)

        result = math.sqrt(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
    def power(self, x:float, y:float, **kwargs: dict[str, any])->any: 
        '''
        거듭제곱. x^y 이며 x=2, y=3 이면 2^3=8을 반환합니다.
        power(2,3) = 8
        '''
        r, f = self.get_kwarg(**kwargs)

        result = math.pow(x,y)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
    def log(self, x:float, **kwargs: dict[str, any])->any:  
        '''
        로그. 밑이 10인 로그 매서드입니다. x=100 이면 log100=2를 반환합니다.
        log(100) = 2
        '''
        r, f = self.get_kwarg(**kwargs)

        result = math.log10(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
    def ln(self, x:float, **kwargs: dict[str, any])->any: 
        '''
        자연로그. 밑이 e인 자연로그 매서드입니다. x=e 이면 lne=1을 반환합니다.
        ln(1) = 0
        '''
        
        r, f = self.get_kwarg(**kwargs)

        result = math.log(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
    def angle_raidans(self, x:float, **kwargs: dict[str, any])->any: 
        '''
        디그리로 설정된 각도(입력x)를 라디안으로 변환해 출력하는 매서드. 키워드 파라미터kwargs 를 이용한다.
        angle_unit = 'degree' 키워드가 있으면 입력 x를 degree에서 라디안으로 변환한 값을 반환합니다.
        angle_raidans(180, angle_unit = 'degree') = pi
        '''
        for key,value in kwargs.items():
            if key == 'angle_unit' and value == 'degree':
                x = math.radians(x)
            else : 
                pass
                
        return x

    def sin(self, x:float, **kwargs: dict[str, any])->any: 
        '''
        사인. 각도 혹은 라디안 x를 입력하고 키워드로 angle_unit = 'degree' 가 입력되면 라디안 값으로 변환하여 sin값을 계산해 결과값을 반환합니다.
        sin(30, angle_unit = 'degree') = 0.5 을 반환합니다.
        '''
        r, f = self.get_kwarg(**kwargs)
        
        x=self.angle_raidans(x=x,**kwargs)

        result = math.sin(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
    def cos(self, x:float, **kwargs: dict[str, any])->any: 
        '''
        코사인. 각도 혹은 라디안 x를 입력하고 키워드로 angle_unit = 'degree' 가 입력되면 라디안 값으로 변환하여 cos값을 계산해 결과값을 반환합니다.
        cos(60, angle_unit = 'degree') = 0.5 을 반환합니다.
        
        '''
        r, f = self.get_kwarg(**kwargs)
        
        x=self.angle_raidans(x=x,**kwargs)
        
        result = math.cos(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    
    def tan(self, x:float, **kwargs: dict[str, any])->any: 
        '''
        탄젠트. 각도 혹은 라디안 x를 입력하고 키워드로 angle_unit = 'degree' 가 입력되면 라디안 값으로 변환하여 tan값을 계산해 결과값을 반환합니다.
        tan(0, angle_unit = 'degree') = 0
        '''
        r, f = self.get_kwarg(**kwargs)
        
        x=self.angle_raidans(x=x,**kwargs)

        result = math.tan(x)
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result
    

__all__ = ['Calculator', 'EngineeringCalculator']

if __name__ == '__main__':
    # 클래스 테스트용 코드
    print("Basic Calculator Demo:")
    calc = Calculator()
    print(calc.add(1, 2, 3, precision=2))  # 출력: 6.00
    print(calc.subtract(10, 2, 3, return_float=True))  # 출력: 5.0
    print(calc.multiply(2, 3, 4))  # 출력: 24
    print(calc.divide(100, 2, precision=3))  # 출력: 50.000

    print("\nEngineering Calculator Demo:")
    eng_calc = EngineeringCalculator()
    print(eng_calc.add(1, 2, 3, precision=2))  # 출력: 6.00
    print(eng_calc.square_root(16, precision=3))  # 출력: 4.000
    print(eng_calc.log(100, precision=4))  # 출력: 2.0000
    print(eng_calc.sin(30, angle_unit='degree', precision=4))  # 출력: 0.5000

    eng_calc.divide(5, 0) # 에러처리 확인용 코드


'''
# 문제 3: 계산기 모듈 만들기

앞서 만든 `Calculator`와 `EngineeringCalculator` 클래스를 사용하여 `calculator.py` 모듈을 만드세요.

요구사항:

1. `calculator.py` 파일을 생성하고 앞서 구현한 두 클래스를 이 파일에 포함시키세요.
2. 모듈 레벨에서 간단한 사용 예시를 포함하는 문서화 문자열(docstring)을 추가하세요.
3. `if __name__ == '__main__'` 블록을 사용하여 모듈이 직접 실행될 때 간단한 데모를 실행하도록 구현하세요. 이 데모는 각 계산기의 주요 기능을 보여주어야 합니다.
4. 모듈 내에 `__all__` 변수를 정의하여 외부에서 import * 를 사용할 때 노출될 이름들을 명시하세요.

예시:

```python
# calculator.py

class Calculator:
    # ... (이전에 구현한 내용)

class EngineeringCalculator(Calculator):
    # ... (이전에 구현한 내용)

__all__ = ['Calculator', 'EngineeringCalculator']

if __name__ == '__main__':
    # 간단한 데모 코드
    calc = Calculator()
    eng_calc = EngineeringCalculator()

    print("Basic Calculator Demo:")
    print(calc.add(1, 2, 3))
    print(calc.multiply(2, 4, 6))

    print("\\nEngineering Calculator Demo:")
    print(eng_calc.square_root(16))
    print(eng_calc.sin(30, angle_unit='degree'))

```

# 문제 4: 계산기 패키지 만들기

앞서 만든 계산기 모듈을 확장하여 `calculator` 패키지를 만드세요.

요구사항:

1. `calculator` 디렉토리를 만들고 그 안에 다음 파일들을 생성하세요:
    - `__init__.py`
    - `basic.py` (기본 계산기 클래스 포함)
    - `engineering.py` (공학용 계산기 클래스 포함)
    - `utils.py` (공통으로 사용되는 유틸리티 함수 포함)
2. `__init__.py`에서 필요한 클래스와 함수를 import하여 패키지 레벨에서 사용할 수 있게 만드세요.
3. `utils.py`에 다음 함수를 구현하세요:
    - `round_result(value, precision)`: 결과값을 지정된 정밀도로 반올림하는 함수
    - `convert_to_radians(angle, unit)`: 각도를 라디안으로 변환하는 함수
4. 각 모듈(`basic.py`, `engineering.py`, `utils.py`)에 적절한 문서화를 추가하세요.
5. 패키지의 루트 디렉토리에 `README.md` 파일을 생성하고, 패키지의 사용법과 예시를 포함한 기본적인 문서를 작성하세요.

예시 구조:

```
calculator/
│
├── __init__.py
├── basic.py
├── engineering.py
├── utils.py
└── README.md

```

# 추가 과제:

1. GitHub에 올릴 수 있는 형식으로 프로젝트를 구성하세요. 이는 다음을 포함해야 합니다:
    - 자세한 [README.md](http://readme.md/) 파일
    - LICENSE 파일
    - requirements.txt (필요한 경우)
    - [setup.py](http://setup.py/) 또는 pyproject.toml 파일 (패키지 설치를 위해)
    - .gitignore 파일
    - 테스트 디렉토리와 테스트 코드
2. 계산기 패키지에 복소수 연산 기능을 추가하세요. `ComplexCalculator` 클래스를 만들고 다음 연산을 구현하세요:
    - 복소수 덧셈, 뺄셈, 곱셈, 나눗셈
    - 복소수의 절대값 (magnitude) 계산
    - 복소수의 편각 (argument) 계산
    - 직교 좌표계와 극 좌표계 간의 변환
    이 기능을 패키지에 통합하고 적절한 문서화와 테스트를 추가하세요.

'''