import os
import multiprocessing

def copy_files(q,file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    #print("=====>模拟复制，将%s 从%s ---->%s" % (file_name,old_folder_name,new_folder_name))
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    q.put(file_name)

def main():
    # 1. 获取用户要copy的文件夹名字
    old_folder_name = input("请输入要copy的文件夹的名字")

    # 2.创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取文件夹的所有文件的名字 
    file_names = os.listdir(old_folder_name)
    print(file_names)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)
    
    # 5. 创建一个队列
    q = multiprocessing.Manager().Queue()

    # 6. 向进程池中添加copy的任务
    for file_name in file_names:
        po.apply_async(copy_files, args=(q,file_name,old_folder_name,new_folder_name))
    
    po.close()
    #po.join()
    old_file_nums = len(file_names)
    new_file_nums = 0
    while True:
        file_name = q.get()
        new_file_nums += 1
        print("\r当前进度为 %.2f %%" % (new_file_nums*100/old_file_nums),end = "")
        if new_file_nums >= old_file_nums:
            break


if __name__ == "__main__":
    main()