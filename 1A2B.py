import random
from typing import List


def create_ans() -> List[int]:
    source = [i for i in range(10)]
    while True:
        random.shuffle(source)
        ans_ls = source[:4]
        if ans_ls[0] != 0:
            break
    return ans_ls
    # First shuffle 10 numbers randomly from 0 to 9,
    # then we pick 4 numbers to obtain a answer_list
    # if the first element is '0',shuffle again


def check(input_ls: str) -> bool:
    if len(input_ls) != 4 or len(set(input_ls)) != 4:
        return True

    elif input_ls[0] == 0:
        return True

    elif input_ls.isdigit() == 0:
        return True

    else:
        return False
    # if input number doesn't follow game rule, return True to print error message


def compare(input_ls, ans_ls:List[int]) -> List[int]:
    result = [0, 0]
    for a in range(4):
        for b in range(4):
            if input_ls[a] == ans_ls[b]:
                if a == b:
                    result[0] += 1
                else:
                    result[1] += 1
    print(f"{result[0]}A{result[1]}B")

    return result
    # compare two list(ans and input),we could get result
    # result[0] == A,result[1] == B


def interact() -> str:
    print(
        "Please enter four number(first number can't be 0,other numbers range from 0 to 9)"
    )

    input_ls = input_function()

    return input_ls


def input_function() -> str:
    input_ls = input("Your answer is: ")
    return input_ls


if __name__ == "__main__":
    Error = "Invalid input,Please enter four number(first number can't be 0,other numbers range from 0 to 9)    "

    password = create_ans()

    while True:
        input_number = interact()

        if check(input_number) == True:
            print("\033[31m" + Error + "\033[0m")
            continue

        input_ls = list(map(int, input_number))

        result = compare(password, input_ls)
        if result[0] == 4:
            break

    print("Nice job!")
