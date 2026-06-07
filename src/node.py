import asyncio
import os
from crypto_utils import generate_keys

class ConsensusNode:

    def __init__(self, node_id, peers, mode="A"):
        self.node_id = node_id
        self.peers = peers
        self.mode = mode
        self.private_key, self.public_key = generate_keys()
        self.is_leader = False

    async def heartbeat_sender(self):
        while True:
            if self.is_leader:
                print(f"Leader {self.node_id} sending heartbeat")
            await asyncio.sleep(2)

    async def start(self):
        print(f"Node {self.node_id} starting in Mode {self.mode}")

        if self.node_id == 1:
            self.is_leader = True

        await self.heartbeat_sender()


if __name__ == "__main__":
    node_id = int(os.getenv("NODE_ID", "1"))
    mode = os.getenv("MODE", "A")

    node = ConsensusNode(node_id, [], mode)

    asyncio.run(node.start())