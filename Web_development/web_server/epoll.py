import socket
import re
import select

def service_client(new_socket, recv_data):
     
    #接收客户端发送过来的请求
    #recv_data = new_socket[0].recv(1024).decode("utf-8")  #接受1024个字节的信息
    #去掉换行
    recv_data_split = recv_data.splitlines()
    print(recv_data_split)
    #获取网页请求的文件名
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)",recv_data_split[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"
    
    try:
        f = open("./返回相应页面的http服务器" + file_name,"rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "---------file not found--------"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
         #发送给浏览器的数据 —— header
        response_body = html_content 

        response_header = "HTTP/1.1 200 OK\r\n"
        #长链接
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)


    
    #关闭套接字
    #new_socket[0].close()


def main():
    # 1. 买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2. 插入手机卡（绑定本地信息bind）
    tcp_server_socket.bind(("",7890))

    # 3.将手机设置为正常的响铃模式(让默认的套接字由主动变为被动listen)
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False) #改套接字为非堵塞

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)
    

    fd_event_dict = dict()

    while True:
        
        # 默认会堵塞，直到os监测到数据到来 通过事件通知的方式告知这个程序，此时才会解堵塞
        fd_event_list = epl.poll() 
        # epl.poll返回的是一个列表，里面包含2个元组
        # [(fd,event),(套接字对应的文件描述符，告知具体是什么事件，例如 可以调用recv接收等)
        for fd, event in fd_event_list:
            # 等待新的客户端到来
            if fd == tcp_server_socket.fileno()
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                #判断已经链接的客户端是否有数据发过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]
                    

    tcp_server_socket.close()

if __name__ == "__main__":
	main()