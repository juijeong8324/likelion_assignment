# 문제 1 주민번호
id_front = 20010821
id_back = 425048

age = id_front // 10000
birth = id_front % 10000
print (f'나이: {2020-age+1}')
print (f'생일: {str(birth)[:1]}월 {str(birth)[1:]}일')

gender = id_back//100000
if gender in [1,3]:
    print (f'성별: 남자')
elif gender in [2,4]:
    print (f'성별: 여자')
else:
    pass