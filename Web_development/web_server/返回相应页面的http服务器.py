import socket
import re

def service_client(new_socket):
     
    #接收客户端发送过来的请求
    recv_data = new_socket[0].recv(1024).decode("utf-8")  #接受1024个字节的信息
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
        new_socket[0].send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
         #发送给浏览器的数据 —— header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"

        #将response的header发送给浏览器
        new_socket[0].send(response.encode("utf-8"))
        #将response的boy发送给浏览器
        new_socket[0].send(html_content)


    
    #关闭套接字
    new_socket[0].close()


def main():
    # 1. 买个手机（创建套接字）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2. 插入手机卡（绑定本地信息bind）
    tcp_server_socket.bind(("",7890))

    # 3.将手机设置为正常的响铃模式(让默认的套接字由主动变为被动listen)
    tcp_server_socket.listen(128)
    
    while True:
        #tcp_server_socket.accept()返回的是一个元组
        new_socket = tcp_server_socket.accept()
        service_client(new_socket)
        

    tcp_server_socket.close()

if __name__ == "__main__":
    main()