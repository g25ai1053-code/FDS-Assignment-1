# src/adversary.py

from node import ConsensusNode
import asyncio

class AdversaryNode(ConsensusNode):

    async def start(self):
        print(f"Adversary Node {self.node_id} started in Mode B")

        while True:
            await self.pbft_prepare({})
            await self.pbft_commit({})
            await asyncio.sleep(3)

    async def pbft_prepare(self, request):
        print(f"Adversary {self.node_id} equivocating during Prepare phase")

    async def pbft_commit(self, request):
        print(f"Adversary {self.node_id} suppressing Commit message")


if __name__ == "__main__":
    node = AdversaryNode(99, [], "B")
    asyncio.run(node.start())