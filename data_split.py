import os
import numpy as np

xing = os.listdir('xing')
yunban = os.listdir('yunban')
xing_num = len(xing)
yunban_num = len(yunban)

test_size = 0.2
index = 1

# print('xing num: {}'.format(xing_num))
# print('yunban num: {}'.format(yunban_num))

# 0-1 array,1 for train,0 for test
xing_arr = np.random.choice([0, 1], size = xing_num, p=[test_size, 1 - test_size])
yunban_arr = np.random.choice([0, 1], size = yunban_num, p=[test_size, 1 - test_size])

# filename is_training
lines = []
for i in range(xing_num - 1):
	line = str(index) + ' ' + str(xing_arr[i])
	lines.append(line)
	index += 1

for i in range(yunban_num):
	line = str(index) + ' ' + str(yunban_arr[i])
	lines.append(line)
	index += 1

with open('train_test_split.txt', 'w') as f:
	for line in lines:
		f.write(line + '\n')

