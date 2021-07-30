#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(a, b):
    # 여기에 코드를 작성해주세요.
    answer = 0
    prime = []
    cnt = set()

    for i in range(2, b + 1):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            prime.append(i)

    for i in prime:
        if (i**2) >= a and (i**2) <= b:
            cnt.add(i**2)
        if (i**3) >= a and (i**3) <= b:
            cnt.add(i**3)
    answer = len(cnt)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
a =  6
b =  30
ret = solution(a, b)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")