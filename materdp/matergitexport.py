import os
import shutil
import urllib.parse
import subprocess

#arg1 https://github.com/mater789/pyproj/materdp/
#arg2 e:/pyproj/
#arg3 master(op)

strGitUrl = os.sys.argv[1]
strLocalDir = os.sys.argv[2]
strBranch = "master"
if len(os.sys.argv) > 3:
    strBranch = os.sys.argv[3]

cGitUrl = urllib.parse.urlparse(strGitUrl)
cWordList = cGitUrl.path.split("/")

strGitUsr = cWordList[1];

strGitRep=cWordList[2];
strGitRep += ".git"

strGitRepUrl = cGitUrl.scheme + "://" + cGitUrl.netloc + "/" + strGitUsr + "/" + strGitRep;
bIsDir = False
strGitRelPath = ""
strGitRelLocalPath = ""
for iWordNum in range(3, len(cWordList)):
    strGitRelPath += cWordList[iWordNum]
    strGitRelLocalPath += cWordList[iWordNum]
    if iWordNum == len(cWordList) - 1:
        if cWordList[iWordNum] == "":#dir
            bIsDir = True
            strGitRelPath += "*"
        break;
    else:
        strGitRelPath += "/"
        strGitRelLocalPath += "/"

strTmpName = "mater_tmp_git_789"
with open(strTmpName + ".bat", "w") as cBatFile:
    cBatFile.write("set curtmpdir=" + strTmpName + "\n")
    cBatFile.write("git clone -n " + strGitRepUrl + " %curtmpdir%\n")
    cBatFile.write("cd %curtmpdir%\n")
    cBatFile.write("git config core.sparsecheckout true\n")
    cBatFile.write("echo " + strGitRelPath + " >> .git/info/sparse-checkout\n")
    cBatFile.write("git checkout " + strBranch + "\n")
    cBatFile.write("rd /q /s .git\n")

subprocess.call(strTmpName + ".bat")
if bIsDir:
    shutil.copytree(strTmpName + "/" + strGitRelLocalPath, strLocalDir)


