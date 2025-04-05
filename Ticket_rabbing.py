# selenium 是一个用于自动化Web应用测试的工具，但它也可以用于爬取网页内容、自动化表单提交、模拟用户交互等。它通过模拟真实用户在浏览器中的操作来实现这些功能
# webdriver作用：启动浏览器：例如 webdriver.Chrome() 启动 Chrome 浏览器。
# 控制浏览器：例如打开网页、刷新页面、关闭页面等。
# 模拟用户操作：例如点击按钮、输入文本、滚动页面等
# By.ID：通过元素的 id 属性定位。
# By.XPATH：通过 XPath 表达式定位。
# By.CSS_SELECTOR：通过 CSS 选择器定位。
# By.CLASS_NAME：通过元素的 class 属性定位。
# By.NAME：通过元素的 name 属性定位。
# By.LINK_TEXT：通过链接文本定位。
# By.PARTIAL_LINK_TEXT：通过部分链接文本定位。
# By.TAG_NAME：通过元素的标签名定位。
#抢票逻辑
from selenium import webdriver #浏览器
# 定位指定地方 点击 模拟人操作
from selenium.webdriver.common.by import By #根据什么定位
import time
from datetime import datetime
#创建浏览器对象
scan=webdriver.Edge()
#打开网站  get获取 获取浏览器地址
scan.get('https://product.suning.com/0000000000/12416207986.html#?safp=d488778a.SFS_10423397.17742927.1&ch=cu')
#可能需要扫码登录，设置一个等待时间
time.sleep(20)
# while True:
#     if datetime.now()>=datetime(2025,4,6,20,0,0):
#         print('到达抢购时间:',datetime.now())
#         点击立即购买 find寻找 element元素 方法 xpath  css js
#         两个值  第一个值 提取的方式 第二个值 具体的下xpath规则
#         scan.find_element(By.XPATH, '//*[@id="buyNowAddCart"]').click()  # 定位到“立即购买”,点击click
#         print('------------已经点击了，立即购买-------------')
#         time.sleep(3)
#         # 点击提交订单
#         scan.find_element(By.XPATH, '//*[@id="submit-btn"]').click()
#         print('---------提交订单执行完毕----------')
#
#         time.sleep(10000000)
#     else:
#         print('还没有到达抢购时间，当前时间：',datetime.now())

# 疑问：1.如果页面因为火爆出现加载错误怎么办，如何立刻刷新并且继续抢票，直到出现付款页面。2.如果点击立即购买后，出现了不是“提交订单的页面又该如何操作/
# 3.我手动填写后去到立即购买页面程序能继续执行吗。4.我在程序执行立即购买点击了立即购买，由于页面换了后续还能继续执行吗。5.
# 仅仅只有几种不同的页面，我能否让程序发现或者说判断我现在处于哪一个界面，如果程序识别后可以执行，立即执行后面的操作，如果判断值为
# 不认识的值就一直等待”
scan.find_element(By.XPATH, '//*[@id="buyNowAddCart"]').click()  # 定位到“立即购买”,点击click
print('------------已经点击了，立即购买-------------')
time.sleep(3)
# 点击提交订单
scan.find_element(By.XPATH, '//*[@id="submit-btn"]').click()
print('---------提交订单执行完毕----------')

time.sleep(10000000)