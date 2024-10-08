# -*- coding: utf-8 -*-
"""
Created on Thur Jun 13 09:00:04 2024

@author: ratho
"""
sentence2="I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("My","Malaysia").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)