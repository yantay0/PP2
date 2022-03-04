import json

f = open("/Users/Madina/Desktop/PP2/labs/lab4/json/sample.json")

data=json.loads(f.read())

print("Interface Status" , '='*82, sep='\n')
print("DN", " "*49, "Description" , " "*11 , "Speed" , " "*3 , "MTU" )
print("-"*52, "-"*21, " ", "-"*6 , " ","-"*6 , sep=" ")

for i in data["imdata"]:
 dn= i['l1PhysIf']['attributes']['dn']
 descr = i['l1PhysIf']['attributes']['descr']
 speed = i['l1PhysIf']['attributes']['speed']
 mtu = i['l1PhysIf']['attributes']['mtu']
 print(dn ,  " "*32,  descr   , speed  ,  " ", mtu)

 
