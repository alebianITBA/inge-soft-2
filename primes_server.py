import sys
import primes
import pika

read_queue_name = sys.argv[1]
write_queue_name = sys.argv[2]

primes_gen = primes.primes_gen()

connection = pika.BlockingConnection()
channel = connection.channel()

channel.queue_declare(queue = read_queue_name)
channel.queue_declare(queue = write_queue_name)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    amount = int(body)
    for n in range(amount):
        channel.basic_publish(exchange = '', routing_key = write_queue_name, body = str(primes_gen.next()))

channel.basic_consume(callback, queue = read_queue_name, no_ack = True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
