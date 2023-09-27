import re
import json
def make_leak_data_agency():
	with open ('../user_data/agency_re.txt','r',encoding='UTF-8') as file:
		lines=file.read().splitlines()
	with open('../user_data/agency_leak_data.txt','w',encoding='UTF-8') as file:
		for i in range(lines.__len__()):
			if(lines[i]=='{' or lines[i]=='},'):
				pass
			else:
				line=lines[i].split('}')[0]
				line=line.split('{')[1]
				line="{"+line+"}"
				line=eval('u"%s"' % line)
				json_=json.loads(line)
				line=str(json_.get('id'))+' '+json_.get('email')+' '+json_.get('姓名')+' '+json_.get('性别')+' '\
					 +json_.get('手机号')+' '+json_.get('省或直辖市')+' '\
					 +json_.get('市') + ' ' + json_.get('区或县')
				file.write(line+'\n')

def find_id(file_name):
	with open(file_name,'r',encoding='UTF-8') as file:
		lines=file.read().splitlines()
	count=[[0,0],[0,0],[0,0],[0,0],
		   [0,0],[0,0],[0,0],[0,0],
		   [0,0],[0,0],[0,0],[0,0],
		   [0,0],[0,0],[0,0],[0,0]]
	for i in range(lines.__len__()):
		line=lines[i].split(' ')
		line=line[line.__len__()-1]
		char_int = ord(line[0]) % 16
		if(line[line.__len__()-1]=='市'):
			count[char_int][1]=count[char_int][1]+1
		else:
			count[char_int][0] = count[char_int][0] + 1
	val=1
	sum=0
	flag=0
	for i in range(16):
		if(count[i][0]<count[i][1]):
			flag=1
			sum=sum+val
		else:
			flag=0
		val=val*2
		print(count[i][0],count[i][1],"第"+str(i)+"个bit位：",flag)
	print("泄露方的id为"+str(sum))

find_id('../user_data/agency_leak_data')






