# -*- coding: utf-8 -*-
# coding=utf-8
import socket,struct,time,os,sys

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1 / 100)


logo = """\x1b[1;37m
                                     
                  
                     ;               ,           
                   ,;                 '.         
                  ;:                   :;        
                 ::                     ::       
                 ::                     ::       
                 ':                     :        
                  :.                    :        
               ;' ::                   ::  '     
              .'  ';                   ;'  '.    
             ::    :;                 ;:    ::   
            ;      :;.             ,;:     ::   
            :;      :;:           ,;"      ::   
             ::.      ':;  ..,.;  ;:'     ,.;:   
              "'"...   '::,::::: ;:   .;.;""'    
                  ''""....;:::::;,;.;'""         
              .:::.....'"':::::::'",...;::::;.   
             ;:' '""'"";.,;:::::;.'""""""  ':;   
            ::'         ;::;:::;::..         :;  
           ::         ,;:::::::::::;:..       :: 
           ;'     ,;;:;::::::::::::::;";..    ':.
          ::     ;:"  ::::::''''::::::  ":     ::
           :.    ::   :::::: \x1b[1;31m::\x1b[00m ::::::   :     ; 
            ;    ::   :::::: \x1b[1;31m::\x1b[00m ::::::   :    ;  
             '   ::   ::::::....:::::'  ,:   '   
             '  ::    :::::::::::::"   ::       
                ::     '::::::::::'    ::       
                 ':       """""""'  "'      ::       
                  ::                   ;:        
                  ':;                 ;:"        
                    ';              ,;'          
                      "'           '"            
                        '         '                                             
                                     
\x1b[00m"""

def show():
	os.system('clear')
	slowprint(logo)

show()
