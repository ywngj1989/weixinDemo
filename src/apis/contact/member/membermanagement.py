import logging
from apis.baseapi import BaseAPI
from initialization.sys_config import sys_cfg
import time
import codecs
import json


class MemberManagement(BaseAPI):
    def __init__(self):
        # 下面这行代码不加时，无法访问BaseAPI的变量
        BaseAPI.__init__(self)
        logging.info("Init MemberManagement API")
        self.create_member_url = sys_cfg.get('contact_para', 'create_member_url')
        self.corpsecret = sys_cfg.get('contact_para', 'corpsecret')

# 读取配置文件中的内容作为创建成员的json
    def get_new_member(self, file_name):
        with codecs.open(file_name, 'r', encoding='utf8') as f:
            json_object = json.loads(f.read(), encoding='utf8')
            logging.debug('json_object'+str(json_object))
            return json_object

# 读配置文件的方式拿到json串
    def create_member(self, file_name):
        new_member = self.get_new_member(file_name)
        logging.debug('')
        params = {'access_token': self.get_token(self.corpsecret)}
        logging.debug("create_dep_url=", self.create_member_url)
        logging.debug("token=", self.get_token(self.corpsecret))
        self.post_json(self.create_member_url, new_member, params=params)

    def get_create_member_res(self):
        return self.get_response()

    def update_member(self, user_id):
        pass

    def read_member(self, user_id):
        pass
