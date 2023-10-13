import random #random 모듈을 불러오기

num = int(input("생각하는 범위의 숫자를 입력하세요.>")) #숫자 범위 입력 받기
pc_num = random.randint(1, num) #범위 안에 수 랜덤으로 뽑은 후 pc_num이라는 변수에 저장

man_try = 0 #man_try라는 변수 생성

while pc_num != man_try:#입력받은 수와 변수가 같지 않다면 반복, 일치할 경우 반복하지 않음
    man_try = int(input("1부터 입력한 숫자 사이의 임의의 수를 설정하였습니다. 한 번 맞혀 보세요.>"))#man_try라는 변수에 input값 입력받기.
    
    if pc_num > man_try:#사용자가 생각한 수가 랜덤으로 뽑힌 수 보다 더 작다면 높여보라는 메시지 출력
        print(f"{man_try}은 정답이 아닙니다. 더 높여 보세요.")
    elif pc_num < man_try:#사용자가 생각한 수가 랜덤으로 뽑힌 수 보다 더 크다면 낮춰보라는 메시지 출력
        print(f"{man_try}은 정답이 아닙니다. 더 낮춰 보세요.")
    else:#두 값이 일치할 경우 정답이라는 메시지 출력
        print(f"{man_try}은 정답입니다. 축하합니다!!")