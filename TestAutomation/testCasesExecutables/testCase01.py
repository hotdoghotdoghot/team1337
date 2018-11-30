import subprocess
import re

loc = "../project/packages/lesspass-cli/index.js"
output = subprocess.check_output([loc, "test", "test", "test"]).decode("utf-8")
output = output.strip()
print(output)
