id_str = input("아이디를 말하시오! \n")
pwd_str = input("비밀번호를 대시오! \n")
#print(type(in_str))
#change data type , match is neccessary

real_junwon = '11'
real_lee = "22"

junwon_pwd = 'wnsdnjs'
lee_pwd = 'fl'

if real_junwon == id_str and junwon_pwd == pwd_str: #앞이 참이면 뒤에 코드는 실행안함
    print("Hello! JJ")
elif real_lee == id_str and lee_pwd == pwd_str:
    print("Hello! LEE")
else:
    print("로그인 실패!")
'''
줄바꿈 문자열이
'''
"안녕하세요"
# 아이디와 비번 쌍을 메모리에 저장?