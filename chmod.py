#-*- coding: utf-8 -*-
import os
import ftplib
import stat
import sys
import ftputil
from multiprocessing import Process
import time
while True:
	try:
		parrent = 'my_dir'#главная директория, в которой производим назначение прав доступа
		ftp_host = ftputil.FTPHost('192.168.1.1', 'login', 'password')#адрес ftp, логин и пароль
		ftp = ftplib.FTP('192.168.1.1')#адрес ftp
		ftp.login(user = 'login', passwd = 'password')#логин и пароль
		ftp.cwd(parrent)

		def clean_tostart (text,cur):
					if not isinstance(text, str):
						raise TypeError('Это не текст')
					for i in [cur,]:
						text = text.replace(i,'')
					return text


		def all_dir(ftp,ftp_host,cur):
			data = ftp.nlst(cur)
			len_data = len(data)
			n = 0
			while n!= len_data:
				w = data[n]
				try:
					ftp_host.chmod(w, 0o777)
					print(w)
					os.system('cls');
				except:
					print('Пропущено из за ошибки')
					pass
				n+=1
			for top, dirs, files in ftp_host.walk(cur):
				l_dirs = len(dirs)
				if l_dirs == 0:
					pass
				else:
					i=0

					while i!=l_dirs:
						ww = (cur+'/'+dirs[i])
						print(ww)
						os.system('cls');
						all_dir(ftp,ftp_host,ww)
						i+=1
				break


		def chmode_start():
			data = ftp.nlst()
			print(len(data))
			for w in data:
				ftp_host.chmod(w, 0o777)
			for w in data:
				all_dir(ftp,ftp_host,w)


		chmode_start()
		print('Во всех файлах изменен доступ на 777')
		print('Перезапускаем процесс...')
		time.sleep(120)
		os.system('cls');
	except:
		pass

