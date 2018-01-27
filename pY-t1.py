#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pandas import Series

aSer = Series([1, 2.0, 'a'])
# print(aSer)

import pandas as pd

data = {'name': ['wangdachui', 'Linling', 'Niuyun'], 'pay': [4000, 5000, 6000]}

frame = pd.DataFrame(data)
print(frame.ix[2])  # 真是奇怪了，明明没有ix的，居然也可以。



