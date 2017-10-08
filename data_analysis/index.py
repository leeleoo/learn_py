#-*- coding:utf-8 –*-
import unicodecsv

common_path = '/Users/leo/study/sklearn/data_analysis/data/'


def read_csv(file_name):
    with open(common_path + file_name, 'rb') as f:
        render = unicodecsv.DictReader(f)
        return list(render)


# 1                 #
#####################################

## 从 daily_engagement.csv 和 project_submissions.csv 载入数据并存
## 储至下面的变量中，然后检查每张表的第1行。


daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

print(daily_engagement[0])
