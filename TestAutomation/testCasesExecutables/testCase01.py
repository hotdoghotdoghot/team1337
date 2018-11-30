import subprocess

loc = "../project/packages/lesspass-cli/index.js"
output = subprocess.check_output([loc, "test", "test", "test"])
output = output.decode("utf-8").strip()

f = open("../temp/01.txt", "w")
f.write(output)
f.close
