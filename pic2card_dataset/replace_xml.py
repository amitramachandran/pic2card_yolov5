import os
import shutil

source = "/home/amit/pic2card_dataset/images/train_and_test-5label-2020-Jun-05/train_and_test-2020-Jun-05/test/"
dest1 = "/home/amit/pic2card_dataset/labels/test/"

files = os.listdir(source)

for f in files:
    if f.endswith(".xml"):
        shutil.move(source+f, dest1)
