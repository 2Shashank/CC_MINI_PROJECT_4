import etcd3

def get_value_for_key(client, key):
    value = client.get(key)  # Get the value of the specified key
    
    # Check if the key exists and return its value
    if value is not None:
        return value[0].decode()
    else:
        return None

def main():
    client = etcd3.client(host = "localhost" , port = 2379) # Connect to etcd server
  
    key = input("Enter the key: ") #specific key from user

    value = get_value_for_key(client, key) # Get value for the specified key

    if value is not None:
        print(f"The value of key '{key}' is: {value}") # Print the value of the key
    else:
        print(f"Key '{key}' not found.")

if __name__ == "__main__":
    main()
