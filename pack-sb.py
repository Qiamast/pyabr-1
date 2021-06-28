#######################################################################################
#  In the name of God, the Compassionate, the Merciful
#  Pyabr (c) 2020 Mani Jamali. GNU General Public License v3.0
#
#  Official Website: 		http://pyabr.rf.gd
#  Programmer & Creator:    Mani Jamali <manijamali2003@gmail.com>
#  Gap channel: 			@pyabr
#  Gap group:   			@pyabr_community
#  Git source:              github.com/PyFarsi/pyabr
#
#######################################################################################

import subprocess, os, sys, shutil

list = os.listdir('.')
list.remove('.git')
list.remove('.idea')
list.remove('wheel')
list.remove('build.py')
list.remove('pack-sb.py')
list.remove('build-packs.py')
list.remove('LICENSE')
list.remove('pack.py')
list.remove('pack-wheel.py')
list.remove('README.md')
list.remove('clouddrive')
list.remove('requirments.txt')
list.remove('setup.ui')
list.remove('setup.py')
list.remove('.gitignore')
list.remove('mark_updates')
list.remove('build-date.txt')
list.remove('CONTRIBUTING.md')
if '__pycache__' in list:
    list.remove('__pycache__')
list.remove('AUTHERS')

if not os.path.isdir('sb'):
    os.mkdir('sb')
    os.mkdir('sb/stor')
    os.mkdir('sb/root')
    os.mkdir('sb/etc')

    f = open('sb/etc/issue.net', 'w')
    f.write('Pyabr')
    f.close()

    f = open('sb/etc/os-release','w')
    f.write('''PRETTY_NAME="Pyabr 2 (Aras)"
NAME="Pyabr"
VERSION_ID="2"
VERSION="2 (Aras)"
VERSION_CODENAME=aras
ID=pyabr''')
    f.close()
else:
    list.remove('sb')

for i in list:
    if os.path.isdir(i):
        shutil.copytree(i,'sb/'+i)
    else:
        shutil.copyfile(i, 'sb/'+i)

subprocess.call(['mksquashfs','sb','stor.sb','-comp','xz'])
import clean