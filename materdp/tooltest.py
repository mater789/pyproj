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

	dasdasd