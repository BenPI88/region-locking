import os
os.system("python3 check_region.py")
region-output = str(os.system("cat out.txt"))
os.system("rm out.txt")
if region-output == "True":
  #game here!
