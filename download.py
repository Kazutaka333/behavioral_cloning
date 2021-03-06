import subprocess
import os

center1 = "https://www.dropbox.com/s/ahuabohmr6pnrg6/center1.zip?dl=1"
center2 = "https://www.dropbox.com/s/6f5zoqkbucxxy42/center2.zip?dl=1"
center3 = "https://www.dropbox.com/s/q42liwlb0x631qm/center3.zip?dl=1"
reverse = "https://www.dropbox.com/s/4p7ctzsslgsowv0/reverse.zip?dl=1"
curve = "https://www.dropbox.com/s/o3dfk8dd3ygx1gl/curve.zip?dl=1"
curve2 = "https://www.dropbox.com/s/yji8e3vkiubc87x/curve2.zip?dl=1"
dirt_curve = "https://www.dropbox.com/s/wkx0swwsfz8s4fs/dirt_curve.zip?dl=1"
dirt_curve2 = "https://www.dropbox.com/s/1iv2jcg47vhrt4o/dirt_curve2.zip?dl=1"
dirt_curve3 = "https://www.dropbox.com/s/9w1qbupyb9nublq/dirt_curve3.zip?dl=1"
dirt_curve4 = "https://www.dropbox.com/s/84zb1o4502ed3b5/dirt_curve4.zip?dl=1"
before_bridge = "https://www.dropbox.com/s/qkejwnr2xfosi8t/before_bridge.zip?dl=1"
recovery = "https://www.dropbox.com/s/q3jm8rux3skhur3/recovery.zip?dl=1"

urls = [center2, center3, curve2, reverse, recovery]

parent_dir = "/Users/Kazutaka/Downloads/"
if not os.path.exists(parent_dir+"data"):
    subprocess.call(["mkdir", parent_dir+"data"])
for url in urls:
    f_name = url.split("/")[-1][:-5]
    subprocess.call(["curl", "-o", parent_dir+"data/"+f_name, url, "-J", "-L"])
    subprocess.call(["unzip", parent_dir+"data/"+f_name, "-d", parent_dir+"data"])
#     subprocess.call(["tar", "-xvzf", "/opt/data/"+f_name, "--directory", "/opt/data"])
subprocess.call(['python', 'flip.py'])

