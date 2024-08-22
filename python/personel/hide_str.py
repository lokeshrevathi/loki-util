#hide_str
import base64
import yaml

def encrypt(str):
    newStr = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    strLen = len(str)
    alphaLen = len(alphabets)
    if strLen <= alphaLen:
        for i in range(strLen):
            newStr = newStr + str[i] + alphabets[i]
    else :
        i = 0
        while i < strLen:
            alphaIndex = i % alphaLen
            newStr = newStr + str[i] + alphabets[alphaIndex]
            i += 1
    encodedStr = base64.b64encode(newStr.encode('utf-8')).decode('utf-8')
    return encodedStr[:len(encodedStr) // 2] + 'g' + encodedStr[len(encodedStr) // 2:]

def decrypt(str):
    str = base64.b64decode(str[:(len(str) - 1) // 2] + str[((len(str) - 1) // 2) + 1:]).decode('utf-8')
    newStr = ''
    newStr = ''.join([j for i, j in enumerate(str) if i % 2 == 0])
    return newStr

def config():
    return yaml.safe_load(open('config.yaml', 'r'))

if __name__ == '__main__':
    toEncrypt = config()['to-encrypt']
    toDecrypt = config()['to-decrypt']
    print(encrypt(toEncrypt))
    # print(decrypt(toDecrypt))