#!/usr/bin/python3
from pwn import *
context.log_level = 'debug'

def solve(Nums, target):
    l = 0
    r = len(Nums) - 1
    cnt = 0

    while(l < r):
        if(Nums[l] + Nums[r] == target):
            l += 1
            r -= 1
            cnt+=1
        elif(Nums[l] + Nums[r] < target):
            l+=1
        else:
            r-=1
    return bytes(str(cnt), 'utf-8')

def autoSolve():
    while(1):
        r.recvuntil(b'Nums = [')
        bl = r.recvline()[:-2].split(b', ')
        r.recvuntil(b'Target = ')
        target = int(r.recvline())
        nums = []
        for x in bl:
            nums.append(int(str(x, 'utf-8')))
        nums.sort()
        r.sendline(solve(nums, target))
    
r = remote('45.77.39.59', 9005)
r.recvuntil(b'Nums = [1,2], Target = 5 => Answer = 0\n\n')

print(autoSolve())