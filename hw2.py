# 입력받은 금액을 전달하받는 exchange() 함수의 정의 :
def exchange(amount) :
    # 입력받은 금액 중
    # n500 = 500원짜리가 몇 개 필요한지 찾기
    n500 = amount // 500
    amount %= 500
    
    # 나머지 금액 중
    # n100 = 100원짜리가 몇 개 필요한지 찾기
    n100 = amount // 100
    amount %= 100

    # 나머지 금액 중
    # n50 = 50원짜리가 몇 개 필요한지 찾기
    n50 = amount // 50
    amount %= 50

    # 나머지 금액 중
    # n10 = 10원짜리가 몇 개 필요한지 찾기
    n10 = amount // 10

    # 각 동전의 개수 출력
    print('> 500원 동전의 개수:', n500)
    print('> 100원 동전의 개수:', n100)
    print('> 50원 동전의 개수:', n50)
    print('> 10원 동전의 개수:', n10)

# 주 프로그램부
change = int(input('동전으로 교환하고자 하는 금액은? '))

exchange(change)

