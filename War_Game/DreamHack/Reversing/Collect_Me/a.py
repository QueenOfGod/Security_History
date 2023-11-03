# 입력 파일 이름과 출력 파일 이름 정의
input_file = "collect_me.txt"
output_file = "output.txt"
keyword = "mov     [rbp+var_1],"  # 여기에 찾고자 하는 키워드를 입력하세요.

# 입력 파일을 읽고 출력 파일을 엽니다
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

with open(output_file, "w", encoding="utf-8") as outfile:
    # 입력 파일의 각 줄을 반복
    for line in lines:
        # 키워드가 줄에 포함되어 있는지 확인
        if keyword in line:
            # 키워드가 포함된 줄을 출력 파일에 복사
            outfile.write(line)

print(f"'{keyword}'를 포함하는 줄을 복사하여 '{output_file}'에 저장했습니다.")
