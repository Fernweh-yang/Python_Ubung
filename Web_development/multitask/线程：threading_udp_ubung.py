import socket
import threading

def recv(udp_socket):

    # 3. 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)

   
def send(udp_socket,dest_ip,dest_port):

    # 3. 发送数据
    while True:
        send_info = input("请输入要发送的数据：")
        udp_socket.sendto(send_info.encode("utf-8"),(dest_ip,dest_port))
    

def main():
    """聊天器的整体控制"""
    
    # 1. 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定port
    localaddr = ("",6789)
    udp_socket.bind(localaddr)

    # 3. 获取对方的ip和port
    dest_ip = input("请输入对方的ip")
    dest_port = int(input("请输入对方的port"))

    # 4. 创建2个线程，去执行相应的获取发送功能
    t_recv = threading.Thread(target=recv, args=(udp_socket,))
    t_send = threading.Thread(target=send, args=(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()

if __name__ == "__main__":
    main()