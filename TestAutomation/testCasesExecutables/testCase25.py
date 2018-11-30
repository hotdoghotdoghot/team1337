import subprocess
import pyperclip

loc = "../project/packages/lesspass-cli/index.js"
output = subprocess.check_output([loc, "test", "test", "test", "-C"])

clipB = pyperclip.paste()
print(clipB)

f = open("../temp/25.txt", "w")
f.write(clipB)
f.close
