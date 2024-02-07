
first=float(input("entaer the first number :"))
print("/")
print("*")
print('+')
print('-')
operator=input('select the operator :')
second=float(input('eter the second number :'))
def opration_performed(f_num,sec_num,operator):
    while True:
        if operator=='*':
            result=f_num*sec_num
        elif operator=='/':
            result=f_num/sec_num
        elif operator=='+':
            result = f_num + sec_num
        elif operator=='-':
            result=f_num-sec_num






opration_performed(first,second,operator)

