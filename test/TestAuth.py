# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_auth(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(group_name="группа1", group_footer="описание", group_header="сыфсфы"))
    app.session.logout()