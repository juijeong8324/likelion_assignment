# 소수 찾기
print(2) #2가 소수임을 알고 있다는 전제 하에 계산 
i=3
prime = [2]
for num in prime:
  while i < 100:
      if i % num != 0:
        prime.append(i)
        print(i)
        i=i+1
      else:
        i=i+1
        pass

