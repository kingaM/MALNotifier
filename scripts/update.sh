rm -rf ./MALNotifier-master
rm -f ./master.zip
wget https://github.com/michboon/MALNotifier/archive/master.zip
unzip master.zip
sudo rm -rf /var/www/*
sudo rm -rf /var/scripts/*
sudo rm -rf /var/backend/*
sudo cp -r ./MALNotifier-master/www/* /var/www
sudo cp -r ./MALNotifier-master/scripts/* /var/scripts
sudo cp -r ./MALNotifier-master/backend/* /var/backend
sudo chmod +x ./MALNotifier-master/scripts/update.sh

# cd ./MALNotifier-master/scripts
# mysql -u root --password=root -e 'DROP DATABASE IF EXISTS MALNotifier;'
# mysql -u root --password=root < create_tables.sql

sudo chmod -R 777 /var/www
