# Unofficial-QuickAnswer.io-Api
A Tiny Program to Get Answers QuickAnswer.io

How-To:

# -*- coding: utf-8 -*-
from quickanswersapi import client

>>> answers = client.api(json = False)
>>> results = answers.get("What was the budget of Titanic (1997)?")
>>> print (results)
...{
  "timestamp":"2016-03-08 20:31:31.916000",
  "question":"What was the budget of Titanic (1997)?",
  "answers":[
        {
          "0":"budget: $200 million"
        }
      ]
    }
