#!/usr/bin/python3
'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, Apt, Dpkg, PyPI
    * License:          GNU General Publice License v3.0

    * Source code:      https://github.com/PyFarsi/pyabr
    * PyPI:             https://pypi.org/project/pyabr

    - Download Pyabr OS

    * AMD64, Intel64:   https://dl.pyabr.ir/pyabr-x86_64.iso     
    * ARM64:            https://dl.pyabr.ir/pyabr-arm64.img
    * Platform:         https://dl.pyabr.ir/stor.sb
    * Wheel Package:    https://dl.pyabr.ir/pyabr.whl
    
    - Channels:

    * Official Website: https://pyabr.ir
    * Telegram Channel: https://t.me/pyfarsi
    * Gap Channel:      https://gap.im/pyabr
    * Sorosh Channel:   https://splus.ir/pyabr
    * Instagram:        https://instagram.com/pyabrir
    * Hoorsa:           https://hoorsa.com/pyabr
    * Aparat:           https://aparat.com/pyabr

'''
import subprocess

from buildlibs import pack_archives as pack
from buildlibs import control
import shutil, os, sys, hashlib,getpass

os.chdir('/')

if os.path.isfile('/stor/vmabr.pyc'):

	if os.path.isdir('/stor/pyabr-master'):
		shutil.rmtree('/stor/pyabr-master')

	if os.path.isfile ('/stor/master.zip'):
		os.remove('/stor/master.zip')

	if os.path.isfile('/stor/proc/0'):  os.remove('/stor/proc/0')
	if os.path.isfile('/stor/proc/id/desktop'): os.remove('/stor/proc/id/desktop')
	if not os.path.isdir('/stor/proc/id'): os.mkdir('/stor/proc/id')

	os.system(f'cd /stor && "{sys.executable}" vmabr.pyc')
else:
	## pre build ##

	if not os.path.isdir("/app"):
		os.mkdir("/app")
		os.mkdir("/app/cache")
		os.mkdir("/app/cache/archives")
		os.mkdir("/app/cache/archives/data")
		os.mkdir("/app/cache/archives/control")
		os.mkdir("/app/cache/archives/code")
		os.mkdir("/app/cache/archives/build")
		os.mkdir("/app/cache/gets")

	if not os.path.isdir("/stor"):
		os.mkdir("/stor")
		os.mkdir("/stor/app")
		os.mkdir("/stor/app/packages")
	else:
		shutil.rmtree('/stor')
		os.mkdir("/stor")
		os.mkdir("/stor/app")
		os.mkdir("/stor/app/packages")

	if not os.path.isdir("/build-packs"): os.mkdir("/build-packs")

	# build #

	pack.install()
	pack.inst('baran')
	pack.inst('setup')

	# run #
	if os.path.isfile('/stor/proc/0'):  os.remove('/stor/proc/0')
	if os.path.isfile('/stor/proc/id/desktop'): os.remove('/stor/proc/id/desktop')
	if not os.path.isdir('/stor/proc/id'): os.mkdir('/stor/proc/id')

	# debug app #
	f = open('/stor/etc/suapp', 'w')
	f.write('setup')
	f.close()

	from PyQt5.QtCore import *
	from PyQt5.QtWidgets import *

	## Main entry ##
	application = QApplication(sys.argv)
	## https://www.cdog.pythonlibrary.org/2015/08/18/getting-your-screen-resolution-with-python/ Get screen model ##
	screen_resolution = application.desktop().screenGeometry()
	width, height = screen_resolution.width(), screen_resolution.height()

	f = open('/stor/proc/info/scn','w')
	f.write(str(width)+'x'+str(height))
	f.close()

	control.write_record('width',str(width),'/stor/etc/gui')
	control.write_record('height', str(height), '/stor/etc/gui')

	try:
		subprocess.call('rm -rf /etc/localtime',shell=True)
		subprocess.call('ln -s /usr/share/zoneinfo/Asia/Tehran /etc/localtime',shell=True)
		f = open ('/etc/sysconfig/clock','w')
		f.write('''ZONE="Asia/Tehran"
	UTC=false
	ARC=false''')
		f.close()
		subprocess.call('hwclock --systohc --localtime',shell=True)
	except: pass

	os.system(f'cd /stor && "{sys.executable}" vmabr.pyc gui-desktop root toor')

if not os.path.isfile('/stor/testing'):
	os.system('poweroff')