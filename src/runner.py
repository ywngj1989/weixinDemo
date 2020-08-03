# ! /usr/bin/env python
# coding=utf-8
import sys
import logging
import os
import pytest


sys.path.append(os.path.dirname(sys.modules[__name__].__file__))
fileHandler = logging.FileHandler(filename="../log/auto.log", encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(module)s- %(lineno)s- %(message)s")
fileHandler.setFormatter(formatter)
logging.getLogger().addHandler(fileHandler)

if __name__ == '__main__':
    logging.info("Start to excute automation cases")
    #运行所有的测试用例
    #pytest.main(['-s', 'testcases/contact/department/test_create_dep.py'])
    #pytest.main(['-s', 'testcases/contact/department/test_create_dep.py::TestCreateDep::test_create_new_dep'])
    #pytest.main(['-s', 'testcases/contact/department/test_get_dep_list.py'])
    #运行指定的测试用例(模块路径- 类名-方法名)
    #pytest.main(['-s', 'testcases/contact/department/test_create_dep.py::TestCreateDep::test_create_new_dep_by_param'])
    #pytest.main(['-s', 'testcases/contact/member/test_create_member.py'])
    #pytest.main(['-s', 'testcases/'])
    pytest.main(['-s', 'testcases/contact/member/test_create_member.py::TestCreateMember::test_delete_member'])
