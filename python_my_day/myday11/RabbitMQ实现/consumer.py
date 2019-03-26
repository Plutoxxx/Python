import pika, time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))
channel = connection.channel()

# You may ask why we declare the queue again ‒ we have already declared it in our previous code.
# We could avoid that if we were sure that the queue already exists. For example if send.py program
# was run before. But we're not yet sure which program to run first. In such cases it's a good
# practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello4', durable=True)

channel.basic_qos(prefetch_count=1) #消费者没处理完时不接收新的信息
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # time.sleep(30)



channel.basic_consume(callback,
                      queue='hello4',
                      no_ack=True
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()