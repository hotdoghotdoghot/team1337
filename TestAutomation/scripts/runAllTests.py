#!/usr/bin/env python3.7

import subprocess
import re
import os
import webbrowser

os.chdir(os.path.dirname(os.path.realpath(__file__)))

# delete temp dir
print("Clearing temp...")
folder = "../temp/"
for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(e)

results = "<html>\
    <link rel='stylesheet' href='style.css'>\
    <table><tr><th>Case</th><th>Description</th>\
    <th>Pass?</th><th>Oracle</th><th>Output</th></tr>"

for case in range(1, 26):
    print(f"Running case {case}")
    execLoc = f"../testCasesExecutables/testCase{case:02}.py"
    oracleLoc = f"../oracles/testCase{case:02}Oracle.txt"
    desLoc = f"../testCases/testCase{case:02}.txt"

    # get the test description
    with open(desLoc, "r") as dFile:
        description = dFile.readline()

    # get the registry pattern for each file
    with open(oracleLoc, "r") as oFile:
        reg = oFile.readline().strip()
    pattern = re.compile(reg)

    # print each exec output to temp
    subprocess.run(["python3.7", execLoc])
    if case == 20:
        with open(f"../temp/{case:02}-1.txt", "r") as tempFile1:
            testOutput1 = tempFile1.readline().strip()
        with open(f"../temp/{case:02}-2.txt", "r") as tempFile2:
            testOutput2 = tempFile2.readline().strip()
        result1 = bool(pattern.match(testOutput1))
        result2 = bool(pattern.match(testOutput2))
        dontMatch = testOutput1 != testOutput2
        result = result1 and result2 and dontMatch
    else:
        with open(f"../temp/{case:02}.txt", "r") as tempFile:
            testOutput = tempFile.readline().strip()
        result = bool(pattern.match(testOutput))

    row = f"<tr><td>{case:02}</td><td>{description}</td>"
    if result is False:
        row = row + f"<td bgcolor='#FF0000'>{result}</td>"
    else:
        row = row + f"<td bgcolor='#00FF00'>{result}</td>"
    row = row + f"<td>{reg}</td><td>{testOutput}</td></tr>"
    results = results + row
results = results + "</table></html>"

print("Writing and opening html...")
resultsLoc = "../reports/results.html"
with open(resultsLoc, "w") as hs:
    hs.write(results)
webbrowser.open(resultsLoc)
