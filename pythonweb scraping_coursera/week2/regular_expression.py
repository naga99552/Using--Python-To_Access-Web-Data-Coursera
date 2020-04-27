import re
# the commented code is sample file execution in assignment
'''#print(file_open.read())
def sample_data():
    file_open=open('sample.txt','r')
    op=[]
    sample_data_sum=0
    for i in file_open:
        s=re.findall('[0-9]+',i)
        for i in s:
            if len(i)!=0:
                sample_data_sum+=int(i)
    print(sample_data_sum)

sample_data()'''


def actual_data():
    file_open=open('actual.txt','r')
    op=[]
    sample_data_sum=0
    for i in file_open:
        s=re.findall('[0-9]+',i)
        for i in s:
            if len(i)!=0:
                sample_data_sum+=int(i)
    print(sample_data_sum)

actual_data()

