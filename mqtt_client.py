import paho.mqtt.client as mqtt
from faucet import Faucet
from faucet_state import FaucetState

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

def on_message(client, userdata, msg):
    state = FaucetState(msg.payload.recv(1024).decode())
    print(state.name)
    # print(msg.topic + " " + str(msg.payload))  


def main():
    broker_address = "192.168.31.11"
    broker_port = 1883

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(broker_address, broker_port)  


    # Publish a message
    client.publish("topic/test", "Hello from the client!")

    # Subscribe to a topic
    client.subscribe("halo")

    client.loop_forever()

if __name__ == "__main__":
    main()
