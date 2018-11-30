import subprocess
import re

loc = "../project/packages/lesspass-cli/index.js"
output1 = subprocess.check_output([loc, "test", "test", "test", "-c", "1"])
output1 = output1.decode("utf-8").strip()

output2 = subprocess.check_output([loc, "test", "test", "test", "-c", "2"])
output2 = output2.decode("utf-8").strip()

f = open("../temp/20-1.txt", "w")
f.write(output1)
f.close

f = open("../temp/20-2.txt", "w")
f.write(output2)
f.close
