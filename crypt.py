import html
import base64 
import hashlib
import json
import subprocess
import urllib3
import requests
import hashlib as hasher
import colorama
from colorama import Fore, Back, Style, init
colorama.init()
init(autoreset=True)
import passlib 
from passlib.hash import mssql2005 as m25
from passlib.hash import mssql2000 as m20
print(Fore.RED + "----------------------------------")
print(Fore.LIGHTBLUE_EX + "         H4WK OFCX   - XAİNE           ")
print(Fore.RED + "----------------------------------")
print(Fore.LIGHTBLUE_EX + "      Python Cryptografi Tool ")
print(Fore.LIGHTMAGENTA_EX + "      Author : H4WK OFCX & XAİNE \n      İnstagram => hawk.def - xaine_v1 \n      İnstagram => xd3lt4 - xaine_v2 \n      YouTube => HAWK DEFACER \n      Blog = https://farukdeveloper.online/")
print(Fore.RED + "----------------------------------")
print(Fore.RED + "      1- HTML ENCODE / DECODE \n      2- BASE64 ENCODE/DECODE \n      3- MD5 GENERATOR GENERATOR / ENCODE / DECODE \n      4- SHA GENERATOR \n")
print(Fore.RED + "----------------------------------")
cyrptsecenek = input("      Seçim=> ")
if cyrptsecenek == "1":
    print(Fore.BLUE + "      1- HTML Decode \n      2- HTML Encode")
    hawk = input("      Seçim yap => ")
    if hawk == "1" : 
        a_string = input("      Html Karakterlerini giriniz örnek '&lt;body&gt;' =>> ")
        decoded_string = html.unescape(a_string)
        print(decoded_string)
    elif hawk == "2" : 
        b_string = input("      Html Karakterlerini giriniz örnek '<body>' =>>")
        encoded_string = html.escape(b_string)
        print(encoded_string)
if cyrptsecenek == "2":
    print(Fore.BLUE + "      1- Base64 Decode \n      2- Base64 Encode")
    hello = input("      Seçenek seç -> ")
    if hello == "1" : 
        message = input("      Encode String => ")
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        print(Fore.BLUE + f"      şifre -> {base64_message}")
    if hello == "2" : 
        base64_string = input("      Decode String => ")
        base64_bytes = base64_string.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        print(Fore.BLUE + f"Çözülmüş ifade -> : {sample_string}")
if cyrptsecenek == "3":
    print(Fore.BLUE + "      MD5 GENERATOR \n      1-GENERATOR \n      2-DECODE (BRUTE FORCE) \n      3-DECODE(APİ) ")
    veri = input("      Islem Numarasini Girin : ")
    if veri =="1" :
        user = input("      YAZIYI GİR :  ")
        h = hashlib.md5(user.encode())
        h2 = h.hexdigest()        
        print(Fore.BLUE + "      " + h2)                       
    if veri =="2":                                
        wlist = input("      wordlist: ")
        hash2crack = input("      hash: ")
        wlistlines = open(wlist, "r").readlines()                                                                    
        for i in range(0, len(wlistlines)):                                            
            hash2comp = hashlib.md5(wlistlines[i].replace(           
                    "\n", "").encode()).hexdigest()                                       
            if hash2crack == hash2comp:                                                       
                print(Fore.BLUE + "      Cracklendi: "+wlistlines[i].replace("\n", ""))                               
                exit()                              
                print(Fore.BLUE + "      Cracklenemedi....")

    if veri == "3" : 
        dat2 = input("      Kırılacak MD5 Hash ==> ")
        print("      ")
        print("      _______________________________")
        print("")
        response = requests.get('http://www.nitrxgen.net/md5db/' + dat2).text
        print(Fore.BLUE + "      crack sonucu => " , response)
        print("")
        print(Fore.BLUE + "      cracklenen hash => " ,dat2)
        print("      ")
        print("      _______________________________")
if cyrptsecenek == "4":
        print(Fore.BLUE +"      1 - SHA512 CRYPT  \n      2 - MD5 CRYPT   \n      3 - SHA 256 CRYPT    \n      4 - SHA 224 CRYPT  \n      5 - SHA 384 CRYPT   \n      6 - MSSQL 2005 HASH  ")
        seçim = input("      Seçim yapınız: ")
        if seçim == "1":
            m=hashlib.sha512()
            sha512 = input("      STRİNG :")
            m.update(sha512.encode('utf-8'))
            print(Fore.BLUE +"      hash =>" + m.hexdigest())
        elif seçim == "2":
            sifreleyici = hashlib.md5()
            metin = input("lütfen Hashlenecek metini giriniz:")
            sifreleyici.update(metin.encode("utf-8"))
            hash = sifreleyici.hexdigest()
            print(Fore.BLUE +"      hash => %s" % hash)
        elif seçim =="3":
            me=hashlib.sha256()
            sha256 = input("      STRİNG :")
            me.update(sha256.encode('utf-8'))
            print(Fore.BLUE +"      hash =>" + me.hexdigest())
        elif seçim =="4":
            me=hashlib.sha224()
            sha224 = input("      STRİNG :")
            me.update(sha224.encode('utf-8'))
            print(Fore.BLUE +"      hash =>" + me.hexdigest())
        elif seçim == "5":
            me=hashlib.sha384()
            sha384 = input("      STRİNG :")
            me.update(sha384.encode('utf-8'))
            print(Fore.BLUE +"      hash =>" + me.hexdigest())
        elif seçim == "6":
            x = input("STRİNG :")
            x2 = m25.hash(x)
            print(Fore.BLUE +"      hash =>" + x2)