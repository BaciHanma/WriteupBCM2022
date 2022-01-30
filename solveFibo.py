from pwn import *
# Để có thể import pwn đầu tiên chúng ra cần phải install pwntools
# Bạn có thể thử lệnh "pip install pwntools"
io = remote('45.77.39.59',9001)
# Để kết nối tới máy chủ ta sử dụng lệnh remote(địa chỉ máy chủ, cổng kết nối )

cache = {}
# Để giải bài này mình sử dụng đệ quy kết hợp với một chút quy hoạch động
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n == 1 or n == 2:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result
        return result

io.recvuntil(b'Input N =')
#Lệnh io.recvuntil(chuoi can tim) dùng để đọc đến khi hết chuỗi cần tìm
io.recvuntil(b'\n')
while True:
    io.recvuntil(b'N = ')
    k = io.recvuntil(b'\n').decode('utf-8').split()
    #Nhớ là khi nhận chuỗi từ máy chủ về là chuỗi dạng byte phải decode('utf-8') để về chuỗi thường nhé 
    resultT = fibonacci(int(k[0]))
    io.sendline(str(resultT).encode())
    #Lệnh sendline() để gửi kết quả lại cho máy chủ
    #và nhớ là cũng phải encode(nghĩa là chuyển chuỗi thường về chuỗi byte )rồi gửi lại cho máy chủ
io.interactive()