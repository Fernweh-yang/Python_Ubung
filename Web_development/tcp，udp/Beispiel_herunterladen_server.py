import socket

def main():
    # 1. 买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. 插入手机卡（绑定本地信息bind）
    tcp_server_socket.bind(("",7890))

    # 3.将手机设置为正常的响铃模式(让默认的套接字由主动变为被动listen)
    tcp_server_socket.listen(128)   #128这个数值主要影响同时可以访问的客户端数

    while True:

        # 4. 等待别人的电话到来(等待客户端的链接accept)
        client_socket, client_addr = tcp_server_socket.accept()
        print(client_addr)
        
        # 5. 发送文件给客户端
        send_file_to_client(client_socket,client_addr)

        # 6. 关闭套接字
        client_socket.close()
    tcp_server_socket.close()

def send_file_to_client(new_socket,new_addr):

    # 1. 接收客户端发送过来的，要下载的文件名
    file_name = new_socket.recv(1024).decode("utf-8") 
    print("客户端（%s）需要下载的文件是：%s"% (str(new_addr),file_name))

    file_content = None
    # 2. 打开这个文件，获取数据
    try:
        f = open(file_name,"rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)

    # 3. 发送文件的数据给客户端
    if file_content:
        #new_socket.send("徐大侠天下第一帅".encode("utf-8"))
        new_socket.send(file_content)

if __name__ == "__main__":
    main()