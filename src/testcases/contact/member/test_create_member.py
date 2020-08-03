from apis.contact.member.membermanagement import MemberManagement
import pytest


class TestCreateMember:

    def setup_class(self):
        self.member = MemberManagement()

    def test_create_new_member(self):
       # member = MemberManagement()
        self.member.create_member('../testdata/createmember.json')
        create_res = self.member.get_response()
        assert create_res.get('errmsg') == 'created'

    @pytest.mark.parametrize('userid', ['lidada'])
    def test_read_member(self, userid):
        errmsg = self.member.read_member(userid)
        assert errmsg == 'ok'

    def test_update_member(self):
        self.member.update_member('../testdata/updatemember.json')
        update_res = self.member.get_response()
        assert update_res.get('errmsg') == 'updated'

    @pytest.mark.parametrize('userid', ['ZhuLiQian'])
    def test_delete_member(self, userid):
        errmsg = self.member.delete_member(userid)
        assert errmsg == 'deleted'

    @pytest.mark.parametrize('useridlist', ['LiuDeHua', 'zhangyishan'])
    def test_delete_memberlist(self, useridlist):
        errmsg = self.member.delete_memberlist(useridlist)
        assert errmsg == 'deleted'

# 2020.8.3此处写到一半
    def test_get_dep_members(self, department_id, fetch_child):
        errmsg = self.member.get_dep_members(department_id, fetch_child)
        assert errmsg == 'ok'
