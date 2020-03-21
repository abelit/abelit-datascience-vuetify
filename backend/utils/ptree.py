# -*- encoding: utf-8 -*-
'''
@File    :   ptree.py
@Time    :   2020/03/21 08:32:27
@Author  :   Abelit
@Version :   1.0
@Contact :   ychenid@live.com
@Copyright :   (C)Copyright 2020, dataforum.org
Licence :   BSD-3-Clause
@Desc    :   None
'''


def create_ptree_from_obj(obj):
    if not isinstance(obj, dict):
        raise InvalidPermissionObjError()

    root = _create_tree_node(obj)
    return root


def _create_tree_node(obj):
    node = Permission(obj.get('key'), obj.get('name'))
    children = obj.get('children', [])
    for child in children:
        node.append_child(_create_tree_node(child))
    return node


def get_nodes_in_path(root, permissions):
    stack, nodes = [], set()
    for node in _traversal_ptree(root, stack):
        if node.key in permissions:
            nodes.update(_copy_path(stack))

    return nodes


def get_child_permissions(root):
    return list(_traversal_ptree(root, []))


def get_permissions_by_keys(root, permission_keys):
    permissions = []
    for node in _traversal_ptree(root, []):
        if node.key in permission_keys:
            permissions.append(node)

    return permissions


def _copy_path(path):
    return [node.key for node in path]


def _traversal_ptree(root, path):
    path.append(root)
    yield root
    for child in root.children:
        #  TODO: yield from for python3
        for node in _traversal_ptree(child, path):
            yield node
    path.pop()
