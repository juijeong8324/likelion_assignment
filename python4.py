grade_list = [60,40,30,50,25]
average = (60+40+30+50+25)/5
for i in grade_list:
    if i > average:
        print (f'{grade_list.index(i)+1}번째 학생 합격!')
    else:
        print (f'{grade_list.index(i)+1}번째 학생 불합격!')
