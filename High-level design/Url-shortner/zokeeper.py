from kazoo.client import KazooClient
import time
import uuid
import threading


class TokenManagementService:
    def __init__(self, zk_hosts):
        self.zk = KazooClient(hosts=zk_hosts)
        self.zk.start()
        self.running = False
        self.leader = False

    def register_service(self):
        self.zk.ensure_path("/token_management")
        self.zk.create("/token_management/service_", ephemeral=True, sequence=True)

    def start_leader_election(self):
        @self.zk.DataWatch("/token_management")
        def watch_leader(data, stat):
            all_services = self.zk.get_children("/token_management")
            all_services.sort()
            if all_services[0] == self.zk.client_id[0]:
                self.leader = True
                print("I am the leader!")
            else:
                self.leader = False
                print("I am not the leader!")

    def generate_token(self):
        if self.leader:
            # Generate a unique token (e.g., using UUID)
            token = str(uuid.uuid4())
            print("Generated token:", token)
            return token
        else:
            print("Cannot generate token. Not the leader.")

    def start(self):
        self.register_service()
        self.start_leader_election()
        self.running = True

    def stop(self):
        self.running = False
        self.zk.stop()


if __name__ == "__main__":
    zk_hosts = '127.0.0.1:2181'  # ZooKeeper server address

    token_service = TokenManagementService(zk_hosts)
    token_service.start()


    # Simulate token generation requests
    def generate_tokens():
        while token_service.running:
            token_service.generate_token()
            time.sleep(5)


    # Start token generation threads
    token_thread = threading.Thread(target=generate_tokens)
    token_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        token_service.stop()
        token_thread.join()
