from pwn import *
io = remote('45.77.39.59',9002)
io.recvuntil(b'arr =')
io.recvuntil(b'\n')
def product(arr):
    resultT = 1
    for i in arr:
        resultT = resultT * i
    return resultT
while True:
    io.recvuntil(b'arr = [')
    k = io.recvuntil(b']\n').decode('utf-8').split()
    k = str(k).replace("]","").replace('[','').replace(',','').replace("'",'').split()
    arr = [int(i) for i in k]
    io.sendline(str(product(arr)).encode())
print(arr)
io.interactive()