import socket

def main():
    # 1. 买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 插入手机卡（绑定本地信息bind）
    tcp_server_socket.bind(("",7890))

    # 3.将手机设置为正常的响铃模式(让默认的套接字由主动变为被动listen)
    tcp_server_socket.listen(128)

    # 4. 等待别人的电话到来(等待客户端的链接accept)
    # accept 返回一个有2个参数的元组
    # 第一个参数 表示新的套接字，其为客户服务，因为原来的套接字被用来接听客户了
    # 第二个参数 表示客户端的地址
    # 监听套接字 负责 等带有新的客户端进行链接
    # accept产生的新套接字 负责 通信服务
    client_socket, client_addr = tcp_server_socket.accept()
    print(client_addr)
    
    #接收客户端发送过来的请求
    recv_data = client_socket.recv(1024)  #接受1024个字节的信息
    print(recv_data)

    #回送一部分数据给客户端
    client_socket.send("xixi".encode("utf-8"))

    #关闭套接字
    client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()