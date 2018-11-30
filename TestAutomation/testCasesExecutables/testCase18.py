import subprocess

loc = "../project/packages/lesspass-cli/index.js"

output = subprocess.run(
    [loc, "test", "test", "test", "-L", "0"], capture_output=True)
output = output.stderr.decode("utf-8")

f = open("../temp/18.txt", "w")
f.write(output)
f.close
