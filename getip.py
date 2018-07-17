import socket
import requests
from bs4 import BeautifulSoup


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ips = s.getsockname()
        ip = ips[0]
    finally:
        s.close()

    return ip


# 获取外网IP
def get_out_ip(url):
    r = requests.get(url)
    txt = r.text
    ip = txt[txt.find("[") + 1: txt.find("]")]
    # print('ip:' + ip)
    return ip


def get_real_url(url=r'http://www.ip138.com/'):
    r = requests.get(url)
    txt = r.text
    soup = BeautifulSoup(txt,"html.parser").iframe
    return soup["src"]


if __name__ == '__main__':
    print("内网ip", get_host_ip())
    real_url = get_real_url()
    outip = get_out_ip(real_url)
    print("外网ip", outip)
