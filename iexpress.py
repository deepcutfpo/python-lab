import os
from subprocess import check_output
import re
print("--------------")
print("  How To Use")
print("--------------")

print("----------------------------------------------------------------\nPlace files you want to bind in the folder named FILES in the \nsame directory as the python script. \nThen input the exe name of the output extractor.")
print("----------------------------------------------------------------\n\n")
outname=os.getcwd()+"\\"+input("File Output Name [.exe]: ")
iex_base=["[Version]","Class=IEXPRESS","SEDVersion=3","[Options]","PackagePurpose=ExtractOnly","ShowInstallProgramWindow=1","HideExtractAnimation=1","UseLongFileName=1","InsideCompressed=0","CAB_FixedSize=0","CAB_ResvCodeSigning=0","RebootMode=I","InstallPrompt=%InstallPrompt%","DisplayLicense=%DisplayLicense%","FinishMessage=%FinishMessage%","TargetName=%TargetName%","FriendlyName=%FriendlyName%","AppLaunched=%AppLaunched%","PostInstallCmd=%PostInstallCmd%","AdminQuietInstCmd=%AdminQuietInstCmd%","UserQuietInstCmd=%UserQuietInstCmd%","SourceFiles=SourceFiles","[Strings]","InstallPrompt=","DisplayLicense=","FinishMessage= ","TargetName="+outname+".exe","FriendlyName= ","AppLaunched=","PostInstallCmd=","AdminQuietInstCmd=","UserQuietInstCmd="]



os.system("dir /b FILES\*.* > lof.dat")
l1=[]
f1 = open('lof.dat')
filenum=0
for line in f1:
    l1.append("FILE"+str(filenum)+"="+"\""+line.rstrip('\n')+"\"")
    filenum+=1
for f in l1:
    iex_base.append(f)
iex_base.append("[SourceFiles]")
iex_base.append("SourceFiles0=\""+os.getcwd()+"\\FILES\"")
iex_base.append("[SourceFiles0]")
for x in range(filenum):
    iex_base.append("%FILE"+str(x)+"%=")
f1.close()
# CREATE SED CONFIG NEEDED FOR IEXPRESS
base=""
if os.path.exists("base.sed"):
    base = open("base.sed", "r+")
else:
    base = open("base.sed", "w")
for item in iex_base:
  base.write("%s\n" % item)
base.close()
# END SED CONFIG

os.system("iexpress /N "+os.getcwd()+"\\base.sed")
os.remove("lof.dat")
os.remove("base.sed")
