# -*- coding: utf-8 -*-
import os

import re
import json

import requests
from bs4 import BeautifulSoup
from datetime import datetime

base_url = 'http://www.quickanswers.io/ask/?q='

class api (object):

    def __init__ (self, format = 'array'):
        supported_formats = ['array','json']
        self.format = format
        if self.format not in supported_formats :
            raise TypeError

    def urlize (self, string):
        #clean the string of symbols ex. # $ @ ! %
        string = re.sub(r"[^\w' ]", "", string)
        return str(string.replace(' ','%20'))

    def json (self, question, answers):
        json_dict = {}
        for a in answers:
            json_dict[answers.index(a)] = a
        data = {
            "question": question,
            "timestamp": str(datetime.now()),
            "answers": [
                json_dict
                ]
            }
        return json.dumps(data, separators=(',', ':'))

    def get (self, question):
        r = requests.get(base_url + self.urlize(question))
        soup = BeautifulSoup(r.text, "html.parser")
        answers = []
        for ans in soup.findAll('p'):
            answers.append(re.sub('[^a-zA-Z0-9\n\.\x00-\x7F]','',ans.text.encode('utf-8').replace('\n','').replace('\t','').replace('\r','')))
        if self.format == 'array': #return answers in array format (default)
            return answers
        if self.format == 'json': #return answers in json format
            return self.json(question ,answers)
