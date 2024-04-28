import pika

def publish_message(message):
    # Establish connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue for sending messages
    channel.queue_declare(queue='user_created')

    # Publish the message
    channel.basic_publish(exchange='', routing_key='user_created', body=message)

    # Close connection
    connection.close()

if __name__ == "__main__":
    # Example usage
    message = "New user created"
    publish_message(message)
