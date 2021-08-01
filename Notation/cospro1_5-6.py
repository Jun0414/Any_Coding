#다음과 같이 import를 사용할 수 있습니다.
#import math

def two_sum(s1, s2, p):
    answer = ''
    plus = 0

    s1 = s1[::-1]
    s1 = change(s1, p, 10)
    
    s2 = s2[::-1]
    s2 = change(s2, p, 10)

    answer = str(int(s1) + int(s2))
    answer = answer[::-1]
    
    return answer

def change(result, p, q):
    total = 0
    answer = ''

    for i in range(len(result)):
        total += (p**i) * int(result[i])
    
    k = 0
    while True:
        if (q**k) < total:
            k += 1
        else:
            k -= 1
            break
    
    for i in range(k, -1, -1):
        answer += str(total // (q**i))
        total = total % (q**i)

    return answer

def solution(s1, s2, p, q):
    #여기에 코드를 작성해주세요.
    answer = ''
    
    result = two_sum(s1, s2, p)
    answer = change(result, 10, q)

    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "112001"
s2 = "12010"
p = 3
q = 8
ret = solution(s1, s2, p, q)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")