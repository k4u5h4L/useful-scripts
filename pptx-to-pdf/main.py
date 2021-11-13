# requirements
# sudo apt install unoconv
# pip install tqdm
# pip install glob
import glob
import tqdm
import os

path = input("Enter path to the folder: ")
extension = input("Enter extension without the dot: ")
files = [f for f in glob.glob(path + "/**/*.{}".format(extension), recursive=True)]
for f in tqdm.tqdm(files):
    command = "unoconv -f pdf \"{}\"".format(f)
    os.system(command)
