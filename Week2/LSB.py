import hashlib
import random
import os
import numpy as np
from PIL import Image

import PLShandler as plsh

PLS = []

def DataListInBit(data):
    dataBits = list(format(c, '08b') for c in bytearray(data.encode('latin-1')))
    return dataBits


def PLSgen(row, col, lenEncodedText, dirTxt):
    new = []
    for i in range(row * col):
        new.append(i)
    for i in range(len(new) - 1, 0, -1):
        j = random.randint(0, i + 1)
        new[i], new[j] = new[j], new[i]
    for i in range(lenEncodedText * 3):
        PLS.append(new[i])
    pixelLocaterSequence = np.array(PLS)
    np.savetxt(dirTxt, pixelLocaterSequence, delimiter="\t")


def LsbEncoding(coverImagePath, stegoImageDir, encodedText, plsPassword):
    img = Image.open(coverImagePath)
    [row, col] = img.size
    dirTxt = stegoImageDir + "/pls.txt"
    PLSgen(row, col, len(encodedText), dirTxt)
    dataBits = DataListInBit(encodedText)
    dr = 0
    for i in range(0, len(encodedText) * 3, 3):
        dc = 0
        for j in range(0, 3):
            rr = PLS[i + j] // col
            rc = PLS[i + j] % col
            rgb = img.getpixel((rr, rc))
            value = []
            idx = 0
            for k in rgb:
                if (k % 2 == 0 and dataBits[dr][dc] == '1'):
                    if (k == 0):
                        k += 1
                    else:
                        k -= 1
                if (k % 2 == 1 and dataBits[dr][dc] == '0'):
                    k -= 1
                value.append(k)
                idx += 1
                dc += 1
                if (dc >= 8):
                    break
            if (dc >= 8):
                value.append(rgb[2])
            newrgb = (value[0], value[1], value[2])
            img.putpixel((rr, rc), newrgb)
        dr += 1
    stegoImagePath = stegoImageDir + "/out1.png"
    img.save(stegoImagePath)
    # plsPassword = input("Insert Password for pls encyption :")
    key = hashlib.sha256(plsPassword.encode()).digest()
    plsh.encrypt_file(key, dirTxt)


def LsbDecoding(stegoImagePath, plsDir, plspassword):
    # plspassword = input("Insert Password for pls decryption :")
    key = hashlib.sha256(plspassword.encode()).digest()
    plsPath = plsDir + '/pls.txt.enc'
    outPath = plsDir + '/out.txt'
    plsh.decrypt_file(key, plsPath, outPath)
    pls = np.genfromtxt(outPath, delimiter='\t')
    # if os.path.exists(outPath):
    #     os.remove(outPath)
    # if os.path.exists(plsPath):
    #     os.remove(plsPath)
    decodedTextInBits = []
    stegoImage = Image.open(stegoImagePath)
    [row, col] = stegoImage.size
    for i in range(0, len(pls), 3):
        ithChar = ""
        for j in range(0, 3):
            rr = pls[i + j] // col
            rc = pls[i + j] % col
            rgb = stegoImage.getpixel((rr, rc))
            for k in rgb:
                if (k & 1):
                    ithChar += '1'
                else:
                    ithChar += '0'

        ithChar = ithChar[:-1]
        decodedTextInBits.append((ithChar))
    decodedText = ''
    for i in decodedTextInBits:
        decodedText += chr(int(i, 2))
    return decodedText
