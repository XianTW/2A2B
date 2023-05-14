import random
password = []
i = 1
A = 0
B = 0
Complete = True
Guess = True
Error = "Invalid input,Please enter four number(first number can't be 0,other numbers range from 0 to 9)"
password.append(random.randint(1,9))
while Complete:
    password.append(random.randint(0,9))
    if i == 1:
        if (password[i-1] == password[i]):
            password.pop()
        else:
            i += 1
    elif i == 2:
        if (password[i-1] == password[i]) or (password[i-2] == password[i]):
            password.pop()
        else:
            i += 1
    elif i == 3:
        if (password[i-1] == password[i]) or (password[i-2] == password[i]) or (password[i-3] == password[i]):
            password.pop()
        else:
            Complete = False
            password_str = [str(a) for a in password]

print("Please enter four number(first number can't be 0,other numbers range from 0 to 9)")
print(password_str)
while Guess:
    ans= input("Your answer: ")
    answer = list(ans)
    if ans.isdigit() != 1:
        print(Error)    
    elif(answer[0] == '0') or (answer.__len__()!=4):
        print(Error)
    else:
        for a in range(4):
            if answer[a] == password_str[a]:
                A += 1
        for b in range(4):
            for c in range(4):
                if (answer[b]==password_str[c])and(b!=c):
                    B += 1
        print(A,"A",B,"B")
        if A>=4:
            Guess = False
            print("Well done! You got it!")
        else:
            print("Try again!")
            A = 0;B = 0