import etcd3

def insert_to_etcd():
    # Connect to etcd server
    etcd = etcd3.client(host='127.0.0.1', port=2379)
    
    while True:
        # Prompt user for key and value
        key = input("Enter key (or 'exit' to stop): ")
        if key.lower() == 'exit':
            break
        
        value = input("Enter value: ")
        
        # Insert key-value pair into etcd
        etcd.put(key, value)
        print(f"Inserted: {key} => {value}")

if __name__ == "__main__":
    insert_to_etcd()
