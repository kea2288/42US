#!/usr/bin python

#---------------------------------------------------------------#
# This program created to check tasks of Piscine days.          #
# No garantee that correction by this progam will be 100% True. #
# PLEASE TURN ON YOUR BRAIN AND NEVER GIVE UP!                  #
# ------------------------------------------------------------- #
# Written by: ekulyyev              |                           #
# Place: 42 School Silicon Valley   |                           #
# Date: 08/12/2017                  |                           #
#---------------------------------------------------------------#

import os, time
import subprocess

sep = os.sep

pathToTask = 'myDay' # This is path to days tasks folder
pathToConfig = '' # This is path to config of days
configFile = ''
runScript = True


myDayFolder = os.listdir('{0}'.format(pathToTask))
myDayDir = myDayFolder[0]

fileNum = myDayDir[1:]
myDayFilesPath = os.listdir(os.getcwd() + sep + myDayDir)

if len(myDayFolder) > 1:
	print("More than one folder in myDay folder. Must be one folder.")
	runScript = False

configFile = 'config_d{0}.pl'.format(fileNum)
print(configFile)
pathToConfig = os.listdir('{0}'.format(myDayDir))
for i in pathToConfig:
	if i == configFile:
		print(i)
		break
if i != configFile:
	runScript = False
	print("Config file doesn\'t exists!" )

if runScript:
	os.system('./spawn.pl .{2}{3}{2}d0{0} .{2}{1}{2}config_d0{0}.pl'.format(fileNum, myDayDir, sep, pathToTask))
	time.sleep(0.1)
	os.system('./tools/build.sh')
	time.sleep(0.1)
	os.system('./tools/verify.sh')
	time.sleep(0.1)
	os.system('./tools/check_all.sh')
	print(' Checked! You can look at your results.')
