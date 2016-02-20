# -*- coding: utf-8 -*-
from client import quickanswersapi as qapi

t = qapi.api()
print t.get("when was google founded?$####")
