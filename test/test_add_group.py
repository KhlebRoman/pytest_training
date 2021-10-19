# -*- coding: utf-8 -*-
from model.group import Group


def test_auth(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="группа1", group_footer="описание", group_header="сыфсфы"))
    app.session.logout()
