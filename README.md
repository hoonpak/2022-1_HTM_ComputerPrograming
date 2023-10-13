# 2022-1_HTM_ComputerPrograming
2022학년도 1학기 HTM Computer Programing 수업에서 활용한 코드입니다.

## 과제 3

### 1. 문자열 다루기
아래 텍스트 중 가장 많이 사용된 알파벳이 무엇인지, 그리고 그 알파벳이 몇 번
사용되었는지 알아내는 프로그래밍을 작성하세요.
1) 단, 대 소문자는 구분하지 마세요. 즉, A 와 a 는 같은 a 로 간주합니다.
2) a 부터 z 까지 각각 몇 번씩 사용되었는지 확인하세요.
3) 가장 많이 사용된 알파벳과 그 숫자가 자동으로 출력되게 해 주세요. (max 
함수 이용)
4) 위 내용으로 코드를 작성하고 마지막 출력 내용은 아래와 같습니다.
가장 많이 사용된 알파벳은 * 이며 모두 ***번 사용되었습니다. (해당 * 부분
print 명령어로 값을 받아와서 자동 출력)
5) 주요 코드 라인 옆에 꼭 주석 처리(#)를 하여 설명을 달아 줍니다.
“I am honored to be with you today at your commencement from one of the finest 
universities in the world. I never graduated from college. Truth be told, this is the closest I’ve 
ever gotten to a college graduation. Today I want to tell you three stories from my life. That’s 
it. No big deal. Just three stories. The first story is about connecting the dots. I dropped out of 
Reed College after the first 6 months, but then stayed around as a drop-in for another 18 
months or so before I really quit. So why did I drop out?
It started before I was born. My biological mother was a young, unwed college graduate 
student, and she decided to put me up for adoption. She felt very strongly that I should be 
adopted by college graduates, so everything was all set for me to be adopted at birth by a 
lawyer and his wife. Except that when I popped out they decided at the last minute that they 
really wanted a girl. So my parents, who were on a waiting list, got a call in the middle of the 
night asking: “We have an unexpected baby boy; do you want him?” They said: “Of course.” 
My biological mother later found out that my mother had never graduated from college and 
that my father had never graduated from high school. She refused to sign the final adoption 
papers. She only relented a few months later when my parents promised that I would 
someday go to college.
And 17 years later I did go to college. But I naively chose a college that was almost as 
expensive as Stanford, and all of my working-class parents’ savings were being spent on my 
college tuition. After six months, I couldn’t see the value in it. I had no idea what I wanted to 
do with my life and no idea how college was going to help me figure it out. And here I was 
spending all of the money my parents had saved their entire life. So I decided to drop out and 
trust that it would all work out OK. It was pretty scary at the time, but looking back it was 
one of the best decisions I ever made. The minute I dropped out I could stop taking the 
required classes that didn’t interest me, and begin dropping in on the ones that looked 
interesting.”

### 2. Input을 받아서 사칙 연산 계산기 만들기
Input으로 연산법칙 설정 (더하기, 빼기, 곱하기, 나누기) 중 하나 선택
- 결과 예시
어떤 연산을 수행할까요? >
첫 번째 수를 입력하세요. >
두 번째 수를 입력하세요. >
- 출력 예시
****************************
입력값 = ,
연산 종류:
연산 결과:
****************************

### 3. < 컴퓨터가 생각한 임의의 수 맞히기 >
1) 정수 input을 받는다.
2) 컴퓨터가 1부터 input 받은 정수 사이에 임의의 숫자를 생성하도록 한다. (출력
하지 않음)
(아래와 같이 입력 받은 숫자를 기준으로 컴퓨터가 임의의 숫자를 생성해서
pc_num에 저장해 두도록 한다.)
import random
num = int(input("생각하는 범위의 숫자를 입력하세요. > "))
pc_num = random.randint(1, num)
3) 사용자가 임의의 수를 추정한다.
man_try = int(input("1부터 입력한 숫자 사이의 임의의 수를 설정하였습니다. 한 번
맞혀 보세요. > "))
4) 값이 다르면 컴퓨터가 적절한 정보를 출력한다.
값이 맞으면 정답 메시지를 출력한다.
- 결과 예시
생각하는 범위의 숫자를 입력하세요. >
1부터 입력한 숫자 사이의 임의의 수를 설정하였습니다. 한 번 맞혀 보세요. >
- 출력 예시 (다음 중 하나를 출력하고, 정답이 나올 때까지 반복함)
**은 정답이 아닙니다. 더 높여 보세요. / **은 정답이 아닙니다. 더 낮춰 보세요. / 
**이 정답입니다. 축하합니다!

## 과제 4
지난 번 과제 3에 대하여(아래 내용 참조), 주어진 조건에 따라 함수를 만들어 처리하여 주시기 바랍니다.

(아래 과제 3 내용)
아래 텍스트 중 가장 많이 사용된 알파벳이 무엇인지, 그리고 그 알파벳이 몇 번 사용되었는지 알아내는 프로그래밍을 작성하세요.
    1) 단, 대 소문자는 구분하지 마세요. 즉, A와 a는 같은 a로 간주합니다.
    2) a부터 z까지 각각 몇 번씩 사용되었는지 확인하세요 (a~z까지 각 횟수 출력)
    3) 가장 많이 사용된 알파벳과 그 숫자가 자동으로 출력되게 해 주세요.
    4) 위 내용으로 코드를 작성하고 마지막 출력 내용은 아래와 같습니다.
가장 많이 사용된 알파벳은 * 이며 모두 ***번 사용되었습니다. (해당 * 부분 print 명령어로 값을 받아와서 자동 출력) 
    5) 주요 코드 라인 옆에 꼭 주석 처리(#)를 하여 설명을 달아 줍니다.

“I am honored to be with you today at your commencement from one of the finest universities in the world. I never graduated from college. Truth be told, this is the closest I’ve ever gotten to a college graduation. Today I want to tell you three stories from my life. That’s it. No big deal. Just three stories. The first story is about connecting the dots. I dropped out of Reed College after the first 6 months, but then stayed around as a drop-in for another 18 months or so before I really quit. So why did I drop out?
It started before I was born. My biological mother was a young, unwed college graduate student, and she decided to put me up for adoption. She felt very strongly that I should be adopted by college graduates, so everything was all set for me to be adopted at birth by a lawyer and his wife. Except that when I popped out they decided at the last minute that they really wanted a girl. So my parents, who were on a waiting list, got a call in the middle of the night asking: “We have an unexpected baby boy; do you want him?” They said: “Of course.” My biological mother later found out that my mother had never graduated from college and that my father had never graduated from high school. She refused to sign the final adoption papers. She only relented a few months later when my parents promised that I would someday go to college.
And 17 years later I did go to college. But I naively chose a college that was almost as expensive as Stanford, and all of my working-class parents’ savings were being spent on my college tuition. After six months, I couldn’t see the value in it. I had no idea what I wanted to do with my life and no idea how college was going to help me figure it out. And here I was spending all of the money my parents had saved their entire life. So I decided to drop out and trust that it would all work out OK. It was pretty scary at the time, but looking back it was one of the best decisions I ever made. The minute I dropped out I could stop taking the required classes that didn’t interest me, and begin dropping in on the ones that looked interesting.”

### 1.
아래 생성되는 리스트를 이용하여, 위의 1) ~ 4) 를 만족하는 get_from_list 함수를 만드시기 바랍니다. 즉, 리스트와 반복문을 이용하는 함수를 만들어 주십시오. 그리고 마지막에 해당 함수를 호출함으로써 프로그램을 완성하여 주시기 바랍니다.
import string
alpha_list = list(string.ascii_lowercase)    # 초기 리스트
print(alpha_list)

get_from_list 함수 생성

함수 실행


### 2.
아래 생성되는 딕셔너리를 이용하여, 위의 1) ~ 4) 를 만족하는 get_from_dict 함수를 만드시기 바랍니다. 즉, 딕셔너리와 반복문을 이용하는 함수를 만들어 주십시오. 그리고 마지막에 해당 함수를 호출함으로써 프로그램을 완성하여 주시기 바랍니다.
import string
alpha_dict = dict.fromkeys(string.ascii_lowercase, 0)     # 초기 딕셔너리 (key는 알파벳, value는 counting 초기화)
print(alpha_dict)

get_from_dict 함수 생성


함수 실행



### 3.
heroes = ['Black Widow', 'Loki', 'Iron man', 'Wanda Maximoff', 'Black Panther', 'Doctor Strange', 'Winter Soldier', 'Thor']
villains = ['Thanos', 'Red Skull', 'Loki', 'Winter Soldier', 'Ultron', 'Hela', 'Dormammu']

villains 몇몇은 (예, 'Loki') 맘을 고쳐 먹고 착한 hero가 되었습니다. 그러므로 기존 villains 리스트 중에서 hero에 속하게 된 아이템들은 빼고 그 나머지로 다시 new_villains 리스트를 구성하는 프로그램을 작성해 주세요.



### 4.
Input을 받아서 사칙 연산 계산기 만들기
이것 역시 지난 과제 3 내용입니다. 네 가지 연산을 각각의 함수로 만들어 두되, 각 함수는 결과값을 리턴합니다.
조건에 따른 함수를 호출한 후 마지막에 출력 예시를 보여주는 프로그램을 만들어 주세요.


Input으로 연산법칙 설정 (더하기, 빼기, 곱하기, 나누기) 중 하나 선택
-	결과 예시
어떤 연산을 수행할까요? >
첫 번째 수를 입력하세요. >
두 번째 수를 입력하세요. >

-	출력 예시
****************************
입력값 =      ,
연산 종류:
연산 결과:
****************************

## 과제 5
지난 번 과제에서 사용된 text를 그대로 사용합니다. a~z까지의 각 알파벳이 텍스트 내에서 사용된 횟수를 막대 그래프로 표시하고, 그래픽 파일을 저장하는 프로그램을 작성합니다.

우선 아래 내용이 오기 전에 alpha_list와 count_list를 만드는 프로그램을 작성하기 바랍니다. (이전 과제 그대로 활용하면 됨)
그 후 아래와 같이 data frame을 만들고 그 data frame을 저장합니다. (df.to_csv 함수 이용)

    import pandas as pd
    import matplotlib.pyplot as plt
    data = {'alphabet':alpha_list, 'count':count_list}
    df = pd.DataFrame(data)
    df.to_csv("alphabet_list.csv")

그 다음 저장된 data frame을 다시 불러와서 막대 그래프를 만드는 프로그램을 이어서 작성하여 주시기 바랍니다.
필요한 타이틀을 넣고, 원하는 만큼 자유롭게 그래픽 효과를 사용해서 출력하기 바랍니다.
마지막에 그래픽 파일을 저장하는 것으로 끝납니다.

참고) 함수를 직접 정의해서 사용해도 됩니다.

