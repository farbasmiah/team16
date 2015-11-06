#!/bin/sh -x
##############INSTALLING REQUIREMENT########################################
echo Installing all requirement
yum -y install python-pip
yum -y install lftp
yum -y install epel-release
yum -y install python-pip httpd mod_wsgi
pip install virtualenv

cd /home/localuser/
git clone "https://github.com/farbasmiah/team16.git"
mv -f team16 newsite
cd /home/localuser/newsite/
virtualenv env
source env/bin/activate
env/bin/pip install Django==1.8.6
deactivate
python manage.py makemigrations
python manage.py migrate

echo Create Admin User
python manage.py createsuperuser

echo Collecting Static
python manage.py collectstatic

echo Configuring django.conf file
cp -f /home/localuser/newsite/config /etc/httpd/conf.d/django.conf

echo Set apache permission
usermod -a -G localuser apache

echo Set dir permission
chmod -R 777 /home/localuser/newsite

echo Set db permission
chmod 777 /home/localuser/newsite/loginapp.sqlite

#echo Chowning
#chown :apache /home/localuser/newsite/loginapp.sqlite
#chown :apache /home/localuser/newsite

echo Try starting apache
systemctl start httpd

echo Enabled apache
systemctl enable httpd 
