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