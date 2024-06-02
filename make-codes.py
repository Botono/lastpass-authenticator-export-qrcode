#!/usr/bin/env python3

import qrcode
import json

def main():
    exportJSON = json.load(open('lastpass-export.json'))
    for account in exportJSON['accounts']:
        url = makeURL(account)
        img = qrcode.make(url)
        img.save(f'{account["issuerName"]}.png')

def makeURL(account):
    return f'otpauth://totp/{account["issuerName"]}:{account["userName"]}?secret={account["secret"].upper()}&issuer={account["issuerName"]}'

if __name__ == "__main__":
    main()




