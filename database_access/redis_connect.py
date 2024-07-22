import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair
r.set('foo', 'bar')

value = r.get('foo')
print(value)

r.incr('counter')

r.append('foo', 'barz')

values = r.mget(['foo', 'counter'])
print(values)

r.hset('myhash', 'field1', 'value1')
r.hset('myhash', 'field2', 'value2')
hash_values = r.hgetall('myhash')
print(hash_values)
