import mysql.connector as mc
import yaml
import pandas as pd

y = yaml.safe_load(open('yamltest.yaml'))

print(type(y['bar']))
print(y['bar'])
print(y['foo'])
print(y['bar1'])
print(y['foo1'])
# for k in y['bar']:
#     print(k)

# print(type(y['xmas-fifth-day']['partridges']))
# for k,v in y['xmas-fifth-day']['partridges'].items():
#     print(k,v)

open