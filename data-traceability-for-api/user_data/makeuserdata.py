import random


def make_user_data(file_name):
    print(file_name)
    with open(file_name,'w') as file:
        file.write('api2_id\n')
        for i in range(10000):
            num=random.randint(1,99996)
            file.write(str(num)+'\n')

def make_leak_data(file_name,leak_file):
    with open('makedata.txt','r',encoding='UTF-8')as file:
        datas_=file.read().splitlines()
    with open(leak_file,'w',encoding='UTF-8') as file:
        with open(file_name,'r') as info:
            lines=info.read().splitlines()
        for i in range(1,lines.__len__()):
            num=int(lines[i])-1
            data=datas_[num]
            temp_data=data.split('\'')
            line = temp_data[1] + ' ' + temp_data[7] + ' ' + temp_data[9] + ' ' + temp_data[11] + ' ' + temp_data[
                13] + ' ' + temp_data[15] + ' ' + temp_data[17]
            file.write(line+'\n')
# make_user_data('user20data.txt')
make_leak_data('user10data.txt','leak_data.txt')