time1 = input()
time2 = input()

time1 = list(map(int, time1.split(":")))
time2 = list(map(int, time2.split(":")))
result = []
for i in range(len(time2)):
  if time1[2-i] > time2[2-i]:
    if len(result) == 2:
      result.append(24-time1[2-i]+time2[2-i]) 
      break  
    result.append(60-time1[2-i]+time2[2-i]) 
    time2[1-i] -= 1
  else:
    result.append(time2[2-i]-time1[2-i])
if result[0] == 0 and result[1] == 0 and result[2] == 0:
  print("24:00:00")
else:
  for i in range(len(result)):
    print(str(result[2-i]).rjust(2,"0"),end="")
    if i-2 == 0:
      break
    print(":",end="")