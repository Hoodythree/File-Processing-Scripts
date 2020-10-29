import os

xing = os.listdir('xing')
yunban = os.listdir('yunban')
xing_num = len(xing)
yunban_num = len(yunban)
index = 1

lines = []
for i in range(xing_num - 1):
	lines.append(str(index) + ' ' + '0')
	index += 1

for i in range(yunban_num):
	lines.append(str(index) + ' ' + '1')
	index += 1

with open('image_class_labels.txt', 'w') as f:
	for line in lines:
		f.write(line + '\n')