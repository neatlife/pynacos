# coding=utf-8


def getProperties(obj):
    properties = {}
    for attr in dir(obj):
        if '_' not in attr:
            properties[attr] = getattr(obj, attr)
    return properties
