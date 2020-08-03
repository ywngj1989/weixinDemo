import logging
from apis.baseapi import BaseAPI
from initialization.sys_config import sys_cfg
import time
import codecs
import json
import requests
import pytest


class MemberManagement(BaseAPI):
    def __init__(self):
        # 下面这行代码不加时，无法访问BaseAPI的变量
        BaseAPI.__init__(self)
        logging.info("Init MemberManagement API")
        self.create_member_url = sys_cfg.get('contact_para', 'create_member_url')
        self.corpsecret = sys_cfg.get('contact_para', 'corpsecret')
        self.read_member_url = sys_cfg.get('contact_para', 'read_member_url')
        self.update_member_url = sys_cfg.get('contact_para', 'update_member_url')
        self.delete_member_url = sys_cfg.get('contact_para', 'delete_member_url')
        self.batchdelete_member_url = sys_cfg.get('contact_para', 'batchdelete_member_url')
        self.dep_member_url = sys_cfg.get('contact_para', 'dep_member_url')

# 读取配置文件中的内容作为创建成员的json
    def get_new_member(self, file_name):
        with codecs.open(file_name, 'r', encoding='utf8') as f:
            json_object = json.loads(f.read(), encoding='utf8')
            logging.debug('json_object'+str(json_object))
            return json_object

# 读配置文件的方式拿到json串， 创建成员
    def create_member(self, file_name):
        new_member = self.get_new_member(file_name)
        logging.debug('')
        params = {'access_token': self.get_token(self.corpsecret)}
        logging.debug("create_dep_url=", self.create_member_url)
        logging.debug("token=", self.get_token(self.corpsecret))
        self.post_json(self.create_member_url, new_member, params=params)

    def get_create_member_res(self):
        return self.get_response()

# 读取成员
    def read_member(self, userid):
        params = {'access_token': self.get_token(self.corpsecret), 'userid': userid}
        logging.debug("read_member_url=", self.read_member_url)
        res = requests.get(self.read_member_url, params=params)
        return res.json().get('errmsg')

# 更新成员
    def update_member(self, file_name):
        update_member = self.get_new_member(file_name)
        params = {'access_token': self.get_token(self.corpsecret)}
        self.post_json(self.update_member_url, update_member, params=params)

# 删除成员
    def delete_member(self, userid):
        params = {'access_token': self.get_token(self.corpsecret), 'userid': userid}
        res = requests.get(self.delete_member_url, params=params)
        return res.json().get('errmsg')

# 批量删除成员
    def delete_memberlist(self, useridlist):
        params = {'access_token': self.get_token(self.corpsecret), 'useridlist': useridlist}
        res = requests.get(self.batchdelete_member_url, params=params)
        return res.json().get('errmsg')

# 获取部门成员
    def get_dep_members(self, department_id, fetch_child):
        params = {'access_token': self.get_token(self.corpsecret), 'department_id': department_id, 'fetch_child':fetch_child}
        res = requests.get(self.dep_member_url, params=params)
        return res.json().get('errmsg')
