# test-redis-python
test redis python


### STEP 1: install redis on Ubuntu
```
sudo apt update
sudo apt install redis-server
```

Mở tưởng lửa qua cổng 6379
```
ufw allow 6379
ufw allow 6379/tcp
```


### STEP 2: Check status redis
```
sudo systemctl status redis
```
### STEP 3: Open cli
```
redis-cli
ping =>pong
```

```
set name "nghiahsgs"
get name
```

```
exit
```

*note dù có reset lại redis, data vẫn còn đó, trừ khi reset cả máy, ram mất thì mất
```
sudo systemctl restart redis
redis-cli
get name
```

### STEP 4: Dùng python kết nối
```python
import redis
import timeprotected-mode no

host = '127.0.0.1'
port = '6379'
client = redis.Redis(host=host,port =port,charset='utf-8',decode_responses=True)
name = client.get("name")
print('name',name)
print(client.ttl("name"))


client.set("name","nghiahsgs2",px=10000)
print('name',client.get("name"))
print(client.ttl("name"))

time.sleep(2)

print('name',client.get("name"))
print(client.ttl("name"))
```

### STEP 5: Cho phép kết nối từ xa (mặc định chỉ cho kết nối từ localhost)
```
vi /etc/redis/redis.conf
Sửa bind 127.0.0.1 thành bind 0.0.0.0
Sửa protected-mode yes thành protected-mode no
```

```
sudo systemctl restart redis
```

