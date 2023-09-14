
import argparse
import collections.abc
import json
import pathlib
from pprint import pprint
import re
import os
import sys

import mozidb


"""
		说明，需要安装：
		pip install python-snappy
		
"""


db_data=[]

db = mozidb.IndexedDB("my.sqlite")
db_data = db.read_objects()

#print(db_data)
# for Export uBlock My filters List
#print(db_data["user-filters"])

data = []


for dict_key in db_data.keys():
	print(dict_key)

for dict_value in db_data.values():
	print(dict_value)




