import Pyro5.api

def main():
    product_keys = ["product.p1", "product.p2", "product.p3"]
    base_uri = "PYRO:{}@localhost:9090"

    print("=== Java RMI Client via Pyro5 ===")
    print("Connecting to remote objects on localhost:9090...\n")

    for key in product_keys:
        uri = base_uri.format(key)
        try:
            with Pyro5.api.Proxy(uri) as product:
                print(f"Remote Object Lookup: {key}")
                print(f"  Name:        {product.getName()}")
                print(f"  Description: {product.getDescription()}")
                print(f"  Price:       ${product.getPrice():.2f}")
                print("-" * 40)
        except Exception as e:
            print(f"Error accessing {key}: {e}")

if __name__ == "__main__":
    main()