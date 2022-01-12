# @time: 2022/1/12 10:07 AM
# Author: pan
# @File: src.py
# @Software: PyCharm
"""
核心代码文件
"""
from db import db_handle
from lib import common
# 存储用户信息
user_data = []


# 注册功能
def register():
    """
    项目注册功能 如果已经注册提示已经注册
    密码需要两次输入的密码一致才可以
    :return:
    """
    while True:
        inp_name = input("请输入用户名:(输入q退出注册)").strip()
        if inp_name == "q" or inp_name == "Q":
            break

        # 判断用户名是否已经注册
        user_data = db_handle.select_user(inp_name)
        if user_data:
            print("该用户名已经注册，请重新输入用户名:")
            continue

        inp_pwd = input("请输入密码:(输入q退出注册)").strip()
        inp_re_pwd = input("请再次输入密码:(输入q退出注册)").strip()
        if inp_pwd == "q" or inp_pwd == "Q":
            break

        if inp_pwd == inp_re_pwd:
            # 密码一致 进行注册
            db_handle.add_user(inp_name, inp_pwd)
            print("恭喜您！ 注册成功")
            break
        else:
            print("两次输入的密码不一致，请重新输入!!!")
            continue


# 项目登录功能
def login():
    """
    用户进行登录 如果输入的用户名不在数据库 提示未进行注册
    登录成功 保存登录信息
    :return:
    """
    while True:
        inp_name = input("请输入用户名:").strip()
        db_user_data = db_handle.select_user(inp_name)
        # 判断数据库中有没有该用户信息
        if not db_user_data:
            print("用户名未注册！")
            continue

        inp_pwd = input("请输入用户密码:").strip()
        # 判断用户输入的用户名和密码是否都一致
        if inp_name == db_user_data[0] and inp_pwd == db_user_data[1]:
            print("登录成功!")
            # 如果一致 保存用户信息到全局变量
            global user_data
            user_data = db_user_data
            break
        else:
            print("账号或密码有误!!!")


# 充值功能
@common.login_auth
def recharge():
    while True:
        inp_money = input("请输入充值金额:").strip()
        if not inp_money.isdigit():
            print("输入的金额必须是数字!!!")
            continue
        # 1 旧数据
        name, pwd, balance = db_handle.select_user(user_data[0])
        old_data = f'{name}:{pwd}:{balance}\n'
        # 2 新数据
        balance = int(balance)
        balance += int(inp_money)
        new_data = f'{name}:{pwd}:{balance}\n'
        # 3 更新数据库中的数据
        db_handle.update_user(old_data, new_data)
        # 4 记录日志
        import time
        now_time = time.strftime('%Y-%m-%d %H:%M:%S')
        log_msg = f'用户:{user_data[0]}, 在:{now_time}, 进行了充值! 充值金额:{inp_money}\n'
        print(log_msg)
        common.logging(log_msg)
        break




# 阅读小说功能
@common.login_auth
def reader():
    print("""
    ================ 小说类别 ===============
    0 武侠小说
    1 玄幻小说
    2 都市言情
    ================== end =================
    """)
    while True:
        # 1) 选择小说类别
        type_cmd = input("请输入要看的小说类别:").strip()
        story_dic = db_handle.select_story_list()
        if type_cmd not in story_dic:
            print("请输入正确的小说类型！！！")
            continue
        # 2）获取对应小说类型的字典
        sub_story_dic = story_dic[type_cmd]
        for key in sub_story_dic:
            print(f'小说编号:{key},'
                  f'小说名字:{sub_story_dic[key][0]},'
                  f'小说价格:{sub_story_dic[key][1]}')

        # 3）输入要看的小说编号
        fiction_no = input("请输入要看的小说编号:").strip()
        if fiction_no not in sub_story_dic:
            print("请输入正确的小说编号!!!")
            continue
        fiction_name, fiction_price = sub_story_dic[fiction_no]

        # 4）输入小说编号之后询问是否是进行付费观看
        pay_cmd = input("是否进行付费观看(输入y或Y进行查看):").strip()
        if pay_cmd == "y" or pay_cmd == "Y":
            user_money = int(user_data[2])
            if user_money >= int(fiction_price):
                # 用户余额充足 进行扣费
                # 1 旧数据
                name, pwd, balance = db_handle.select_user(user_data[0])
                old_data = f'{name}:{pwd}:{balance}\n'
                # 2 新数据
                balance = int(balance)
                balance -= int(fiction_price)
                new_data = f'{name}:{pwd}:{balance}\n'
                # 3 更新数据库中的数据
                db_handle.update_user(old_data, new_data)
                # 4 记录日志
                import time
                now_time = time.strftime('%Y-%m-%d %H:%M:%S')
                log_msg = f'用户:{user_data[0]}, 在:{now_time}, 进行了消费! 消费金额:{fiction_price}\n'
                print(log_msg)
                common.logging(log_msg)
                # 5 扣费之后 查看小说内容
                fiction_content = db_handle.show_fiction_content(fiction_name)
                print(fiction_content)
                break
            else:
                print("用户余额不足,请先进行充值！！！")
                break


# 函数功能字典
func_dic = {
    "0": ["退出功能", exit],
    "1": ["账号注册", register],
    "2": ["账号登录", login],
    "3": ["充值功能", recharge],
    "4": ["阅读小说", reader]
}


def run():
    print("项目开始运行...")
    while True:
        print("=============  请选择项目功能  ===============")
        for key in func_dic:
            print(f'    {key}  {func_dic[key][0]}')
        print("==================  end  ====================")
        # 输入指令
        cmd = input("请输入指令：").strip()

        if cmd not in func_dic:
            print("请输入正确的指令!!!")
            continue
        # 指令正确运行功能
        func_dic[cmd][1]()

