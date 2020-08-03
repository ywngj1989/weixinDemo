#! /usr/bin/env python
# coding=utf-8

import logging
import requests
from initialization.sys_config import sys_cfg


class BaseAPI:
    def __init__(self):
        logging.info("Init baseAPI interface")
        self.corpid = sys_cfg.get('corp_para', 'corpid')
        self.token_url = sys_cfg.get('corp_para', 'token_url')
        logging.info('token_url:' + str(self.token_url))
        logging.info('corpid:'+str(self.corpid))
        self.res = ''

    def get_token(self, corpsecret):
        params = {'corpid': self.corpid, 'corpsecret': corpsecret}
        logging.info('params='+str(params))
        logging.info('token_url:'+self.token_url)
        token_res = requests.get(self.token_url, params=params)
        print('access_token=', token_res.json().get('access_token'))
        return token_res.json().get('access_token')

    def post_json(self, url, json_obj, params=None):
        if params:
            self.res = requests.post(url, json=json_obj, params=params)
        else:
            self.res = requests.post(url, json=json_obj)

    def get_response(self):
        return self.res.json()
