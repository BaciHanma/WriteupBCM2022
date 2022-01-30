from pwn import *
import math
io = remote('45.77.39.59',9004)
def solve(s):
    t = 1
    for i in set(s):
        t=t*math.factorial(s.count(i))
    return math.factorial(len(s))//t
io.recvline()
io.recvline()
io.recvline()
io.recvline()
io.recvline()
io.recvline()
io.recvline()
io.recvline()
while True:
    io.recvuntil(b'S = ')
    k = io.recvuntil(b'\n').decode('utf-8').replace('\n','')
    io.recvuntil( b'How many different strings can be generated from string S?\n')
    io.recvuntil(b'answer = ')
    resultT = f'{solve(k)}'
    io.send(resultT.encode())
io.interactive()
