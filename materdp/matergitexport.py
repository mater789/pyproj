import os
import shutil
import urllib.parse
import subprocess

#arg1 https://github.com/mater789/pyproj/materdp
#arg2 e:/pyproj
#arg3 master(op)

def CopyDir(strSrcDir, strDestDir):
    if not os.path.isdir(strSrcDir):
        raise FileNotFoundError
    if not os.path.isdir(strDestDir):
        os.makedirs(strDestDir)
    cFileNameList = os.listdir(strSrcDir)
    for strFileName in cFileNameList:
        strSrcName = os.path.join(strSrcDir, strFileName)
        strDstName = os.path.join(strDestDir, strFileName)
        if os.path.isdir(strSrcName):
            CopyDir(strSrcName, strDstName)
        elif os.path.isfile(strSrcName):
            if os.path.isfile(strDstName):
                os.remove(strDstName)
            shutil.copy2(strSrcName, strDstName)

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
strGitRelPath = ""
for iWordNum in range(3, len(cWordList)):
    strGitRelPath += cWordList[iWordNum]
    if iWordNum == len(cWordList) - 1:
        strGitRelPath += "/*"
        break;
    else:
        strGitRelPath += "/"

strTmpName = "mater_tmp_git_789"
with open(strTmpName + ".bat", "w") as cBatFile:
    cBatFile.write("set curtmpdir=" + strTmpName + "\n")
    cBatFile.write("git clone -n --depth=1 " + strGitRepUrl + " %curtmpdir%\n")
    cBatFile.write("cd %curtmpdir%\n")
    cBatFile.write("git config core.sparsecheckout true\n")
    cBatFile.write("echo " + strGitRelPath + " >> .git/info/sparse-checkout\n")
    cBatFile.write("git checkout " + strBranch + "\n")
    cBatFile.write("rd /q /s .git\n")

subprocess.call(strTmpName + ".bat")
strGitRelPath = strGitRelPath.strip("*")
CopyDir(strTmpName + "/" + strGitRelPath, strLocalDir)
os.remove(strTmpName + ".bat")
shutil.rmtree(strTmpName)


