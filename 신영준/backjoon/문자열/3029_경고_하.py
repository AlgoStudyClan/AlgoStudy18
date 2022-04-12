h1, m1, s1 = map(int, input().split(':')) # 현재 시간 입력
h2, m2, s2 = map(int, input().split(':')) # 던질 시간 입력

now = h1*60*60 + m1*60 + s1               # 현재 시간
throw = h2*60*60 + m2*60 + s2             # 던질 시간

time = throw - now if throw > now else throw - now + 24 * 60 * 60 # if문 3항 연산자
# 86400 = 60 * 60 * 24

h = time // 3600
m = time // 60 % 60
s = time % 60

print("%02d:%02d:%02d" % (h, m, s))