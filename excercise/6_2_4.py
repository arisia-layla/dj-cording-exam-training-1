# hello text
import random
def radomize():
    return random.randint(1, 6)
print("주사위 프로그램을 시작합니다. 첫 번째 숫자는")
print(radomize())
inpp = '1'
while True:
    inpp = input("아무키나 누르면 주사위가 던져집니다. 종료를 원하시면 'q'를 입력해주세요.")
    if inpp == 'q':
        break
    else:
        print(radomize())
