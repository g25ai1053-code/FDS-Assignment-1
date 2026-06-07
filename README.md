# Distributed Consensus Engine (Paxos & PBFT)

## Overview

This project implements a resilient distributed consensus engine designed to maintain a consistent, append-only transaction ledger across a cluster of five nodes. The system is capable of tolerating both crash faults and Byzantine (malicious) faults while preserving data consistency and availability.

## Key Features

* Distributed transaction ledger replicated across 5 nodes
* Crash-fault tolerance using Leader Election and Paxos
* Byzantine-fault tolerance using Practical Byzantine Fault Tolerance (PBFT)
* RSA-based digital signatures for message authentication
* Client workload simulation for testing consensus behavior
* Fault-injection and chaos testing support

## System Architecture

The platform supports two operational modes:

### Mode A – Crash Fault Tolerance

Uses Leader Election and Basic Paxos to ensure consensus despite node failures.

**Capabilities:**

* Handles up to 2 simultaneous node crashes
* Maintains ledger consistency
* Automatically elects a leader when required

### Mode B – Byzantine Fault Tolerance

Uses Practical Byzantine Fault Tolerance (PBFT) together with RSA cryptographic signatures.

**Capabilities:**

* Tolerates 1 malicious (Byzantine) node
* Verifies message authenticity through digital signatures
* Protects the system against tampering and forged messages

## Project Structure

```text
├── src/
│   ├── node.py          # Consensus node implementation
│   ├── adversary.py     # Byzantine fault simulator
│   ├── client.py        # Client transaction generator
│   └── crypto_utils.py  # RSA key generation and signature utilities
├── tests/
│   └── chaos_test.sh    # Fault-injection and resilience testing
├── Dockerfile           # Container configuration
├── docker-compose.yml   # Multi-node cluster orchestration
└── project_report.pdf   # Design, implementation, and evaluation report
```

## Technologies Used

* Python
* Paxos
* PBFT
* RSA Cryptography
* Docker
* Docker Compose
* Toxiproxy (Chaos Testing)

## Objective

To demonstrate how modern distributed systems can achieve reliable consensus and maintain ledger integrity in the presence of both accidental failures and malicious behavior.
