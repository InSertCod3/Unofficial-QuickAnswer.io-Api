# -*- coding: utf-8 -*-
from client import quickanswersapi

qapi = quickanswersapi.api('json')
print qapi.get("What was the budget of Titanic (1997)?")
