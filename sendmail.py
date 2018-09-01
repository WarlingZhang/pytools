import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp = smtplib.SMTP("smtp.163.com")
# smtp = smtplib.SMTP("smtp.qiye.163.com")
# smtp.connect('smtp.163.com', 25)
sender = 'use2send@163.com'
password = 'sqm123123'


def sendmail(receiver, subject, content):
    """
    发送邮件
    :param receiver: 接收人
    :param subject: 主题
    :param content: 邮件内容
    :return:
    """
    msg = MIMEMultipart('mixed')
    subject = subject
    msg['Subject'] = subject
    msg['From'] = 'use2send <' + sender + '>'
    if isinstance(receiver, str):
        receivers = receiver
    else:
        receivers = ";".join(receiver)
    msg['To'] = receivers
    # 构造文字内容
    text = content
    text_plain = MIMEText(text, 'plain', 'utf-8')
    msg.attach(text_plain)

    smtp.login(sender, password)
    # if isinstance(msg, str):
    #     content = msg
    # else:
    #     content = msg.as_string()

    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()


if __name__ == '__main__':
    # sendmail("use2send@163.com",  "127.0.0.1")
    # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.baidu.com"
    # text_plain = MIMEText(text, 'plain', 'utf-8')
    # sendmail("use2send@163.com",  text_plain)

    # 构造邮件对象MIMEMultipart对象
    # 下面的主题，发件人，收件人，日期是显示在邮件页面上的。

    # msg['To'] = 'XXX@126.com'
    # 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串

    # msg['Date']='2012-3-16'

    # 构造图片链接
    # sendimagefile = open(r'D:\pythontest\testimage.png', 'rb').read()
    # image = MIMEImage(sendimagefile)
    # image.add_header('Content-ID', '<image1>')
    # image["Content-Disposition"] = 'attachment; filename="testimage.png"'
    # msg.attach(image)

    # 构造附件
    # sendfile = open(r'D:\pythontest\1111.txt', 'rb').read()
    # text_att = MIMEText(sendfile, 'base64', 'utf-8')
    # text_att["Content-Type"] = 'application/octet-stream'
    # # 以下附件可以重命名成aaa.txt
    # # text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
    # # 另一种实现方式
    # text_att.add_header('Content-Disposition', 'attachment', filename='aaa.txt')
    # # 以下中文测试不ok
    # # text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
    # msg.attach(text_att)


    sendmail("use2send@163.com", "ipchanged22", "<html>你好, 送到附近速度飞快</html>")
    print("发送完成")

