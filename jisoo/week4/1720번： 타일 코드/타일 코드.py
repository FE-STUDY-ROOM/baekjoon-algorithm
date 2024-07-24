tile_len = int(input()) 


d = [0 for _ in range(tile_len+1)]

d[0] = 1
d[1] = 1

n = 2
while n < tile_len +1: 
		#중복을 생각하지 않고 그냥 계산한 점화식
    d[n] = d[n-1] + 2*d[n-2]

    n += 1

if tile_len %2 == 0 :
    print((d[tile_len] + d[tile_len//2] + 2*d[(tile_len-2)//2])//2)
else:
    print((d[tile_len] + d[(n-1)//2] )//2) 