# -*- coding: utf-8 -*-
from quickanswersapi import client

answers = client.api(json = False)
results = answers.get("What was the budget of Titanic (1997)?")
print (results)
