# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(phrases, second):
    # 여기에 코드를 작성해주세요.
    answer = ''

    tmp = "______________" + phrases + "_______________"
    length = 14 + len(phrases)
    a = second % length
    answer += tmp[a:a + 14]

    for i in range(1, second + 1):
        b = i % length
        print(tmp[b:b + 14])



    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")