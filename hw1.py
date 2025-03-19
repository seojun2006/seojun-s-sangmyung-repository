def get_circle_area(r) :
    area = f'반지름이 {r}인 원의 넓이: 3.14 x {r} x {r} = {3.14*r*r}'
    return area

input_r = int(input('넓이를 구하고자 하는 원의 반지름은? '))
result = get_circle_area(input_r)
print(result)
