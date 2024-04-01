import etcd3

client = etcd3.client(host='localhost' , port = 2379) #creating a client pointer to access etcd database

def getAllKeys(): #function creation to genarate only keys
  for key in client.get_prefix('' , keys_only = True): 
    print(f"Key : {key.decode()}") #printing all keys in the node/database

getAllKeys()
