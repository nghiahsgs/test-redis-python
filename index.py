import redis
host = '127.0.0.1'
port = '6379'
client = redis.Redis(host=host,port =port)
name = client.get("name")
print('name',name)