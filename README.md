패키지 작성자 : 김광재

제작기한 : 2024-09-30 ~ 2024-10-01

파이썬 버전 : 3.11.9

<<<<<<< HEAD


calculator 패키지는 덧셈, 뺄셈, 곱셈, 나눗셈을 할 수 있는 basic.py 와 제곱근, 제곱, 로그, 삼각함수 계산이 추가된 engineering.py 와 basic.py, engineering.py 의 계산 기능을 보조하기 위한 utils.py 로 구성되어있습니다. ____init__.py 는 과제와 관련된 공지사항을 작성해둔 파일이라 동작은 하지 않습니다.

basic.py 내부에 있는 Calculator 클래스의 add, subtract, multiply, divide 매서드들은 사칙연산을 위한 매서드입니다. 각각 덧셈, 뺄셈, 곱셈, 나눗셈을 수행합니다.

engineering.py 내부에 있는 EngineeringCalculator 클래스의 square_root, power, log, ln, sin, cos, tan 매서드는 차례대로 제곱근, 거듭제곱, 로그, 자연로그, 사인, 코사인, 탄젠트를 수행하는 매서드입니다.

자세한 내용과 설명은 basic.py, engineering.py, utils.py 을 참고해주세요.
=======
이전에 계산기 과제를 작성한 코드들의 모음집입니다. 파이썬 함수와 모듈, 패키지를 공부하기 위한 과제이기도 합니다. 옛날에 한 과제 1, 2, 3번 과제를 한 뒤 4번 과제를 calculator 파일에 만들어 패키지를 만들었습니다. 이 코드 모음집은 작성한 과제 백업용이며 과제 작성 중 공부할 때 사용한 자료도 동봉되어있습니다. 



calculator 폴더는 덧셈, 뺄셈, 곱셈, 나눗셈을 할 수 있는 basic.py 와 제곱근, 제곱, 로그, 삼각함수 계산이 추가된 engineering.py 와 basic.py, engineering.py 의 계산 기능을 보조하기 위한 utils.py 로 구성되어있습니다. ____init__.py 는 과제와 관련된 공지사항을 작성해둔 파일이라 동작은 하지 않습니다. basic.py 내부에 있는 Calculator 클래스의 add, subtract, multiply, divide 매서드들은 사칙연산을 위한 매서드입니다. 각각 덧셈, 뺄셈, 곱셈, 나눗셈을 수행합니다.engineering.py 내부에 있는 EngineeringCalculator 클래스의 square_root, power, log, ln, sin, cos, tan 매서드는 차례대로 제곱근, 거듭제곱, 로그, 자연로그, 사인, 코사인, 탄젠트를 수행하는 매서드입니다. 자세한 내용과 설명은 basic.py, engineering.py, utils.py 을 참고해주세요.
2024_09_27_Calculator_homwork1,2,3.py 는 각각 과제 1,2,3번을 작성한 것입니다.
calculator.py 는 4번 과제 작성을 편하게 하기위해 작성한 파이썬 파일입니다.
calculaotr copy.py 는 calculator.py 의 백업용 파일입니다.
d.ipynb 은 딕셔너리 쌍 위치 바꾸기를 해설한 코드와 계산기를 만들때 사용한 코드의 초기모델을 기록한 파일입니다.
docstring_guide.py는 파이썬 문서화를 진행할 때 도움이 되는 자료들을 모아둔 파일입니다.
swap_dict_with_map_and_lambda.py 는 맵과 람다 함수로 딕셔너리 쌍 위치 바꾸는 코드를 작성한 파일입니다.
>>>>>>> 1e45f70 (갱신)

해당 패키지의 구조는 아래와 같습니다

calculator/

│

<<<<<<< HEAD
├── __init__.py

├── basic.py

├── engineering.py

├── utils.py
=======
├── calculator

│       ├── __init__.py

│       ├── basic.py

│       ├── engineering.py

│       ├── utils.py

│       └── README.md

├── 2024_09_27_Calculator_homework_1.py

├── 2024_09_27_Calculator_homework_2.py

├── 2024_09_27_Calculator_homework_3.py

├── calculator copy.py

├── calculator.py

├── d.ipynb

├── docstring_guide.py

├── git_commit_test.py

├── swap_dict_with_map_and_lambda.py

├── LICENSE
>>>>>>> 1e45f70 (갱신)

└── README.md


파이썬 클래스 및 모듈 사용법을 익히기 위한 과제 수행의 결과물입니다. 또한 *args, **kwargs 사용법을 익히기 위한 결과물이기도 합니다.

이틀만에 만든 코드라 버그가 있을 수 있습니다. 또한 출력 결과가 문자열, 정수형, 부동소수점 등등 조건에 따라 다르게 출력되기 때문에, 버그를 막기 위해서는 print문 안에서 사용하시길 권장드립니다.

해당 패키지는 영리, 비영리 목적으로 자유롭게 배포, 수정이 가능합니다. 단, 버그가 있다고 원작성자탓을 하시면 안됩니다.

이 패키지 파일은 아래의 요구사항을 충족하기 위해 만들어졌습니다.


1-`Calculator` 클래스를 만드세요. 이 클래스는 기본적인 산술 연산을 제공해야 합니다.

요구사항
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


2-`Calculator` 클래스를 상속받아 `EngineeringCalculator` 클래스를 만드세요. 이 클래스는 기본 계산기의 기능을 모두 포함하면서 추가적인 공학 계산 기능을 제공해야 합니다.

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


ex 추가사항
1. 타입 힌팅을 사용하여 모든 메서드와 함수의 입력 및 출력 타입을 명시하세요.
2. 두 계산기 클래스에 대한 간단한 문서화를 작성하세요. (클래스, 메서드, 예외 등)


3-앞서 만든 `Calculator`와 `EngineeringCalculator` 클래스를 사용하여 `calculator.py` 모듈을 만드세요.

요구사항:
1. `calculator.py` 파일을 생성하고 앞서 구현한 두 클래스를 이 파일에 포함시키세요.
2. 모듈 레벨에서 간단한 사용 예시를 포함하는 문서화 문자열(docstring)을 추가하세요.
3. `if __name__ == '__main__'` 블록을 사용하여 모듈이 직접 실행될 때 간단한 데모를 실행하도록 구현하세요. 이 데모는 각 계산기의 주요 기능을 보여주어야 합니다.
4. 모듈 내에 `__all__` 변수를 정의하여 외부에서 import * 를 사용할 때 노출될 이름들을 명시하세요.


4-앞서 만든 계산기 모듈을 확장하여 `calculator` 패키지를 만드세요.

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

calculator/

│

├── __init__.py

├── basic.py

├── engineering.py

├── utils.py

└── README.md


ex 추가사항

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
<<<<<<< HEAD

사용예시 
=================================================
from basic import Calculator 

a = Calculator()

from engineering import EngineeringCalculator

b = EngineeringCalculator()

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

=================================================

=======
>>>>>>> 1e45f70 (갱신)
