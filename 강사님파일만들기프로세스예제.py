import os
import random
import string

# 대형 파일 생성 함수 (랜덤 데이터 포함)


def create_large_file(file_path, size_gb):
    chunk_size = 1024 * 1024 * 10  # 10MB씩 쓰기
    total_size = size_gb * 1024 * 1024 * 1024  # GB를 바이트로 변환
    written = 0

    with open(file_path, "wb") as f:
        while written < total_size:
            # 10MB 크기의 랜덤 데이터를 생성하여 파일에 기록
            random_data = ''.join(random.choices(
                string.ascii_letters + string.digits,
                k=chunk_size)).encode('utf-8')
            f.write(random_data)
            written += chunk_size
            print(f"{written / (1024 * 1024):.2f} MB 생성 완료...", end="\r")

    print(f"\n파일 생성 완료: {file_path} ({size_gb}GB)")


# 소스 디렉토리 생성
source_dir = "source_files"
os.makedirs(source_dir, exist_ok=True)

# 대형 파일 생성 (각각 5GB)
file_count = 5
for i in range(1, file_count + 1):
    file_path = os.path.join(source_dir, f"large_file_{i}.dat")
    print(f"생성 중: {file_path}")
    create_large_file(file_path, 5)  # 각 파일 크기: 5GB
    print(f"완료: {file_path}")

print(f"총 {file_count}개의 대형 파일이 {source_dir} 폴더에 생성되었습니다.")
