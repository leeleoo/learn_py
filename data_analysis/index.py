# -*- coding:utf-8 –*-
import unicodecsv
import os

path1 = os.path.abspath('.')

common_path = '/csv/'


def read_csv(file_name):
    _path = path1 + common_path + file_name
    print 'real_path', _path
    with open(_path, 'rb') as f:
        render = unicodecsv.DictReader(f)
        return list(render)


# 1                 #
#####################################

## 从 daily_engagement.csv 和 project_submissions.csv 载入数据并存
## 储至下面的变量中，然后检查每张表的第1行。


daily_engagement = read_csv('daily-engagement.csv')
project_submissions = read_csv('project-submissions.csv')

print(daily_engagement[0])
