from urllib.request import urlopen
from bs4 import BeautifulSoup
import itchat as ic
import time, re, datetime
from wxpy import *
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def getWeather():
    # 使用BeautifulSoup获取天气信息
    resp = urlopen('http://www.weather.com.cn/weather/101230201.shtml')
    soup = BeautifulSoup(resp, 'html.parser')
    tagDate = soup.find('ul', class_="t clearfix")
    dates = tagDate.h1.string
    tagToday = soup.find('p', class_="tem")
    try:
        temperatureHigh = tagToday.span.string
    except AttributeError as e:
        temperatureHigh = tagToday.find_next('p', class_="tem").span.string
    temperatureLow = tagToday.i.string
    weather = soup.find('p', class_="wea").string
    tagWind = soup.find('p', class_="win")
    winL = tagWind.i.string
    content = '早上好，宝宝！\n 今日份厦门市天气请注意查收：\n' + '今天是：' + dates + '\n' + '风级：' + winL + '\n' + '最低温度：' + temperatureLow + '\n' + \
              '最高温度：' + temperatureHigh + '\n' + '天气：' + weather + '\n'
    return content

def main():
    try:
        msg = getWeather()
        print('成功获取天气信息')
    except:
        msg = ""
        print("获取天气信息失败")
    # 参数hotReload=True实现保持微信网页版登陆状态，下次发送无需再次扫码
    # ic.auto_login()
    # users = ic.search_friends(name = '测试')
    # userName = users[0]['UserName']
    # ret = ic.send(msg = message, toUserName = userName)
    # if ret:
    #     print("成功发送")
    # else:
    #     print("发送失败")
    # time.sleep(60)
    # ic.logout()
    #发送邮件1042538305@qq.com
    sender = 'luoquanhit@foxmail.com'
    receivers = ['1042538305@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    # 第三方 SMTP 服务
    mail_host = "smtp.qq.com"  # 设置服务器
    mail_user = "luoquanhit@foxmail.com"  # 用户名
    mail_pass = "fjhnhlbkatcgbedh"  # 口令


    message = MIMEText( msg, 'plain', 'utf-8')
    message['From'] = Header("你的罗大权～", 'utf-8')
    message['To'] = Header("双双～", 'utf-8')

    date_today = str(datetime.datetime.today()).split(' ')[0]
    subject = date_today + '今日份天气预报'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")




if __name__ == '__main__':
    # message = getWeather()
    # # 初始化机器人，扫码登陆
    # bot = Bot()
    # # 搜索名称含有 "游否"
    # my_friend = bot.friends().search('梁辉辉', sex=FEMALE, city="厦门")[0]
    # my_friend.send(message)
    main()
