
# 진수 변환기

print("변환하고자 하는 진수법 2개를 입력해주세요 (2진수, 8진수, 10진수)")
print("예) 10 2 (10진수 -> 2진수)")

from_, to_ = map(int, input().split())

print("변환하고자 하는 값을 입력하세요")
val = int(input())

binary = ''
octal = ''
decimal = 0
hexadecimal = 0

def binary_number(to_, val):
    global decimal
    global octal
    tmp_arr = []

    if to_ == 8:
        # 2의 0승부터 3자리씩 잘라서 더해주는 방법
        while val != 0:
            bi = 1
            tmp = 0

            for _ in range(3):
                if val == 0:
                    break
                tmp += (bi * (val % 10))
                val //= 10
                bi *= 2
            tmp_arr.append(str(tmp))
        # 뒤에서부터 자릿수 만들기
        for num in tmp_arr[::-1]:
            octal += num
        return int(octal)

    elif to_ == 10:
        bi = 1
        # 2의 0승 자리부터 잘라서 더해주는 방법
        while val != 0:
            decimal += (bi * (val % 10))
            val //= 10
            bi *= 2
        return decimal

def octal_number(to_, val):
    global binary
    tmp_arr = []

    if to_ == 2:
        while val != 0:
            tmp = val % 10

            while tmp != 0:
                if tmp % 2 == 0:
                    tmp_arr.append('0')
                else:
                    tmp_arr.append('1')
                tmp //= 2
            val //= 10

            if len(tmp_arr) % 3 != 0:
                while len(tmp_arr) % 3 != 0:
                    tmp_arr.append('0')

        # 뒤에서부터 자릿수 만들기
        for num in tmp_arr[::-1]:
            binary += num
        return int(binary)

    elif to_ == 10:
        return binary_number(10, octal_number(2, val))

def decimal_number(to_, val):
    global binary
    tmp_arr = []

    if to_ == 2:
        while val != 0:
            if val % 2 == 0:
                tmp_arr.append('0')
            else:
                tmp_arr.append('1')
            val //= 2
        # 뒤에서부터 자릿수 만들기
        for num in tmp_arr[::-1]:
            binary += num
        return int(binary)

    elif to_ == 8:
        return binary_number(8, decimal_number(2, val))

if from_ == 2:
    result = binary_number(to_, val)
elif from_ == 8:
    result = octal_number(to_, val)
elif from_ == 10:
    result = decimal_number(to_, val)

print(result, end=' ')

if to_ == 2:
    print("(2)")
elif to_ == 8:
    print("(8)")
elif to_ == 10:
    print("(10)")
else:
    print("(16)")
