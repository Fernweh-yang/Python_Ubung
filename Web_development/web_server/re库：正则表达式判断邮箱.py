import re

def main():
    email = input("请输入邮箱地址")
    ret = re.match(r"[a-zA-Z_0-9]*@163.com", email)
    if ret:
        print("%s符合要求。。" % email)
    else:
        print("%s不符合要求。。" % email)
if __name__ == "__main__":
    main()