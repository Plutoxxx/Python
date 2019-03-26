import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello4', durable=True) # 确保任务是持久的，即使RabbitMQ服务关闭了也能保存消息

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello4',
                      body='Hello World!',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent确保队列中消息是持久的
                      )
                      )
print(" [x] Sent 'Hello World!'")
connection.close()