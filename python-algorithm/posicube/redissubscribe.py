import redis

# Redis 클라이언트 설정
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# 구독하려는 채널 지정
channel_name = 'VECDSAH'

# Redis Pub/Sub 시스템에 연결
pubsub = redis_client.pubsub()
pubsub.subscribe(channel_name)

# 메시지를 받기 위한 루프
print(f"Subscribing to channel {channel_name}.")
try:
    for message in pubsub.listen():
        # 메시지가 수신될 때 처리할 작업
        if message['type'] == 'message':
            print(f"Message received: {message['data'].decode('utf-8')}")
except KeyboardInterrupt:
    print("Unsubscribing and exiting...")
    pubsub.unsubscribe(channel_name)
    pubsub.close()