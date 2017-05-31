# -*- coding: UTF-8 -*-
import os

# 知乎 API 根地址
API_URL = 'https://api.zhihu.com'

# 是否需要验证码
CAPTCHA_URL = API_URL + '/captcha'

# 登录
LOGIN_URL = API_URL + '/sign_in'

CLIENT_ID = '8d5227e0aaaa4797a763ac64e0c3b8'
CLIENT_SECRET = 'ecbefbf6b17e47ecb9035107866380'

# 登录参数
LOGIN_DATA = {
    'client_id': CLIENT_ID,
    'grant_type': 'password',
    'source': 'com.zhihu.android',
    'timestamp': '',
    'username': '',
    'password': ''
}

# token 默认保存地址
TOKEN_PATH = os.environ['HOME'] + '/zhihu_crawler/zhihu.token'

# 日志文件
LOG_PATH = os.environ['HOME'] + '/zhihu_crawler/zhihu.log'