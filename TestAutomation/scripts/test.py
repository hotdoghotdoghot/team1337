import subprocess

loc = "../project/packages/lesspass-cli/index.js"
# output = subprocess.check_output(["echo", "Hello World!"])
output = subprocess.check_output([loc, "test", "test", "test", "-lup"])
print(str(output))
