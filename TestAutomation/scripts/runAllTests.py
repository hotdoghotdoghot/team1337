import subprocess
import re
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# delete temp dir
folder = "../temp/"
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

strTable = "<html><table><tr><th>Char</th><th>ASCII</th></tr>"

for case in range(1, 26):
    execLoc = f"../testCasesExecutables/testCase{case:02}.py"
    oracleLoc = f"../oracles/testCase{case:02}Oracle.txt"

    # get the registry pattern for each file
    oFile = open(oracleLoc, "r")
    reg = oFile.readline().strip()
    oFile.close()
    pattern = re.compile(reg)

    # print each exec output to temp
    subprocess.run(["python", execLoc])

    if case == 20:
        tempFile1 = open(f"../temp/{case:02}-1.txt", "r")
        tempFile2 = open(f"../temp/{case:02}-2.txt", "r")
        testOutput1 = tempFile1.readline().strip()
        testOutput2 = tempFile2.readline().strip()
        tempFile1.close()
        tempFile2.close()
        result1 = bool(pattern.match(testOutput1))
        result2 = bool(pattern.match(testOutput2))
        dontMatch = testOutput1 != testOutput2
        result = result1 and result2 and dontMatch
    else:
        tempFile = open(f"../temp/{case:02}.txt", "r")
        testOutput = tempFile.readline().strip()
        tempFile.close()
        result = bool(pattern.match(testOutput))

    strRW = f"<tr><td>{case:02}</td><td>{result}</td></tr>"
    strTable = strTable + strRW

strTable = strTable + "</table></html>"
hs = open("asciiCharHTMLTable.html", "w")
hs.write(strTable)
