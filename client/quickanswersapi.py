# -*- coding: utf-8 -*-
import os

import re

import requests
from bs4 import BeautifulSoup

base_url = 'http://www.quickanswers.io/ask/?q='

class api (object):

    def __init__ (self):
        pass

    def urlize (self, string):
        #clean the string of symbols ex. # $ @ ! %
        string = re.sub(r"[^\w' ]", "", string)
        return str(string.replace(' ','%20'))

    def get (self, question):
        r = requests.get(base_url + self.urlize(question))
        soup = BeautifulSoup(r.text, "html.parser")
        answers = []
        for ans in soup.findAll('p'):
            answers.append(re.sub('[^a-zA-Z0-9\n\.\x00-\x7F]',"",ans.text.encode('utf-8').replace('\n','').replace('\t','')))
        return answers
