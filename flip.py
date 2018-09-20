import csv
import os
import subprocess
import cv2
parent_dir = "/home/carnd/"
def makeFlippedData(og_folder_name):
    print("flipping", og_folder_name)
    # og_folder_name = "dirt_curve"
    og_folder_path = "{}data/{}".format(parent_dir, og_folder_name)
    new_folder_path = "{}data/flipped_{}".format(parent_dir, og_folder_name)
    if not os.path.exists(new_folder_path):
        subprocess.call(["mkdir", new_folder_path])
    if not os.path.exists("{}/IMG".format(new_folder_path)):
        subprocess.call(["mkdir", "{}/IMG".format(new_folder_path)])
    with open("{}/driving_log.csv".format(og_folder_path),'r') as csvfile:
        newfile = open('{}/driving_log.csv'.format(new_folder_path), 'w')
        reader = csv.reader(csvfile)
        writer = csv.writer(newfile)
       
        for line in reader:
            center_name = line[0].split("/")[-1]
            left_name = line[1].split("/")[-1]
            right_name = line[2].split("/")[-1]
            center_path = "{}data/{}".format(parent_dir, "/".join(line[0].split("/")[-3:]))
            left_path = "{}data/{}".format(parent_dir, "/".join(line[1].split("/")[-3:]))
            right_path = "{}data/{}".format(parent_dir, "/".join(line[2].split("/")[-3:]))
            center_flipped = cv2.flip(cv2.imread(center_path), 1)
            left_flipped = cv2.flip(cv2.imread(left_path), 1)
            right_flipped = cv2.flip(cv2.imread(right_path), 1)
            center_flipped_path = "{}/IMG/{}".format(new_folder_path, center_name)
            left_flipped_path = "{}/IMG/{}".format(new_folder_path, left_name)
            right_flipped_path = "{}/IMG/{}".format(new_folder_path, right_name)
            cv2.imwrite(center_flipped_path, center_flipped)
            cv2.imwrite(left_flipped_path, left_flipped)
            cv2.imwrite(right_flipped_path, right_flipped)
            newline = [center_flipped_path, 
                       left_flipped_path, 
                       right_flipped_path, 
                       -float(line[3]),
                       *line[4:]]
            writer.writerow(line)
        newfile.close()
        
folder_names = ["center1", "center2", "curve", "reverse", "dirt_curve", "dirt_curve2", "dirt_curve3", "dirt_curve4", "before_bridge", "recovery"]
for name in folder_names:
    makeFlippedData(name)
