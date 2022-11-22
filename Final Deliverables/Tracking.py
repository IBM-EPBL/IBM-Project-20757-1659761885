import json
import wiotp.sdk.device
import time

myConfig ={
    "identity":{
    "orgId": "t1sqja",
    "typeId":"NodeMCU",
    "deviceId":"12345"
    },
    "auth":{
        "token":"12345678"
       }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    name="locater"
    #in area location
    latitude=11.114778283092631
    longitude=77.1881467129582

    #out area location
    #latitude=11.123452065028367          
    #longitude=77.1768449916141
    
    myData={'name':name, 'lat':latitude, 'lon':longitude}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Data published to IBM Iot platform: ",myData)
    time.sleep(2)
    
client.disconnect()
