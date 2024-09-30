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
            result = str(result)
            if result.find(".") == -1:
                # print("len = ", result.find("."))
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

        result = args[0] / math.prod(args[1:])
        result = self.prec(result=result, r=r)
        result = self.fl(result=result, f=f)

        return result


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