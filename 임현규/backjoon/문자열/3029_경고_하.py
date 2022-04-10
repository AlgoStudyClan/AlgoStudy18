
import sys
input = sys.stdin.readline

hh1, mm1, ss1 = map(int, input().split(":"))
hh2, mm2, ss2 = map(int, input().split(":"))
h  = (hh2 - hh1)
m = (mm2 - mm1)
s = (ss2 - ss1)
if s < 0:
    m -= 1
    s += 60
if m < 0:
    h -= 1
    m += 60
if h < 0:
    h += 24

str_h = str(h).zfill(2)
str_m = str(m).zfill(2)
str_s = str(s).zfill(2)

print(f"{str_h}:{str_m}:{str_s}")
