in_str = input("2자리 숫자의 암호를 대시오! \n")
#print(type(in_str))
#change data type , match is neccessary
real_junwon = '11'
real_lee = "22"
if real_junwon == in_str:
    print("Hello Junwon")
elif real_lee == in_str:
    print("Hello lee")
else:
    print("로그인 실패!")

