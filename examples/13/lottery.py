# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 00:33:44 2020

@author: jh041
"""
# days_in_month = {
#     #여기에 코드를 완성해 보세요.
#     '1월': 31,
#     '2월': 28,
#     '3월': 31,
#     '4월': 30,
#     '5월': 31,
#     '6월': 30,
#     '7월': 31,
#     '8월': 31,
#     '9월': 30,
#     '10월': 31,
#     '11월': 30,
#     '12월': 31
    
#  }

# print(days_in_month)

# def check_and_clear(box):
#     print("불량품이 있으면 box를 clear합니다.")
#     if "불량품" in box.keys():
#         box.clear()
#     else:
#         print("{}:{}".format(box.keys(), box.values()))

# box1 = {"불량품" : 10}
# check_and_clear(box1)
# # {}가 출력되어야합니다.
# print(box1)

# box2 = {"정상품": 10}
# check_and_clear(box2)
# # {"정상품": 10}가 출력되어야합니다.
# print(box2)

products = {"풀":800, "딱풀":1200, "색종이":1000,"색연필":5000,"스케치북":3500}

catalog = {"겨울용 실내화":12000, "잠자리채":8000, "딱풀":1400}
products.update(catalog)

print(products)