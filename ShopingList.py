# -*- coding:utf-8 -*-
# Author: Lightwing Ng


def formatNum(num):  # 1234 -> 1,234
    num = str(num)
    result = ''
    count = 0
    for i in num[::-1]:
        count += 1
        result += i
        if count % 3 == 0:
            result += ','
    return result[::-1].strip(',')


product_list = [
    ('iPhone X, 256GB', 5800),
    ('MacBook Pro 1TB', 18800),
    ('Apple Watch Top', 2588),
    ('Starbucks Coffee', 31),
    ('Python Tutorial', 120),
]
shopping_list = []

salary = input("Input your salary: ")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index, '\t', item[0], '\tCN￥', formatNum(item[1]))
        UserChoice = input(
            "May I know what you want to buy？\nPress q to quit>>>\t")
        if UserChoice.isdigit():
            UserChoice = int(UserChoice)
            if UserChoice < len(product_list) and UserChoice >= 0:
                p_item = product_list[UserChoice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart, your current balance is CN￥\033[31;1m%s\033[0m." % (
                        p_item[0], formatNum(salary)))
                else:
                    print("\033[41;1m你的余额只剩CN￥%s啦，还买个毛线\033[0m" %
                          formatNum(salary))
            else:
                print("product code [%s] is not exist!" % UserChoice)
        elif UserChoice == 'q':
            print("Your Shopping List:\t")
            print('\tITEMS:\t\t\t\tPrice\t\tNumbers')
            for p in shopping_list:
                print('\t', p[0], '\tCN￥', formatNum(p[1]), '\t1')
            print("\nYour current balance is CN￥", formatNum(salary), '.')
            exit()
        else:
            print("Invalid Option!")
