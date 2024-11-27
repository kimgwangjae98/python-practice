# import multiprocessing
# import threading
# import time
# import os


# # 텍스트 파일 생성 함수 (스레드 수 조정 가능)
# def create_text_files_abcd(file_count, process_name, max_threads):
#     # 스레드에서 실행할 작업
#     def worker(start, end):
#         for i in range(start, end):
#             filename = f"{process_name}_file_{i}.txt"  # 파일 이름
#             with open(filename, "w") as file:
#                 file.write("ABCD")  # 파일 내용 작성
#             print(f"{filename} 생성 완료")
#             time.sleep(0.1)  # 작업 딜레이

#     threads = []
#     files_per_thread = (
#         file_count + max_threads - 1) // max_threads  # 지정된 스레드 수로 분배(올림처리)
#     for i in range(max_threads):  # 입력받은 스레드 수만큼 생성
#         start = i * files_per_thread
#         end = min((i + 1) * files_per_thread, file_count)
#         if start >= end:  # 더 이상 할당할 작업이 없으면 중단
#             break
#         thread = threading.Thread(target=worker, args=(start, end))
#         threads.append(thread)
#         thread.start()

#     # 모든 스레드가 완료될 때까지 대기
#     for thread in threads:
#         thread.join()


# if __name__ == "__main__":
#     total_files = 100  # 생성할 총 파일 수
#     half_files = total_files // 2  # 두 프로세스에 나눌 파일 수

#     max_threads = 2  # 스레드 수를 조정하려면 여기 값을 변경
#     print(f"스레드 수: {max_threads}")

#     # 시작 시간 기록
#     start_time = time.time()

#     # 프로세스 생성
#     process1 = multiprocessing.Process(
#         target=create_text_files_abcd,
#         args=(half_files, "Process1", max_threads))
#     process2 = multiprocessing.Process(
#         target=create_text_files_abcd,
#         args=(half_files, "Process2", max_threads))

#     # 프로세스 시작
#     process1.start()
#     process2.start()

#     # 프로세스 종료 대기
#     process1.join()
#     process2.join()

#     # 종료 시간 기록
#     end_time = time.time()

#     # 총 소요 시간 출력
#     print(f"모든 파일 생성 완료! 실행 시간: {end_time - start_time:.2f}초")

import multiprocessing
import threading
import time
import os


# 텍스트 파일 생성 함수 (스레드 수 조정 가능)
def create_text_files_abcd(file_count, process_name, max_threads):
    # 스레드에서 실행할 작업
    def worker(start, end):
        for i in range(start, end):
            filename = f"{process_name}_file_{i}.txt"  # 파일 이름
            with open(filename, "w") as file:
                file.write("ABCD")  # 파일 내용 작성
            print(f"{filename} 생성 완료")
            time.sleep(0.1)  # 작업 딜레이

    threads = []
    files_per_thread = (
        file_count + max_threads - 1) // max_threads  # 지정된 스레드 수로 분배
    for i in range(max_threads):  # 입력받은 스레드 수만큼 생성
        start = i * files_per_thread
        end = min((i + 1) * files_per_thread, file_count)
        if start >= end:  # 더 이상 할당할 작업이 없으면 중단
            break
        thread = threading.Thread(target=worker, args=(start, end))
        threads.append(thread)
        thread.start()

    # 모든 스레드가 완료될 때까지 대기
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    total_files = 100  # 생성할 총 파일 수
    num_processes = 4  # 사용할 프로세스 수
    max_threads = 25  # 각 프로세스에서 사용할 최대 스레드 수

    # 시작 시간 기록
    start_time = time.time()

    # 파일을 프로세스 수로 분배
    files_per_process = (total_files + num_processes - 1) // num_processes

    # 프로세스 리스트
    processes = []
    for i in range(num_processes):
        start_file = i * files_per_process
        end_file = min((i + 1) * files_per_process, total_files)
        process_name = f"Process{i + 1}"
        process = multiprocessing.Process(
            target=create_text_files_abcd,
            args=(end_file - start_file, process_name, max_threads)
        )
        processes.append(process)
        process.start()

    # 모든 프로세스 종료 대기
    for process in processes:
        process.join()

    # 종료 시간 기록
    end_time = time.time()

    # 총 소요 시간 출력
    print(f"모든 파일 생성 완료! 실행 시간: {end_time - start_time:.2f}초")
