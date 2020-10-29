import os

xing = os.listdir('xing')
yunban = os.listdir('yunban')
xing_num = len(xing)
yunban_num = len(yunban)
index = 1

lines = []
for i in range(xing_num - 1):
	lines.append(str(index) + ' ' + 'xing/' + xing[i])
	index += 1

for i in range(yunban_num):
	lines.append(str(index) + ' ' + 'yunban/' + yunban[i])
	index += 1

with open('images.txt', 'w') as f:
	for line in lines:
		f.write(line + '\n')