from apis.contact.member.membermanagement import MemberManagement
import pytest


class TestCreateMember:
    def test_create_new_member(self):
        member = MemberManagement()
        member.create_member('../testdata/member.json')
        create_res = member.get_response()
        assert create_res.get('errmsg') == 'created'
