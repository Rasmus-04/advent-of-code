"""
Beräkna 1*2*3*4, …., hela vägen upp till 100 (multiplicera alltså alla heltal mellan 1 och 100, inklusive 100)
Beräkna också 2*4*6*8, …., hela vägen upp till 164 (multiplicera alltså vartannat heltal mellan 2 och 164, inklusive 164)
Dividera de två talen och avrunda till närmaste heltal
"""

summa1 = 1
summa2 = 1

for i in range(1, 101):
    summa1 *= i


for i in range(2, 165, 2):
    summa2 *= i

print(round(summa1 / summa2))

