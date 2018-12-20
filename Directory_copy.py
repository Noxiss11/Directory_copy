#-*- coding: utf-8 -*-
import os


path = input('Provide the path \n')
output_path = input('Provide output path \n')

class CopyDirectory():

	def Get_Folders(path):
		for folder in os.listdir(path):
			print(folder, os.path.isdir(path + '/' + folder))

	def Copy_Folders(path, output_path):
		for folder in os.listdir(path):
			if os.path.isdir(path + '/' + folder) == True:
				os.mkdir(output_path + '/' + folder)

	def Copy_Directory(path,output_path):
		for folder in os.listdir(path):
			if os.path.isdir(path + '/' + folder) == True:
				#print(path + '/' + folder)
				os.mkdir(output_path + '/' + folder)
				#print('created: ' , output_path + '/' + folder)
				CopyDirectory.Copy_Directory(path + '/' + folder,output_path+ '/' + folder)
			


# try:
# 	CopyDirectory.Copy_Directory(path,output_path)
# 	print('Done')
# except:
# 	print('Something has gone wrong')
CopyDirectory.Copy_Directory(path,output_path)