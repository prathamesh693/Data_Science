# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:09:16 2024

@author: ratho
"""
import re
chat1='Hello,I am having an issue with my order #412889912'
def get_pattern_match(pattern,text):
    matches = re.findall(pattern, text)
    if matches:
       return matches[0]
    
    
get_pattern_match('order[^\d](\d)',chat1 )

#############################3
chat1='you ask lot of question 123456789,abc@xyz.com'
chat2='hereit is:(123)-567-8912,abc@xyz.com'
chat3='yes,phone:12345678912 email:abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]@[a-z]\'[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]@[a-z]\'[a-zA-Z0-9]*',chat2)
get_pattern_match('[a-zA-Z0-9_]@[a-z]\'[a-zA-Z0-9]*',chat3)
########################################
get_pattern_match('(\d{10})|(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\d{3}\)-\d{3}-\d{4})',chat2)
get_pattern_match('(\d{10})|(\d{3}\)-\d{3}-\d{4})',chat3)

###############################3

text= '''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)
'''
get_pattern_match(r'age(\d+)',text)
get_pattern_match(r'Born(.*)\n',text).strip()
get_pattern_match(r'Born.\n(.)\(age',text).strip()
get_pattern_match(r'\(age.\n(.)',text)