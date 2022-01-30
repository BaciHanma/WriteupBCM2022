# WriteupBCM2022
Writeup của gà mờ
# 1.FIBONACCI
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

