## READ ME

### Update

This project is temporarily closed beacause of high cost(time, and my patient) of maitaining.

I'll try some new method to screen the data from original website, using selenium and phantomjs in new version of bjmemc.py

### Usage (discarded)
bjmemc.py is a crawler to get data from zx.bjmemc.com.cn（北京市环境保护监测中心）

using mongodb to store data,using celery to maintain the daily crawler's task queue

how to use bjmemc:
	
	# start redis
	D:\env\redis\>redis-server
	# start mongodb
	D:\env\mongodb\bin\>mongod.exe --dbpath E:\mongodata\airstation\db
	# start celery worker
	D:\>celery -A test_celery worker --loglevel=info
	# start celery beat
	D:\>celery beat
