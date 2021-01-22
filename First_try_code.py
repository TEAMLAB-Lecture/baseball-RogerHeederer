import random
import sys
def get_random_number():
    random_num = random.randrange(100, 1000)
    if len(set(str(random_num))) == 3:
        return random_num
    else:
        return get_random_number() #재귀 스택 쌓여서. 성능 면에서 좋지않다. 스택 프레임. while로 해결할 수 있으면 while로 해결. global (정적 메모리) . 멀티 스레드 사이에서 충돌 -> 정적 변수는 지양.  대신 파라미터와 리턴 값으로 해결


def get_not_duplicated_three_digit_number():
    #조건_ 입력값 없음 ok. 중복없는 숫자 세자리 정수값 ok. 반환타입 정수 ok.
    get_num = get_random_number() # 리턴값은 int
    return get_num

def is_digit(user_input_number): #인풋 문자열. 아웃풋 정수 TF
    if str(user_input_number).isdigit():
        return True
    else:
        return False

def is_between_100_and_999(user_input_number):
    if len(str(user_input_number)) == 3:
        return True
    else:
        return False

def is_duplicated_number(user_input_number):
    if len(set(str(user_input_number))) != 3: #중복될 경우
        return True
    else:
        return False    

def is_validated_number(user_input_number):
    
    if is_digit(user_input_number) and is_between_100_and_999(user_input_number) and not is_duplicated_number(user_input_number):
        global selected_number
        selected_number = user_input_number
        return True
    elif user_input_number == '0':
        print("Thank you for using this program
        print("End of the Game")
        exit()
    else:
        return False

def get_strikes_or_ball(user_input_number, random_number): # 문자열, 정수
    strike, ball= 0,0
    for i in range(3):
        if user_input_number[i] in str(random_number):
            if str(random_number).index(user_input_number[i]) == i:
                strike += 1
            else:
                ball += 1
        else:
            continue

    print(f"Strikes : {strike}, Balls : {ball}")
    return [strike, ball]

def is_yes(one_more_input):
    if one_more_input.isalpha() and one_more_input.lower() in ['yes', 'y']:
        return True
    else:
        return False

def is_no(one_more_input):
    if one_more_input.isalpha() and one_more_input.lower() in ['no', 'n']:
        return True
    else:
        return False

def main():
    print("Play Baseball") # 플래그 사용해서 새로운 게임시 스킵
    random_number = get_not_duplicated_three_digit_number() #정수값
    print("Random Number is : ", random_number)
    
    global selected_number #글로벌 변수는 전역,지역 전부 명시 필요
    selected_number = 0

    while not is_validated_number(input('Input guess number : ')):
        print("Wrong Input, Input again")
    
    while [3,0] != get_strikes_or_ball(selected_number, random_number):
        while not is_validated_number(input('Input guess number : ')):
            print("Wrong Input, Input again")

    retry_selection = input('You win, one more(Y/N)?')

    while is_yes(retry_selection) == False and is_no(retry_selection) == False:
        retry_selection = input('Wrong Input, Input again')


    if is_yes(retry_selection) == True and is_no(retry_selection) == False:
        return main()
    elif is_no(retry_selection) == True and is_yes(retry_selection) == False:
        print("Thank you for using this program
        print("End of the Game")
        return
    else:
        return

if __name__ == "__main__":
    main()