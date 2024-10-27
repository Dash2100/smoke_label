import os

# load all files name in ./lay
def get_all_files():
    files = os.listdir('./lay')
    return files

num = 1372

for filename in get_all_files():
    # print(filename, num)
    filename = filename.split('0000000000000')[1].split('.')[0]
    if num == int(filename):
        num += 1
    else:
        print(int(filename) - 1)
        num = int(filename) + 1

print("All files are checked.")