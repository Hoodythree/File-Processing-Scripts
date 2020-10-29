
import os
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-p', '--path', required=True,
    help='base path of images')
ap.add_argument('-s', '--start', required=True,
    help='start index')


args = vars(ap.parse_args())

base_path = args['path']
# rename image(run once)
image_name = os.listdir(base_path)
total = int(args['start'])
for n in image_name:
	new_name = str(total).zfill(3) + '.jpg'
	old_filename = os.path.join(base_path, n)
	new_filename = os.path.join(base_path, new_name)

	os.rename(old_filename, new_filename)
	total += 1




