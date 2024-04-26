# 导入os模块
import os
# 导入time模块
import time


class File:
    def __init__(self):
        # 获取当前工作目录
        self.current_d = os.getcwd()
        self.files = os.listdir(self.current_d)

    # 文件备份
    def backup(self):
        old_name = input('请输入您要备份的文件名：\n')
        if old_name in self.files:
            timestamp = time.time()
            postfix_index = old_name.rfind('.')
            if postfix_index > 0:
                # 获取文件后缀
                postfix = old_name[postfix_index:]
                # 获取文件名
                new_name = old_name[:postfix_index] + '[备份]' + str(timestamp) + postfix
                # 在这里创建备份文件
                with open(os.path.join(self.current_d, old_name), 'r') as old_file:
                    content = old_file.read()
                    with open(os.path.join(self.current_d, new_name), 'w') as new_file:
                        new_file.write(content)
                print('文件备份成功，备份文件名为：', new_name)
            else:
                print('文件没有后缀，无法备份')
        else:
            print('文件不存在')

    # 删除文件
    def delete(self):
        name = input('请输入您要删除的文件名：\n')
        if name in self.files:
            os.remove(os.path.join(self.current_d, name))
            print('文件删除成功')
        else:
            print('文件不存在')

    # 创建文件
    def create(self):
        name = input('请输入您要创建的文件名：\n')
        if name not in self.files:
            content = input('请输入文件内容：\n')
            with open(os.path.join(self.current_d, name), 'w') as file:
                file.write(content)
            print('文件创建成功')
            # 更新文件列表
            self.files = os.listdir(self.current_d)
        else:
            print('文件已存在')

    # 重命名文件
    def rename(self):
        old_name = input('请输入您要重命名的文件名：\n')
        if old_name in self.files:
            new_name = input('请输入新的文件名：\n')
            os.rename(os.path.join(self.current_d, old_name),
                      os.path.join(self.current_d, new_name))
            print('文件重命名成功')
            # 更新文件列表
            self.files = os.listdir(self.current_d)
        else:
            print('文件不存在')


class Folder:
    def __init__(self):
        self.folder = os.getcwd()
        self.folders = os.listdir(self.folder)

    # 创建文件夹
    def create(self):
        name = input('请输入您要创建的文件夹名：\n')
        if name not in self.folders:
            os.mkdir(name)
            print('文件夹创建成功')
        else:
            print('文件夹已存在')

    # 删除文件夹
    def delete(self):
        name = input('请输入您要删除的文件夹名：\n')
        if name in self.folders:
            os.rmdir(name)
            del self.folders[name]
            print('文件夹删除成功')
        else:
            print('文件夹不存在')

    # 重命名文件夹
    def rename(self):
        old_name = input('请输入您要重命名的文件夹名：\n')
        if old_name in self.folders:
            new_name = input('请输入新的文件夹名：\n')
            os.rename(old_name, new_name)
            self.folders[new_name] = self.folders.pop(old_name)
            print('文件夹重命名成功')
        else:
            print('文件夹不存在')


file_manager = File()
folder_manager = Folder()

while True:
    print('\n请选择操作：')
    print('1. 创建文件')
    print('2. 备份文件')
    print('3. 删除文件')
    print('4. 重命名文件')
    print('5. 创建文件夹')
    print('6. 删除文件夹')
    print('7. 重命名文件夹')
    print('8. 退出')

    choice = input('请输入操作编号：')

    if choice == '1':
        file_manager.create()
    elif choice == '2':
        file_manager.backup()
    elif choice == '3':
        file_manager.delete()
    elif choice == '4':
        file_manager.rename()
    elif choice == '5':
        folder_manager.create()
    elif choice == '6':
        folder_manager.delete()
    elif choice == '7':
        folder_manager.rename()
    elif choice == '8':
        print('退出程序')
        break
    else:
        print('无效操作，请重新输入。')
