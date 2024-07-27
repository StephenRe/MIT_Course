import pandas as pd

filepath = 'tryit_8_1_batting_avg.csv'
batting = pd.read_csv(filepath)
batting

# creating sql file for install script.

# path to output sql file
output_file = 'MRTS/batter_insert.sql'

# prep statements
create_statement = '''DROP DATABASE IF EXISTS module_8_project;
CREATE DATABASE IF NOT EXISTS module_8_project;
USE module_8_project;
DROP TABLE IF EXISTS batting_average;
CREATE TABLE IF NOT EXISTS batting_average (Rk int, Pos varchar(5), Name varchar(50), BA float);\n'''

# list to hold values of each row
value_list = []

# populate value_list
for i, row in batting.iterrows():
    values = ','.join([f"'{str(val).replace("'", "''")}'" for val in row.tolist()])
    sql = f'({values})'
    value_list.append(sql)

# turn value_list into string
value_str = ',\n'.join(value_list)

# create full sql insert statement
insert_statement = f'INSERT INTO batting_average(Rk,Pos,Name,BA)\nVALUES\n{value_str};'

# write to sql file
with open(output_file, 'w') as file:
    file.write(create_statement)
    file.write(insert_statement)