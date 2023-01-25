from opcua import Client
import time
from random import randint

url ="opc.tcp://localhost:4845"

client = Client(url)
client.connect()

print("OPC UA Client connected")


tags = []
tags_number = 6

for i in range(2, tags_number + 1 ):
    var = {
            "nodeid":"ns=2;i=" + str(i),
            "name":
                    str(client.get_node("ns=2;i=" + str(i)).get_description().Text),
            "value":   
                    client.get_node("ns=2;i=" + str(i)).get_value()
                    }
    tags.append(var)

print(tags)

while True:
    for j in range(0,len(tags)):
        
        print("\n" + tags[j]["name"])
        print(tags[j]["nodeid"] + ":\n" + str(client.get_node(tags[j]["nodeid"]).get_value()))


    client.get_node(tags[2]["nodeid"]).set_value(randint(0, 100))

        

    time.sleep(2)
