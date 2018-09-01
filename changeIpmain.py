import codecs
import re
import logging

from getip import get_real_url, get_out_ip
from sendmail import sendmail

logging.basicConfig(
    filename='log/app.log',
    level=logging.DEBUG,
    format='%(asctime)s'
           ' %(threadName)s-%(thread)d'
           ' %(levelname)s-%(levelno)s'
           ' %(filename)s[line:%(lineno)d]'
           ' %(message)s',
    datefmt='%Y-%m-%d'
)


def check_ip(ip_str):
    """
    检查ip_str是否是IP4地址
    :param ip_str:
    :return:
    """
    flag = True
    # 精确的匹配给定的字符串是否是IP地址
    if re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                ip_str):
        logging.info("IP vaild")
    else:
        logging.info("IP invaild")
        flag = False
    return flag


def out_ip2(times):
    flag = False
    ip = None
    if times < 1:
        return ip
    try:
        # 获取外网ip
        real_url = get_real_url()
        ip = get_out_ip(real_url)
        flag = check_ip(ip)
    except Exception as e:
        logging.error(e)
    if flag:
        return ip
    else:
        if times == 1:
            return ""
        times = times - 1
        return out_ip2(times)


if __name__ == '__main__':
    out_ip = out_ip2(3)
    logging.info("外网ip: " + out_ip)
    if out_ip is None or "" == out_ip.strip():
        logging.error("程序异常退出")
        exit(0)
    # 检查保存的ip
    ip_file = "data/ip.txt"
    encoding = "UTF-8"
    old_ip = ""
    with codecs.open(ip_file, encoding=encoding) as f:
        for line in f:
            old_ip = line
    if out_ip != old_ip:
        logging.info("ip changed, set new ip address")
        with codecs.open(ip_file, 'w', encoding=encoding) as f:
            f.writelines(out_ip)
        # sendmail("463450693@qq.com", "ipchanged", out_ip)
        sendmail("use2send@163.com", "ipchanged", out_ip)
        logging.info("发送邮件成功")
    else:
        logging.info("ip has not changed")
    logging.info("程序完成")
