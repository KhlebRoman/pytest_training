# -*- coding: utf-8 -*-
from model.group import Group



def test_add_group(app):
    old_groops = app.group.get_group_list()
    group = Group(group_name="группа", group_footer="описание", group_header="сыфсфы")
    app.group.create(group)
    new_groops = app.group.get_group_list()
    assert len(old_groops) + 1 == len(new_groops)
    old_groops.append(group)
    assert sorted(old_groops, key=Group.id_or_max) == sorted(new_groops, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groops = app.group.get_group_list()
    group = Group(group_name="", group_footer="", group_header="")
    app.group.create(group)
    new_groops = app.group.get_group_list()
    assert len(old_groops) + 1 == len(new_groops)
    old_groops.append(group)
    assert sorted(old_groops, key=Group.id_or_max) == sorted(new_groops, key=Group.id_or_max)
