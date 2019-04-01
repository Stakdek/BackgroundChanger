#!/bin/bash
sudo chown 777 -R $PWD
echo 'Update Repo…'
git config credential.helper store
git pull
echo 'Setup templates…'
python install/setup_templates.py $1 $2
echo 'Moving new files…'
sudo cp install/backgroundchanger.service /etc/systemd/system/
sudo mv backgroundchanger /usr/bin/
echo 'Make executable…'
sudo chmod -x /usr/bin/backgroundchanger
sudo chmod 775 /usr/bin/backgroundchanger
echo 'Installing service…'
sudo chmod 777 -R $PWD
sudo systemctl daemon-reload
sudo systemctl enable backgroundchanger.service
sudo systemctl stop backgroundchanger.service
sudo systemctl daemon-reload
sudo systemctl start backgroundchanger.service
echo 'Installiert.'
