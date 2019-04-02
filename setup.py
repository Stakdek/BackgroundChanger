#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8
import sys
import os
import subprocess
from PythonSpinner import spinner
from install import setup_templates
import psutil

spinner.loading_bar(progress=4, state='Get variables…')
pwd = os.getcwd()
home = os.environ['HOME']
spinner.loading_bar(progress=6)
if len(sys.argv) > 2:
    picpath = str(sys.argv[2]).strip()
    if picpath.endswith('/'):
        picpath = picpath + '*'
    else:
        picpath = picpath + '/*'
else:
    picpath = '$HOME/*'
spinner.loading_bar(progress=8)
if len(sys.argv) > 1:
    interval = str(sys.argv[1]).strip()
    try:
        interval = int(interval)
    except ValueError:
        interval = 300
else:
    interval = 300
spinner.loading_bar(progress=10)
subprocess.check_call(['sudo', 'chown', '777', '-R', pwd])

spinner.loading_bar(progress=20, state='Update Repos…')
subprocess.check_call('cd PythonSpinner/ && git pull && cd ..',
                      shell=True, stdout=open(os.devnull, 'wb'))
spinner.loading_bar(progress=30)
subprocess.check_call(['git', 'pull'], stdout=open(os.devnull, 'wb'))

spinner.loading_bar(progress=40, state='Setup templates…')
setup_templates.run(interval, picpath)

spinner.loading_bar(progress=50, state='Moving new files…')
subprocess.check_call(['sudo', 'cp', 'install/backgroundchanger.desktop',
                       home + '/.config/autostart/'])
spinner.loading_bar(progress=60)
subprocess.check_call(['sudo', 'mv', 'backgroundchanger', '/usr/bin/'])

spinner.loading_bar(progress=70, state='Make executable…')
subprocess.check_call(['sudo', 'chmod', '-x', '/usr/bin/backgroundchanger'])
spinner.loading_bar(progress=80)
subprocess.check_call(['sudo', 'chmod', '775', '/usr/bin/backgroundchanger'])

spinner.loading_bar(progress=40, state='Installing service…')
subprocess.check_call(['sudo', 'chmod','777','-R',pwd])
spinner.loading_bar(progress=50)
subprocess.check_call(['mkdir', '-p',home+'/.local/share/systemd/user'])
spinner.loading_bar(progress=60)
subprocess.check_call(['sudo','cp', 'install/backgroundchanger.service',home+'/.local/share/systemd/user'])
spinner.loading_bar(progress=70)
subprocess.check_call('systemctl --user daemon-reload', shell=True)
spinner.loading_bar(progress=80)
subprocess.check_call(['systemctl', '--user','enable','backgroundchanger.service'])
spinner.loading_bar(progress=90)
subprocess.check_call(['systemctl', '--user','restart','backgroundchanger.service'])
spinner.loading_bar(progress=100)
print('')
print('Installed')
