import socket

def main():
    #1.创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    """ 
    #2.绑定一个本地信息,ip一般不用写表示本机任何一个IP，主要绑定端口
    localaddr = ("",7788)
    udp_socket.bind(localaddr)

    #3.接受数据
    recv_data = udp_socket.recvfrom(1024) #1024表示本次接收的最大字节数

    #4.打印接收到的数据
    print(recv_data)
    """
    
    #从键盘获取发送信息
    #send_info = input("请输入数据")
    
    #如果输入的数据是exit，那么退出程序
    #if send_info == "exit":
    #    break

    #可以使用套接字收发数据
    #udp_socket.sendto(byte类型的data,目标的ip和port)两种方法发送数据
    udp_socket.sendto(b"Ich liebe dich",("193.168.232.128",7788))
    #udp_socket.sendto(send_info.encode("utf-8"),("192.168.232.128"),7788)
   
    #关闭套接字
    udp_socket.close()

if __name__ == "__main__":
    main()
