import pika

params = pika.URLParameters(
    "amqps://ounebdmh:wziqnmaX5KIrfFDiUI-0ttDdwoxQBkw3@sparrow.rmq.cloudamqp.com/ounebdmh"
)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic.publish(exchange="", routing="admin", body="hello")
