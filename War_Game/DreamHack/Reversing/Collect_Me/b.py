import re

# 입력 파일 이름과 출력 파일 이름 정의
input_file = "output.txt"
output_file = "output_1.txt"

# 정규 표현식 패턴 설정
pattern = r"'(.*?)'"

# 입력 파일을 읽고 출력 파일을 엽니다
with open(input_file, "r", encoding="utf-8") as infile:
    file_contents = infile.read()

# 정규 표현식을 사용하여 홑따옴표로 둘러싸인 문자열만 추출
extracted_strings = re.findall(pattern, file_contents)

# 추출된 문자열을 다시 조합하여 하나의 문자열로 만듭니다.
result_string = " ".join(extracted_strings)

# 출력 파일에 결과를 쓰기
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write(result_string)

print(f"홑따옴표로 둘러싸인 문자열만을 추출하여 '{output_file}'에 저장했습니다.")

