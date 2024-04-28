import pika

def callback(ch, method, properties, body):
    print("Received message:", body)

def start_consuming():
    # Establish connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue for receiving messages
    channel.queue_declare(queue='user_created')

    # Subscribe to the queue and start consuming messages
    channel.basic_consume(queue='user_created', on_message_callback=callback, auto_ack=True)

    print('Waiting for messages...')
    channel.start_consuming()

if __name__ == "__main__":
    # Start consuming messages
    start_consuming()