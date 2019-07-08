from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import functools
import collections


def cE():
    nA = open('numarr.txt', 'a')
    num = range(0, 10)
    version = range(1, 10)

    for eN in num:
        for eV in version:
            ip = 'D:/Tutorial/Test/IMg/images/numbers/' + str(eN) + '.' + str(eV) + '.png'
            ei = Image.open(ip)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())
            linetowrite = str(eN) + '::' + eiar1 + '\n'
            nA.write(linetowrite)


def threshold(imageArray):
    balanceAr = []
    new = imageArray

    for eachRow in imageArray:
        for eachPix in eachRow:
            avgNum = functools.reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3])
            balanceAr.append(avgNum)

    balance = functools.reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)

    for eachRow in new:
        for eachPix in eachRow:
            if functools.reduce(lambda x, y: x + y, eachPix[:3]) / len(eachPix[:3]) > balance:
                eachPix[0] = 255
                eachPix[1] = 255
                eachPix[2] = 255

            else:
                eachPix[0] = 0
                eachPix[1] = 0
                eachPix[2] = 0

    return(new)


def find(filePath):
    matchedar = []
    loadex = open('D://Tutorial//Test//Python//imgp//numarr.txt', 'r').read()
    loadex = loadex.split('\n')
    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()
    inq = str(iarl)
    for eX in loadex:
        if len(eX) > 3:
            splitEx = eX.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]

            epe = currentAr.split('],')
            epi = inq.split('],')
            x = 0
            while(x < len(epe)):
                if epe[x] == epi[x]:
                    matchedar.append(int(currentNum))
                    x = x + 1

    print(matchedar)
    x = collections.Counter(matchedar)
    print(x)


find("D:/Tutorial/Test/Python/imgp/test.png")
