import random
import sys
def get_random_number():
    random_num = random.randrange(100, 1000)
    if len(set(str(random_num))) == 3:
        return random_num
    else:
        return get_random_number()

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
        if user_input_number[0] == '0':
            return False
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
        return True
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
    
    while True:
        user_number = input('Input guess number : ')
        if user_number == str(0):
            break
        elif not is_validated_number(user_number):
            print('Wrong Input, Input again')
            continue
        else: # 사용자의 입력값이 유효하다면 
            result = get_strikes_or_ball(user_number, random_number)
            print(f"Strikes : {result[0]}, Balls : {result[1]}")
            if result[0] == 3:
                again = None
                while True:
                    again = input('You win, one more(Y/N)?')
                    if is_yes(again) or is_no(again): # T/F or F/T
                        break
                    else: # F/F
                        print('Wrong Input, Input again')
                
                if is_no(again):
                    break
                if is_yes(again):
                    random_number = str(get_not_duplicated_three_digit_number())
                    print("Random Number is : ", random_number)

    print("Thank you for using this program")
    print("End of the Game")