# author : @Syhrularv_ Mod by topenK<
# -*- coding: utf-8 -*-

import os
import sys
import fileinput

N = '\033[0m'
D = '\033[90m'
W = '\033[1;37m'
B = '\033[1;34m'
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'

ask = G + '[' + W + '?' + G + '] '
sukses = G + '[' + W + '√' + G + '] '
eror = R + '[' + W + '!' + R + ']'

banner = """
{}BASH OBFUSCATE{}
{}Encrypt and Decrypt shell{}
{}
{}Mod by      :topenK{}
Youtube     {}:orangasing Channel
{}Telegram ch {}:@TPorangasing{}
""".format(D,W,D,W,D,W,Y,W,D,W,D,W,D,W,D,W,D,Y,D,W,D,Y,D,G,W,G,D,G,W,G,Y,D,Y,D,Y,D,Y,D,Y)

banner2 = """
   {}[{}1{}]{} Decrypt
""".format(G,W,G,W,G,W,G,W)

print banner
print banner2

def dekrip():
   try:
       sc = raw_input(ask + W + "Script " + G + "> " + W)
       f = open(sc,'r')
       filedata = f.read()
       f.close()

       newdata = filedata.replace("eval","echo")

       out = raw_input(ask + W + "Output" + G + " > " + W)
       f = open(out,'w')
       f.write(newdata)
       f.close()

       os.system("touch tes.sh")
       os.system("bash " + out + " > tes.sh")
       os.remove(out)
       os.system("mv -f tes.sh " + out)
       print (sukses + "Done..")

   except KeyboardInterrupt:
       print (eror + " Stopped!")
   except IOError:
       print (eror + " File Not Found!")

takok = raw_input(W + "Input 1 to Decrypt" + G + " > ")

if takok == "1" or takok == "01":
   dekrip()
else:
   print (eror + " Wrong input")
