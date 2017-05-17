# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 Spatial Current, Inc.
#
#########################################################################
"""
Contains the extract function
"""


def extract(keyChain, node, fallback):
    """
    extract data from object

    :param keyChain: a list of key names or array indicies for the target location
    :param node: the input object
    :param fallback: the value to return if the location is invalid or target value is None
    :return: the target value or fallback if None
    """

    if isinstance(keyChain, basestring):
        keyChain = keyChain.split(".")

    obj = None

    if node is not None:
        if len(keyChain) == 0:
            obj = node
        else:
            newKeyChain = keyChain[1:]
            if len(newKeyChain) == 0:
                if isinstance(keyChain[0], basestring) and keyChain[0].lower() == "length":
                    if isinstance(node, list):
                        obj = len(node)
                    else:
                        obj = node.get("length", 0)

        if (obj is None) and (node is not None):
            if isinstance(node, list):
                index = int(keyChain[0]) if isinstance(keyChain[0], basestring) else keyChain[0]
                obj = extract(newKeyChain, node[index], fallback)
            else:
                obj = extract(newKeyChain, node.get(""+keyChain[0]), fallback)
    else:
        obj = fallback

    return obj
