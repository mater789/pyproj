import json

with open("test1.json","r") as cLoadJsonFile:
    cLoadDic = json.load(cLoadJsonFile)

if "accessors" in cLoadDic:
    cAcList = cLoadDic["accessors"]
    for cAc in cAcList:
        print(cAc)
        iBfViewIdx = cAc["bufferView"]
        print(type(iBfViewIdx))
        if "max" in cAc:
            cMax = cAc["max"]
            print(type(cMax[0]))

with open("test2.json", 'w') as cSaveJsonFile:
    json.dump(cLoadDic, cSaveJsonFile)

import os
import shutil

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
    
CopyDir("../materpy", "../test/materpy")

#def ExportGit(strGit, )