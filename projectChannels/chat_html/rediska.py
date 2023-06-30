import redis, json

test_data = redis.Redis()
test_data.set('k','johan')
print(test_data.get('k'))
print(test_data.get('k').decode())
