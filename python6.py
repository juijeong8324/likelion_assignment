my_dict = {"최정호":"010-6722-xxxx","송민선":"010-5029-xxxx","이종훈":"010-6335-xxxx","정재환":"010-8589-xxxx"}
who= input("찾고자 하는 사람을 입력하시오.\n")
if who in my_dict.keys():                                            
    print(f'{who}의 전화번호는 {my_dict[who]}입니다.')
else:
    print(f'{who}의 번호를 찾을 수 없습니다.')
