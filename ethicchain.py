"""
EthicChain - Gouvernance Éthique Dynamique
------------------------------------------
Blockchain simplifiée pour auditabilité éthique et conformité RGPD/AI Act.
"""

import hashlib
import time

class EthicBlock:
    def __init__(self, index, previous_hash, decision, validator="EthicNode"):
        self.index = index
        self.timestamp = time.time()
        self.decision = decision
        self.previous_hash = previous_hash
        self.hash = self.compute_hash()
        self.validator = validator

    def compute_hash(self):
        payload = f"{self.index}{self.timestamp}{self.decision}{self.previous_hash}"
        return hashlib.sha256(payload.encode()).hexdigest()

class EthicChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return EthicBlock(0, "0", "Genesis Decision")

    def add_decision(self, decision):
        prev = self.chain[-1]
        block = EthicBlock(len(self.chain), prev.hash, decision)
        self.chain.append(block)
        return block

if __name__ == "__main__":
    chain = EthicChain()
    chain.add_decision("Consent donné")
    chain.add_decision("Rollback ΔM11.3 validé")
    for b in chain.chain:
        print(b.index, b.decision, b.hash[:8])
