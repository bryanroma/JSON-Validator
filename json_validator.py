#!/usr/bin/python3
## Script Author: Bryan Rodriguez Martin
## Description: Simple JSON validator written in python for a project in https://www.gofiotec.com
## TO-DO / KNOWN ERRORS
## [X] SOLVED: If the path has any '\b' , it rather reads hexadecimal \x08. The chars are being escaped.


## Execution: python json_checker.py

# -*- coding: utf-8 -*-

import json, sys

#Global var's
array = "null"
data_json = "null"


# Function that loads the JSON
def load_json():
    foo = 'null'
    try:
        ruta_json = input("[*] JSON path >>> ")
        print(ruta_json)
    # json.load throws a dicctionary
        with open(ruta_json, 'r') as f:
            try:
                array = json.load(f)
                print("[*] JSON loaded . . .")
            except:
                print("[!] Error loading JSON . . .")
                print("[!] Invalid JSON")
                foo = "1"
                sys.exit()

        data_json = json.dumps(array)    #json.dump throws a string
    
    except:
        if (foo == '1'):
            sys.exit()
        print("[!] File not found, please make sure the path is OK. Example: C:\\Users\\foo\\Desktop\\boo.json")
        sys.exit()

def banner():
    print('###########################################################')
    print('####################  G O F I O T E C  ####################')
    print('###########################################################')
    

# Function that validates the JSON
def validar_json(data_json):
    try:
        json.loads(data_json)
        print("[*] Valid JSON")
        return True
    except:
        print("[!] Invalid JSON")
        return False
        sys.exit()

def python_ver():
    #print(sys.version_info[0])
    if sys.version_info[0] < 3:
        print("Sorry, you must use Python 3.X")
        sys.exit()


def main():
    banner()
    python_ver()
    load_json()
    validar_json(data_json)

if __name__ == "__main__":
    main()
