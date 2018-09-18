import subprocess
import os

# center1 = "https://www.dropbox.com/s/7jr9njm7b5ck0oo/center1.tar.gz?dl=1"
# center2 = "https://www.dropbox.com/s/khow2cd32nuim4o/center2.tar.gz?dl=1"
# center3 = "https://www.dropbox.com/s/ibiblwu7iwfv7h6/center3.tar.gz?dl=1"
# curve = "https://www.dropbox.com/s/cnr58iuhie6ubk0/curve.tar.gz?dl=1"
# recovery = "https://www.dropbox.com/s/9tgzzk82emek49k/recovery.tar.gz?dl=1"
# reverse = "https://www.dropbox.com/s/yp30jwqa3zhlmb4/reverse.tar.gz?dl=1"
center1 = "https://www.dropbox.com/s/ahuabohmr6pnrg6/center1.zip?dl=1"
center2 = "https://www.dropbox.com/s/6f5zoqkbucxxy42/center2.zip?dl=1"
reverse = "https://www.dropbox.com/s/4p7ctzsslgsowv0/reverse.zip?dl=1"
curve = "https://www.dropbox.com/s/o3dfk8dd3ygx1gl/curve.zip?dl=1"
dirt_curve = "https://www.dropbox.com/s/wkx0swwsfz8s4fs/dirt_curve.zip?dl=1"
dirt_curve2 = "https://www.dropbox.com/s/1iv2jcg47vhrt4o/dirt_curve2.zip?dl=1"
dirt_curve3 = "https://www.dropbox.com/s/9w1qbupyb9nublq/dirt_curve3.zip?dl=1"
dirt_curve4 = "https://www.dropbox.com/s/84zb1o4502ed3b5/dirt_curve4.zip?dl=1"
before_bridge = "https://www.dropbox.com/s/qkejwnr2xfosi8t/before_bridge.zip?dl=1"

urls = [center1, center2, curve, reverse, dirt_curve, dirt_curve2, dirt_curve3, dirt_curve4, before_bridge]


if not os.path.exists("/opt/data"):
    subprocess.call(["mkdir", "/opt/data"])
for url in urls:
    f_name = url.split("/")[-1][:-5]
    subprocess.call(["curl", "-o", "/opt/data/"+f_name, url, "-J", "-L"])
    subprocess.call(["unzip", "/opt/data/"+f_name, "-d", "/opt/data"])
#     subprocess.call(["tar", "-xvzf", "/opt/data/"+f_name, "--directory", "/opt/data"])

