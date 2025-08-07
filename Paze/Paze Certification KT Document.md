
# 📄 Paze Certification – Knowledge Transfer Summary

## 🧠 Purpose of the Document
This document explains how the **Paze Certification framework** is built and how it works, primarily for **testing and automating certification flows**. It provides a high-level overview of key components, structure, tools, and test scenarios involved.

------

## 🏗️ Architecture Overview

### 🔹 Core Stack:
- **Backend:** FastAPI
- **Frontend:** React (used for the WebTool interface)
- **Automation:** Python + Pytest + Playwright (for headless browser testing)
- **Security:** OAuth 2.0, JWE (JSON Web Encryption)
- **Database:** PostgreSQL

> All certification flows and tests run through a local FastAPI-based backend and trigger automated headless UI tests using Playwright.

---

## 📁 Directory Structure

```
.
├── backend/             # FastAPI codebase (API logic)
├── frontend/            # React app for test input UI
├── playwright/          # Certification tests (Playwright-based)
│   ├── flows/           # Certification test flows
│   ├── testdata/        # Dynamic test data JSON files
│   ├── utils/           # Helper methods and page classes
├── wallet-certification-api/ # Reusable APIs and core features
```

---

## 🧪 Certification Test Flows

### ✅ Primary Use Cases Covered:
1. **Add Card to Wallet**
2. **Delete Card**
3. **Update Card Status (ON/OFF)**

> Each flow can be run individually via the UI or CLI, and uses environment-specific test data.

### 🛠️ Supporting Tools
- **WebTool:** Helps trigger test flows manually via a browser.
- **Postman:** Used to validate endpoints for Wallet Management APIs.

---

## 🔐 Security & Tokens

- Uses **OAuth 2.0** for access token generation.
- Sensitive payloads are **JWE encrypted**.
- Salt version and key IDs are used to rotate secrets for enhanced security.

---

## 🔄 Wallet Management APIs

These APIs are part of the Certification tests:

| Endpoint | Purpose |
|----------|---------|
| `/addCard` | Adds a new card |
| `/deleteCard` | Deletes a card |
| `/updateCardStatus` | Toggle ON/OFF |
| `/walletStatus` | Check wallet readiness |
| `/userDetails` | Fetch user identity info |

> These APIs are tested against different environments and issuers.

---

## 📂 Test Data Structure

Test data for each issuer is stored as JSON in `testdata/`. Example format:

```json
{
  "issuer": "StarOne",
  "environment": "cert",
  "userId": "test-user-001",
  "cards": ["4001", "4002"]
}
```

Each test dynamically pulls from this JSON during runtime.

---

## 🧰 Utilities and Helpers

Inside `utils/` you’ll find:
- **CommonRequestBuilder:** Build standard headers and payloads
- **WalletPages:** Page Object Model for UI flows (Playwright)
- **JsonUtils:** Load & parse test data JSONs

---

## 🌐 WebTool (React Frontend)

- Allows testers to input test params from browser.
- On submit → triggers backend which executes the certification test in headless mode.
- Helpful for non-technical testers.

---

## 🧾 Checklist for Understanding

- [x] Reviewed API endpoints and what each does
- [x] Understood security flow (JWE + OAuth)
- [x] Learned test data structure & environment configs
- [x] Know where test flows are triggered from (backend / frontend)
- [x] Understood how Playwright is used for automation

---

## 📌 What You’ll Automate Later

Once you’re ready to write automation, you’ll be working on:
- Writing/Modifying flows in `playwright/flows/`
- Creating new test data in JSON format
- Reusing existing API methods and utility functions
- Adding test verification in the WebTool or CLI

---

## 📚 Useful References

- Paze Discovery Doc
- Paze Wallet Management API Specification
- Paze Certification KT Doc (This)
- Paze Postman Collection
- FastAPI + React App (for triggering tests)

---
