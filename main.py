from flask import Flask, render_template
from flask_navigation import Navigation
from flask_mqtt import Mqtt
from flask_socketio import SocketIO
import paho.mqtt.client as mqtt

#create a flask instance
app = Flask(__name__)
nav = Navigation(app)

# initializing Navigations
nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Gfg', 'gfg', {'page': 5}),
])
   
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app)
mqtt_client = mqtt.Client()

# MQTT on_message callback function
def on_message(client, userdata, message):
    payload = message.payload.decode()
    socketio.emit('mqtt_message_elecmarket', payload)
@app.route("/")
def index():
    
    return render_template(
        'base2.html' )

# MQTT configuration: modify them accordingly
mqtt_broker_address = '199.2.100.199'
mqtt_broker_port = 4883
mqtt_username = 'X'
mqtt_password = 'XXX'
mqtt_topic = '#'

mqtt_client.username_pw_set(username=mqtt_username, password=mqtt_password)
mqtt_client.on_message = on_message
mqtt_client.connect(mqtt_broker_address, mqtt_broker_port)
mqtt_client.subscribe(mqtt_topic)
mqtt_client.loop_start()

if __name__ == '__main__':
    socketio.run(app)