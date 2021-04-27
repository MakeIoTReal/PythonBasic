log_count = 5

password = ['1234','9798']
while True:
    input_pw = input("password 입력하시오.\n")
    for pw in password:
        if input_pw == pw:
            print("반가워요 ")
            import sys
            sys.exit()
        if log_count==0:
            print("횟수 초과 Error\n")
            import sys
            sys.exit()

    print("로그인 가능 횟수: " + str(log_count)+" \n---------------\n")
    log_count = log_count - 1

