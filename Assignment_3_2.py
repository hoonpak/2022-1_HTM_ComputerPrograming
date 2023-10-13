#input으로 값 받기
operation = input("어떤 연산을 수행할까요?(더하기, 빼기, 곱하기, 나누기 중 택1)>")
f_num = int(input("첫 번째 수를 입력하세요.>")) 
s_num = int(input("두 번째 수를 입력하세요.>"))

#if문을 활용해서 받은 사칙연산에 맞는 계산하기
if operation == "더하기":
    result = f_num + s_num
elif operation == "빼기":
    result = f_num - s_num
elif operation == "곱하기":
    result = f_num * s_num
elif operation == "나누기":
    result = f_num / s_num
else: # 사칙연산을 잘못 입력하였을 경우
    print("잘못 입력하셨습니다.")
    result = 0

#사직연산 결과 출력하기
print(f"입력값 = {f_num},{s_num}")
print("연산 종류:",operation)
print(f"연산 결과:{result:.2f}")#나누기의 경우 소수점이 무한대로 나올 수 있음으로 소수점 2번째짜리까지 출력