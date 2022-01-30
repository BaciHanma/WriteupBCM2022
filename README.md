# WriteupBCM2022
Writeup của gà mờ
# 1.FIBONACCI
![alt text](https://github.com/northern-cyber/WriteupBCM2022/blob/main/Fibonacci.png)

Đầu tiên, nếu bạn chưa biết thì để thực hiện các thử thách mảng programming đầu tiên chúng ta cần biết về socket. 

Mình cũng mới đọc về nó chút thôi.
Bạn có thể tham khảo ở link này:https://topdev.vn/blog/socket-la-gi-websocket-la-gi/ 


Hoặc với có kiến thức nông cạn của mình hiện tại chắc mình sẽ giải thích nó như này: để thực hiện các thử thách chúng ta kết nối đến các máy chủ, rồi các máy chủ
trả ra các vấn đề, ta giải quyết vấn đề rồi gửi kết quả lại cho máy chủ kiểm tra. Hiểu đơn giản vậy :D.

Vậy để kết nối đến các máy chủ phải làm sao?

__1. Khi sử dụng terminal__
Ta có thể sử dụng lệnh:
>nc {địa chỉ của máy chủ} {cổng mạng} 

__2. Hoặc ta có thể sử dụng các thư viện hỗ trợ của các ngôn ngữ lập trình__

Trong bài này và các bài sau, mình sẽ sử dụng python và cụ thể là thư viện pwn, hay còn biết đến với tên pwntool

Ok giờ vừa làm chall này rồi mình vừa giải thích nhé.

Đầu tiên khi ta kết nối tới với máy chủ với lênh:
>nc -v 45.77.39.59 9001

![alt text](https://github.com/northern-cyber/WriteupBCM2022/blob/main/terminal.png)

Có thể thấy chúng ta cần lấy được giá trị của N và gửi kết quả fibonacci(n) về cho máy chủ.

Đây là code mình thao tác và giải thích

```python
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
```
Sau đó chạy file py và nhận kết quả thôi:
>python3 solveFibo.py DEBUG

![alt text](https://github.com/northern-cyber/WriteupBCM2022/blob/main/fiboResult.png)

# 2.Product

![alt text](https://github.com/northern-cyber/WriteupBCM2022/blob/main/Product.png)

Yêu cầu: Bài này chỉ khác bài trên đầu vào là một mảng. Đừng suy nghĩ thuật toán phức tạp. Chỉ đơn giản là lấy tích cả mảng thôi. Đọc file solve ở dưới nhé.

![alt text](https://github.com/northern-cyber/WriteupBCM2022/blob/main/productTer.png)

Đây là file solve nhé:

[solvePro.py](https://github.com/northern-cyber/WriteupBCM2022/blob/main/solvePro.py)

Mình mới chỉ giải được 2 bài này thôi. Các bài sau mình tham khảo và đọc hint của các admin.

# 4.Permutation

![alt text](https://github.com/northern-cyber/WriteupBCM2022/blob/main/Permutation.png)

Yêu cầu: Tìm số chuỗi có thể tạo ra từ chuỗi đã cho.

![alt text](https://github.com/northern-cyber/WriteupBCM2022/blob/main/PermutationTer.png)

Để giải được bài này bạn có thể tham khảo hai nguồn sau:

https://vnhoctap.com/hoan-vi-lap/ (của admin __Lil Thawg__)

https://math.stackexchange.com/questions/2211509/how-many-different-strings-can-i-create-with-the-characters-of-the-string-speis (còn đây là nguồn mình đọc lúc giải bài)

Còn đây là code:

[solveLetter.py](https://github.com/northern-cyber/WriteupBCM2022/blob/main/SolveLetter.py)


# 5.SUM

![alt text](https://github.com/northern-cyber/WriteupBCM2022/blob/main/Sum.png)

Yêu cầu: Tìm số cặp có tổng bằng một giá trị cho trước.

![alt text](https://github.com/northern-cyber/WriteupBCM2022/blob/main/SumTer.png)

Để giải bài này bạn có thể đọc qua hai nguồn sau:

https://vnoi.info/wiki/algo/basic/two-pointers.md

https://www.geeksforgeeks.org/two-pointers-technique/

Còn đây là file solve:

[solveSum.py](https://github.com/northern-cyber/WriteupBCM2022/blob/main/SolveSum.py)

Cảm ơn các bạn đã đọc đến tận đây. Đây là lần đầu mình viết writeup nên chắc hơi dài dòng và giải thích có thể hơi mơ hồ.

