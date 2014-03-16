rm -rf ./MALNotifier-master
rm -f ./master.zip
wget https://github.com/michboon/MALNotifier/archive/master.zip
unzip master.zip
sudo rm -rf /var/www/*
sudo cp -r ./MALNotifier-master/www/* /var/www
sudo chmod +x /MALNotifier-master/scripts/update.sh

cd ./MALNotifier-master/scripts
mysql -u root --password=root -e 'DROP DATABASE IF EXISTS MALNotifier;'
mysql -u root --password=root < create_tables.sql

sudo chmod -R 777 /var/www
