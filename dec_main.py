import json,re,sys,os
import getpass
import argparse
from time import sleep
from http import client
try:
   import colorama
   from colorama import Fore, Back, Style
   colorama.init(autoreset=True)
   hijau = Style.RESET_ALL+Style.BRIGHT+Fore.GREEN
   res = Style.RESET_ALL
   abu2 = Style.DIM+Fore.WHITE
   ungu2 = Style.NORMAL+Fore.MAGENTA
   ungu = Style.RESET_ALL+Style.BRIGHT+Fore.MAGENTA
   hijau2 = Style.NORMAL+Fore.GREEN
   yellow2 = Style.NORMAL+Fore.YELLOW
   yellow = Style.RESET_ALL+Style.BRIGHT+Fore.YELLOW
   red2 = Style.NORMAL+Fore.RED
   red = Style.RESET_ALL+Style.BRIGHT+Fore.RE
except:   
   print ("Hmm Sepertinya Modul Colorama Belum Terinstall")
   sys.exit()
   try:
      import requests
      from bs4 import BeautifulSoup
   except:
      print ("Hmm Sepertinya Modul Requests Dan BS4 Belum Terinstall")
      sys.exit()
      from telethon import TelegramClient, sync, events
      from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
      from telethon.errors import SessionPasswordNeededError
      from telethon.errors import FloodWaitError
      banner = Style.NORMAL+Fore.MAGENTA+"""
      ###############################################
      #       Simple Bot Click Bot Telegram         #
      ###############################################
      # Create By : Kyuoko                          #
      # Code : Python                               #
      # Thx To UKL-TEAM, GFS-TEAM, AND YOU          #
      ###############################################
      """
      if not os.path.exists("session"):
            os.makedirs("session")
            def login(nomor): global client
            api_id = 717425
            api_hash = '322526d2c3350b1d3530de327cf08c07' 
            phone_number = nomor  
            client = TelegramClient("session/"+phone_number, api_id, api_hash)
            client.connect()
            if not client.is_user_authorized():    
               try:      
                  client.send_code_request(phone_number)      
                  me = client.sign_in(phone_number, input(f"{hijau}Enter Your Code {res}: "))    
               except SessionPasswordNeededError:
                  passw = input(f"{hijau}Your 2fa Password {res}: ")      
                  me = client.start(phone_number,passw)  
                  myself = client.get_me()  
                  os.system("clear")  
                  print (banner)  
                  print (f"{hijau}Telegram Number{res}",nomor)  
                  print (f"{hijau}Welcome To TeleBot{res}",myself.first_name,f"\n{hijau}Bot Ini Di Gunakan Untuk Menuyul Bot Telegram\\n\n")
                  def tunggu(x):
                                             sys.stdout.write("\r                                        \r")    
                                             for remaining in range(x, 0, -1):       
                                                sys.stdout.write("\\r")       
                                                sys.stdout.write("{}[{}|{}]{} {:2d} {}seconds remaining".format(abu2,yellow2,abu2,res,remaining,hijau))
                                                sys.stdout.flush()       
                                                sleep(0.125)       
                                                sys.stdout.write("\\r")       
                                                sys.stdout.write("{}[{}/{}]{} {:2d} {}seconds remaining".format(abu2,yellow2,abu2,res,remaining,hijau))       
                                                sys.stdout.flush()       
                                                sleep(0.125)       
                                                sys.stdout.write("\\r")       
                                                sys.stdout.write("{}[{}-{}]{} {:2d}{} seconds remaining".format(abu2,yellow2,abu2,res,remaining,hijau))       
                                                sys.stdout.flush()       
                                                sleep(0.125)       
                                                sys.stdout.write("\\r")      
                                                sys.stdout.write("{}[{}\\{}]{} {:2d}{} seconds remaining".format(abu2,yellow2,abu2,res,remaining,hijau))       
                                                sys.stdout.flush()       
                                                sleep(0.125)       
                                                sys.stdout.write("\\r")       
                                                sys.stdout.write("{}[{}|{}]{} {:2d}{} seconds remaining".format(abu2,yellow2,abu2,res,remaining,hijau))
                                                sys.stdout.flush()       
                                                sleep(0.125)       
                                                sys.stdout.write("\\r")       
                                                sys.stdout.write("{}[{}/{}]{} {:2d} {}seconds remaining".format(abu2,yellow2,abu2,res,remaining,hijau))       
                                                sys.stdout.flush()       
                                                sleep(0.125)       
                                                sys.stdout.write("\\r")
                                                sys.stdout.write("{}[{}-{}]{} {:2d} {}seconds remaining".format(abu2,yellow2,abu2,res,remaining,hijau))       
                                                sys.stdout.flush()       
                                                sleep(0.125)      
                                                sys.stdout.write("\\r")       
                                                sys.stdout.write("{}[{}\\{}]{} {:2d}{} seconds remaining".format(abu2,yellow2,abu2,res,remaining,hijau))
                                                sys.stdout.flush()       
                                                sleep(0.125)    
                                                sys.stdout.write("\\r                                           \\r")
                                                sys.stdout.write(f"\\r{abu2}[{yellow2}!{abu2}] {yellow}Getting Reward")
                                                ua={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36"}
                                                c = requests.session()
                                                if len(sys.argv)<2:    
                                                   print(banner)    
                                                   print(yellow2+"\\n\\n\\nUsage : python main.py +62xxxxxxxxxx")    
                                                   sys.exit(1)
                                                   login(sys.argv[1])
                                                   channel_entity=client.get_entity("@ClickBeeBot")
                                                   channel_username="@ClickBeeBot"
                                                   while True:    
                                                      sys.stdout.write("\\r                                             \\r")    
                                                      sys.stdout.write(f"\\r{abu2}[{yellow2}!{abu2}]{yellow} Mencoba Mengambil URL")    
                                                      client.send_message(entity=channel_entity,message="\xf0\x9f\x9a\xb2 Visit Links")    
                                                      sleep(3)    
                                                      posts = client(GetHistoryRequest(peer=channel_entity,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))    
                                                      if posts.messages[0].message.find("Aw snap! You can\'t visit any websites for now.") != -1:        
                                                         sys.stdout.write("\\r                                                 \\r")        
                                                         print (f"\\n{abu2}[{red2}x{abu2}] {red}Iklan Sudah Habis Coba Lagi Besok")
                                                         break    
                                                      else:        
                                                         url = posts.messages[0].reply_markup.rows[0].buttons[0].url
                                                         sys.stdout.write("\r                                              \r")        
                                                         sys.stdout.write(f"\r{abu2}[{yellow2}!{abu2}]{yellow} Memulai Mengunjungi Situs...!")
                                                         r = c.get(url,headers=ua)        
                                                         soup = BeautifulSoup(r.text, "html.parser")        
                                                         if soup.find('form', method="GET") is not None:            
                                                            sys.stdout.write("\r                                              \r")           
                                                            sys.stdout.write(f"\r{abu2}[{yellow2}!{abu2}]{yellow} Timer Detected....!")            
                                                            waktu = soup.find('i', id="timer")            
                                                            tunggu(int(waktu.text))
                                                            link = soup.find('form', method="GET").find('input').get('value')            
                                                            r = c.get('https://clickbeeads.com/link.php?u='+link)        
                                                            sleep(3)        
                                                            posts = client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0,hash=0))
                                                            sys.stdout.write("\\r                                        \\r")        
                                                            sys.stdout.write("\\r"+f"\\r{abu2}[{hijau2}+{abu2}]{hijau} "+posts.messages[0].message.replace("\xe2\x9c\x85 Task Completed!\\n","")+"\\n")
