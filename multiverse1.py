import time
import json
import paho.mqtt.client as mqtt
THINGSBOARD_HOST="demo.thingsboard.io"
ACCESS_TOKEN="pCtang0rgNFepOSsaEEj"
light_data={"status":False,"time":time.asctime()}
client=  mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST,1883)
client.loop_start()
try:
  while True:
    light_data['status']=true if input("Enter input:")=="Y" else False
    light_data['time']=time.asctime()
    print(str(light_data))        
    client.publish("v1/devices/me/telemetry",json.dumps(light_data))
    time.sleep(1)
except KeyboardInterrupt:
  pass
  client.loop_stop()
  client.disconnect()