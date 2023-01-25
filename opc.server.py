from opcua import Server
from random import randint
import time
import json

## --- Load OPC Data --- ##
jfile = open("./assets/opc.server.data.json")
jdata01 = json.load(jfile)

namespace = jdata01["namespace"]
node_name = jdata01["node_name"]


## --- OPC Settings --- ##
server = Server()
url = "opc.tcp://localhost:4845"
server.set_endpoint(url)

server_namespace = server.register_namespace(namespace)

node = server.get_objects_node()
param = node.add_object(server_namespace, node_name)

# extract the points
variables=[]
for key, value in jdata01.items():
    if isinstance(jdata01[key], list):
        for item in jdata01[key]:
            
            for key2 in item:
                var = param.add_variable(server_namespace,key2, 0)
                var.set_writable()
                var.set_value(item[key2])
                variables.append(var)

                print("key:{}\nvalue: {}".format(key2, item[key2]))


                
                
#temp1 = param.add_variable(server_namespace, "Temperature", 0)
# press = param.add_variable(add_reactor, "Pressure", 0)

# temp1.set_writable()
# press.set_writable()

server.start()

print("OPC UA Server started at {}".format(url))
 
while True:
    #temperature = randint(0, 100)
    #pressure = randint(200, 999)

    # print(temperature, pressure)
    
    #variables[0].set_value(temperature)
    
    # press.set_value(pressure)

    time.sleep(2)

    try:
        
        print(variables[0].get_value())
    except KeyboardInterrupt:
        break
