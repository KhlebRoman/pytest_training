# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(group_name="группа1", group_footer="описание", group_header="сыфсфы"))


def test_add_empty_group(app):
    app.group.create(Group(group_name="", group_footer="", group_header=""))
