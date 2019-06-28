from kafka import KafkaProducer
from websocket import create_connection
import json

ws = create_connection("wss://ws.blockchain.info/inv")
ws.send("""{"op":"unconfirmed_sub"}""")
 
bootstrap_servers = ['localhost:9092']
topicName = 'myTopic'
 
producer = KafkaProducer(bootstrap_servers = bootstrap_servers)
producer = KafkaProducer()


while True:
    tx = ws.recv()
    data=json.dumps(tx)
    ack = producer.send(topicName, data.encode('utf-8'))
    print ("",ack)    
    metadata = ack.get()


