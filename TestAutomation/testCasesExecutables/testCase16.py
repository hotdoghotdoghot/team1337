import subprocess

loc = "../project/packages/lesspass-cli/index.js"
output = subprocess.check_output([loc, "test", "test", "test", "-luds"])
output = output.decode("utf-8").strip()

f = open("../temp/16.txt", "w")
f.write(output)
f.close
