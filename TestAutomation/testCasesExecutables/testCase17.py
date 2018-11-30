import subprocess

loc = "../project/packages/lesspass-cli/index.js"
try:
    output = subprocess.check_output([loc, "test", "test", "test", "-L", "\-1"])
    output = output.decode("utf-8").strip()
except Exception as e:
    output = str(e)


f = open("../temp/17.txt", "w")
f.write(output)
f.close
