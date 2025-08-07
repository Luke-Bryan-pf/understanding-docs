
# Paze Discovery Workshop Guide (StarOne)

This guide provides a simplified breakdown of the content from the "Discovery Workshop (APIs)_StarOne" document to help engineers and QA testers understand the Paze system, API categories, and key flows like webhook validation and certification.

---

## 🔍 What is Paze?

Paze is a **digital wallet and payment system** that allows users to check out online without manually entering card details. The Paze infrastructure connects with various financial institutions (like StarOne) to enable secure transactions.

---

## 🧩 StarOne’s Role in Paze

StarOne is integrating with Paze via APIs. The StarOne core system must respond to requests from Paze and also **emit and respond to events** related to users, wallets, transactions, and fraud detection.

---

## 🏗️ Paze Architecture Overview

### Main Components:
- **API Gateway**: Entry point for all API requests.
- **Core System (StarOne)**: Handles identity, transactions, cards.
- **Webhook System**: Sends outbound events to StarOne's system.

---

## 🔌 Paze API Categories

### 1. Identity & Token
- **WhoIs API**: Identifies users based on an identity key.
- **Token API**: Issues temporary tokens for secure usage.

### 2. Wallet Management
- Retrieve cards
- Enable/disable card toggle
- Eligibility checks

### 3. Transaction APIs
- Log wallet-based transactions
- Fraud event tagging

### 4. Notifications
- **Webhook callbacks** (event-driven)

---

## 🔔 Webhook Events & Validation

### What is a Webhook?
A webhook is a way for Paze to **inform StarOne** when specific events happen.

### Examples of Events:
- Card enabled/disabled
- Transactions completed
- Fraud reported

### Webhook Validation Tasks:
- StarOne must **receive** the webhook payload.
- StarOne must **respond with 200 OK**.
- The response **must be timely** (within SLA).
- StarOne should **validate payload contents**.
- **Security**: Use of shared secret/signature to confirm origin.

---

## 🧪 Certification Testing

Paze provides a **certification suite** that StarOne must pass to go live.

### Key Tests:
- Valid WhoIs flow
- Card retrieval & toggle
- Simulated fraud
- Webhook receipt & validation

---

## 🛠️ Automation Opportunities

- Use **mock APIs** to simulate real core behavior.
- Validate that your **webhook receiver** can handle all events.
- Use **pytest or Postman** for automated API test flows.

---

## 📘 Summary

The document is meant to:
- Prepare you to test Paze + StarOne integration.
- Understand webhook flow handling.
- Support eventual automation of Paze certification.

---

