import os
os.system("rm code.txt")
os.system("git clone https://github.com/BenPI88/region-locking-us && cd region-locking-us && cp code.txt ~/region-code.txt && cd .. && rm -rf region-locking-us")
region-code = str(os.system("cat region-code.txt"))
region-code = region-code
os.system("rm ~/region-code.txt")
os.system("echo " + str(region-code) + " > -code.txt")
if str(os.system("cat code.txt")) == str(os.system("cat -code.txt")):
  os.system("echo True > out.txt")
else:
  os.system("echo False > out.txt")
