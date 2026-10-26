import Pyro5.api
from product import Product

def start_server():
    daemon = Pyro5.api.Daemon(host="localhost", port=9090)

    # Instantiate products matching the Java RMI repository logic
    p1 = Product("Laptop", "High-performance developer workstation", 1299.99)
    p2 = Product("Smartphone", "Flagship 5G mobile device", 799.50)
    p3 = Product("Headphones", "Noise-cancelling wireless headphones", 199.99)

    # Register each remote object with an identifier
    uri1 = daemon.register(p1, objectId="product.p1")
    uri2 = daemon.register(p2, objectId="product.p2")
    uri3 = daemon.register(p3, objectId="product.p3")

    print("=" * 60)
    print("Pyro5 Java-RMI Translated Server running...")
    print(f"Registered Product 1: {uri1}")
    print(f"Registered Product 2: {uri2}")
    print(f"Registered Product 3: {uri3}")
    print("Ready to receive client requests.")
    print("=" * 60)

    daemon.requestLoop()

if __name__ == "__main__":
    start_server()