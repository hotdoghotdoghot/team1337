import subprocess

loc = "../project/packages/lesspass-cli/index.js"
output = subprocess.check_output([loc, "test", "test", "test", "-lud"])
output = output.decode("utf-8").strip()

f = open("../temp/13.txt", "w")
f.write(output)
f.close
