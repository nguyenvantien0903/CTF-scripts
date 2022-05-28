from pwn import *


# s=process('./chall1')
s=remote('tjc.tf',31111)
cnt=1

while(True):
	print(s.recvuntil("routes:\n"))


	a=[[0 for x in range(1000)] for y in range(1000)]
	for i in range(0,21):
		for j in range(0,21):
			a[i][j]=999999999

	# for i in range(1,21):
	# 	for j in range(1,21):
	# 		print(a[i][j],end=" ")
	# 	print()

	for i in range(1,41):
		str1=s.recvline()[:-1].decode().split(" ")
		x=int(str1[0])
		y=int(str1[1])
		z=int(str1[2])
		a[x][y]=z
		a[y][x]=z
		print(str1)

	print("end")
	for k in range(0,21):
		for i in range(0,21):
			for j in range(0,21):
				if a[i][k] + a[k][j] < a[i][j]:
					a[i][j] = a[i][k] + a[k][j]

	print(s.recvuntil("answer:"))

	if a[0][20] == 999999999:
		s.sendline("-1")
		print(-1)
	else:
		s.sendline(str(a[0][20]))
		print(a[0][20])
	print(cnt)
	if cnt==50:
		print(s.recvline())
		print(s.recvline())
		print(s.recvline())
	cnt+=1