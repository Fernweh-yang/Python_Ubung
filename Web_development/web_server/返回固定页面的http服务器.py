import socket

def main():
    # 1. 买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2. 插入手机卡（绑定本地信息bind）
    tcp_server_socket.bind(("",7890))

    # 3.将手机设置为正常的响铃模式(让默认的套接字由主动变为被动listen)
    tcp_server_socket.listen(128)
    
    while True:
        print("等待一个新的客户端的到来...")
        # 4. 等待别人的电话到来(等待客户端的链接accept)
        client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来%s" % str(client_addr))
        
        
        #接收客户端发送过来的请求
        recv_data = client_socket.recv(1024)  #接受1024个字节的信息
        print("客户端发送过来的请求是%s" % recv_data.decode("gbk"))

        #如果recv解堵塞，那么有2种方式：
        # 1. 客户端发送过来的数据
        # 2. 客户端调用close导致
        #if  recv_data:
            #回送一部分数据给客户端
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        response += "徐大帅"
        client_socket.send(response.encode("gbk"))

        client_socket.close()
        print("本次服务已结束")

            #else:
                #break

        #关闭套接字
        

    tcp_server_socket.close()

if __name__ == "__main__":
    main()