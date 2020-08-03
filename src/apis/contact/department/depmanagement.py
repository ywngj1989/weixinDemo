import logging
from apis.baseapi import BaseAPI
from initialization.sys_config import sys_cfg
import requests
import time
import datetime


class DepManagement(BaseAPI):
    def __init__(self):
        # 下面这行代码不加时，无法访问BaseAPI的变量
        BaseAPI.__init__(self)
        logging.info("Init depmanagement API")
        self.create_dep_url = sys_cfg.get('contact_para', 'create_dep_url')
        self.corpsecret = sys_cfg.get('contact_para', 'corpsecret')
        self.update_dep_url = sys_cfg.get('contact_para', 'update_dep_url')
        self.get_dep_list_url = sys_cfg.get('contact_para', 'get_dep_list_url')
        self.update_dep_url = sys_cfg.get('contact_para', 'update_dep_url')
        self.delete_dep_url = sys_cfg.get('contact_para', 'delete_dep_url')

    def create_dep(self):
        curr_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(curr_time, '%Y%m%d%H%M%S')
        name = "test" + time_str
        new_dep = {
          "name": name,
          "parentid": 1,
          "order": 1,
         }
        params = {'access_token': self.get_token(self.corpsecret)}
        logging.debug("创建部门的create_dep_url=", str(self.create_dep_url))
        logging.debug("创建部门的params = ", str(params))
        self.post_json(self.create_dep_url, new_dep, params=params)

# 参数化的方式创建成员
    def create_dep_by_param(self, name):
        new_dep = {
         "name": name,
         "parentid": 1,
         "order": 1
        }
        params = {'access_token': self.get_token(self.corpsecret)}
        logging.debug("create_dep_url=", str(self.create_dep_url))
        logging.debug("token=", self.get_token(self.corpsecret))
        self.post_json(self.create_dep_url, new_dep, params=params)

    def get_create_dept_res(self):
        return self.get_response()

# 获取部门列表
    def get_dep_list(self):
        params = {'access_token': self.get_token(self.corpsecret)}
        logging.debug("get_dep_list_url=", str(self.get_dep_list_url))
        res = requests.get(self.get_dep_list_url, params=params)
        logging.info("获取部门列表的响应内容=", res.json())
        return res.json().get('errmsg')

# 更新部门
    def update_dep(self, dep_id):
        curr_time = datetime.datetime.now()
        time_str = datetime.datetime.strftime(curr_time, '%Y%m%d%H%M%S')
        name = "edit"+time_str
        edit_dep = {
            "id": dep_id,
            "name": name
         }
        params = {'access_token': self.get_token(self.corpsecret)}
        self.post_json(self.update_dep_url, edit_dep, params=params)

# 删除部门
    def delete_dep(self, dep_id):
        params = {'access_token': self.get_token(self.corpsecret), 'id': dep_id}
        print("删除部门的params=", str(params))
        res = requests.get(self.delete_dep_url, params=params)
        return res.json().get('errmsg')
