# -*- coding: utf-8 -*-
import unittest
import pytest
from group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_auth(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="группа1", group_footer="описание", group_header="сыфсфы"))
    app.logout()
