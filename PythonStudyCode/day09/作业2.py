# 4、简单购物车,要求如下：
# 实现打印商品详细信息，用户输入商品名和购买个数，
# 则将商品名，价格，购买个数以三元组形式加入购物列表，
# 如果输入为空或其他非法输入则要求用户重新输入　

msg_dic = {
    'apple': 10,
    'tesla': 100000,
    'mac': 3000,
    'lenovo': 30000,
    'chicken': 10,
}
product_list = []

while True:
    # 打印出可以购买的商品
    for key, value in msg_dic.items():
        # 1 使用%s进行输出信息
        # print("商品名称: %s, 商品价格: %s" % (key, value))
        # 2 使用format
        # print("商品名称: {},\t 商品价格: {}".format(key, value))
        # 3 使用f''
        print(f"商品名称: {key},\t 商品价格: {value}")

    # 1 name
    product_name = input("请输入购买的商品:").strip()
    if product_name not in msg_dic:
        print("商品不存在 请重新输入>")
        continue

    # 2 count
    product_count = input("请输入购买数量:").strip()
    if not product_count.isdigit():
        print("请输入商品数量>")
        continue

    if msg_dic.get(product_name):
        t = (product_name, msg_dic[product_name], int(product_count))
        product_list.append(t)
        print(product_list)
