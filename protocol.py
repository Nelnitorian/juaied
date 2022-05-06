# -*- coding: utf-8 -*-

"""
Cliente -> Servidor:
[ USERNAME SEPARATOR DATA ]

Servidor -> Cliente
[ USERNAME SEPARATOR STATUS ]

"""

LIMIT_REACHED = 41
OK = 21

_SEPARATOR = '##'
_END = '&&'

def separate(message):
    msgs = message.split(_END)
    return msgs

def extract(message):
    data = message.split(_SEPARATOR)
    return data

def S2Cmsg(username, status):
    msg = username + _SEPARATOR + status + _END
    return msg

def C2Smsg(username, data):
    msg = username + _SEPARATOR + data + _END
    return msg