import pandas as pd

data={
    'Group':['A','A','A','B','B','B'],
    'Category':['X','Y','Z','X','Y','Z'],
    'Successes':['20','10','30','15','25','5'],
    'Trials':['50','50','50','50','50','50']
}

df=pd.DataFrame(data)
print (df)
