in_str = input("2자리 숫자의 암호를 대시오! \n")

#print(type(in_str))
#change data type , match is neccessary

real_junwon = '11'
real_lee = "22"

if real_junwon == in_str or real_lee == in_str: #앞이 참이면 뒤에 코드는 실행안함
    print("Hello! You are right!!")
else:
    print("로그인 실패!")

