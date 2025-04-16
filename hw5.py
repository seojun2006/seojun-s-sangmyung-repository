def read_single_digit(digit):
    hangul_digits = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    return hangul_digits[int(digit)]

def read_number(num):
    for digit in num:
        print(read_single_digit(digit), end=' ')

num = input("세 자리 정수 입력: ")
read_number(num)
