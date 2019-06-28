from kafka import KafkaConsumer
import json
import redis
from datetime import datetime
import random
import string

redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)

 
bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
 
consumer = KafkaConsumer (topicName, group_id = 'group1',value_deserializer=lambda m: json.loads(m.decode('utf-8')),
bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest')
consumer.subscribe(['myTopic'])
for message in consumer:
    random_gen = ''.join(random.sample(string.ascii_uppercase, 6))
    transaction_data=json.loads(message.value)
    time=str(transaction_data['x']['time']) +'-'+ str(random_gen)
    data=message.value
    redis_db.set(time, data)
    redis_db.expire(time, 10800) 
    redis_db.lpush('last100',str(transaction_data))
    redis_db.ltrim('last100',0,99)
    k = redis_db.get(time)
    print('###############{}'.format(time))

 
