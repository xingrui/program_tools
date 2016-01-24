rm -rfv PDO_PGSQL-1.0.2*
wget http://pecl.php.net/get/PDO_PGSQL-1.0.2.tgz
tar xzvf PDO_PGSQL-1.0.2.tgz
cd PDO_PGSQL-1.0.2
/usr/local/php/bin/phpize
./configure -with-php-config=/usr/local/php/bin/php-config --with-pdo-pgsql
#./configure -with-php-config=/usr/local/php/bin/php-config --with-pdo-mysql=/usr/bin
make
make install
#/data/jackson/program_tools/storages/redshift/php/PDO_PGSQL-1.0.2/modules/pdo_mysql.so
