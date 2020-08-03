from apis.contact.department.depmanagement import DepManagement
import pytest


class TestCreateDep:

    def setup_class(self):
        self.dep = DepManagement()

    #@pytest.mark.dependency()
    def test_create_new_dep(self):
      #  dep = DepManagement()
        self.dep.create_dep()
        create_res = self.dep.get_response()
        dep_id = create_res.get('id')
        globals()['id'] = dep_id
        print('部门id=', dep_id)
        assert create_res.get('errmsg') == 'created'

    #@pytest.mark.dependency(depends=["test_create_new_dep"])
    def test_update_dep(self):
       # self.dep = DepManagement()
        dep_id = globals()['id']
        self.dep.update_dep(dep_id)
        update_res = self.dep.get_response()
        assert update_res.get('errmsg') == 'updated'

    def test_get_dep_list(self):
       # dep = DepManagement()
        errmsg = self.dep.get_dep_list()
        print("errmsg=", errmsg)
        assert errmsg == 'ok'

    def testdown(self):
        print("用例执行完毕")

'''
    #@pytest.mark.dependency(depends=["test_create_new_dep"])
    def test_delete_dep(self):
        #dep = DepManagement()
        dep_id = globals()['id']
        print("删除部门的id= ", dep_id)
        errmsg = self.dep.delete_dep(dep_id)
        assert errmsg == 'deleted'

    @pytest.mark.parametrize('name', ['测试部ya', '研发部w', '产品部o', '财务部k'])
    def test_create_new_dep_by_param(self, name):
        dep = DepManagement()
        dep.create_dep_by_param(name)
        create_res = dep.get_response()
        assert create_res.get('errmsg') == 'created'
'''





