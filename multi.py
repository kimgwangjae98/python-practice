import multiprocessing
import threading
import time


# 제곱을 계산하는 함수
def calculate_square(numbers):
    # 스레드에서 실행할 작업
    def worker(num):
        print(f"Square: {num * num}")  # 제곱 결과 출력
        time.sleep(1)  # 작업 딜레이 (1초)

    threads = []
    # 숫자마다 스레드 생성 및 시작
    for n in numbers:
        thread = threading.Thread(target=worker, args=(n,))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 완료될 때까지 대기
    for thread in threads:
        thread.join()


# 세제곱을 계산하는 함수
def calculate_cube(numbers):
    # 스레드에서 실행할 작업
    def worker(num):
        print(f"Cube: {num ** 3}")  # 세제곱 결과 출력
        time.sleep(1)  # 작업 딜레이 (1초)

    threads = []
    # 숫자마다 스레드 생성 및 시작
    for n in numbers:
        thread = threading.Thread(target=worker, args=(n,))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 완료될 때까지 대기
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]  # 처리할 숫자 목록

    # 각 작업을 처리하는 프로세스 생성
    process1 = multiprocessing.Process(
        target=calculate_square, args=(numbers,))  # 프로세스 1: 제곱 계산
    process2 = multiprocessing.Process(
        target=calculate_cube, args=(numbers,))  # 프로세스 2: 세제곱 계산

    # 프로세스 시작
    process1.start()  # 프로세스 1 실행
    process2.start()  # 프로세스 2 실행

    # 프로세스 종료 대기
    process1.join()  # 프로세스 1이 끝날 때까지 대기
    process2.join()  # 프로세스 2가 끝날 때까지 대기

    print("멀티프로세싱 및 멀티스레딩 실행 완료!")  # 모든 작업 완료
