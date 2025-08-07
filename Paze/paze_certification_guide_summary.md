
# Paze Certification Guide – Summary

This guide explains all the test cases, requirements, and validations issuers must complete to certify their integration with Paze Wallet.

---

## 🔐 Core Goals of Certification

- Prove API integration is secure and functional.
- Validate onboarding, provisioning, and identity handling.
- Ensure proper consumer info updates and fraud handling.
- Confirm webhook notifications and lifecycle events work correctly.

---

## 🧪 API Testing Requirements

### 1. **Connectivity**
- Ensure secure connection using `/getSalt`, `/addCard`, `/getWalletDetails`.

### 2. **Provisioning Tests**
- Add existing and new cards successfully.
- Bulk provision multiple cards without errors.
- Retrieve wallet details and verify card info.

### 3. **Card & Wallet Info Updates**
- Update consumer **name**, **billing address**, **email**, **phone**.
- Use `/updateWalletDetails` and validate via `/getWalletDetails` and `/getWalletAliases`.

### 4. **Remediation & Salt Handling**
- React to `salt_compromised` and regenerate identityKeys.
- Use new salt via `/getSalt`, then `/updateIdentityKeys`.
- Receive system notifications (`identity_key_activities_disabled`, etc.).

---

## ✅ Eligibility Checks for Card Provisioning

Make sure users meet these criteria:
- Signed in within 365 days
- Valid email and U.S. address
- U.S. mobile number (not toll-free)
- At least 18 years old
- No confirmed fraud in 45 days
- Card is active and eligible for tokenization
- Card used for e-commerce or opened in last 180 days
- Card issued to primary/joint cardholder

---

## 🔁 Lifecycle Scenarios

- Card Expiration Update
- Card Product Upgrade
- Account Closure & Token Deletion
- Card Suspension & Reactivation

---

## 👁️‍🗨️ UI Verification

- Confirm cards are shown/hidden in Wallet UI
- Add/delete cards and verify state in UI
- Wallet states: `active`, `unclaimed`, `restricted`, `deleted`, `suspended`

---

## 🔔 Webhook Notifications

Test transitions with webhook alerts:
- `Active → Deleted`
- `Active → Unclaimed`
- `Active → Restricted → TempSuspended`
- `Unclaimed → Active`

Each should trigger a webhook notification to the issuer.

---

## ⚠️ Fraud Testing

- Multiple fraud claims → restrict or delete wallet
- Fraud file triggers state change to `Restricted` or `Deleted`
- Token deletions must follow fraud handling rules

---

## 📄 Required Forms & Confirmations

- Submit attestation forms (e.g., BIN eligibility, fraud analytics data)
- Email confirmations for various steps (salt storage, etc.)

---

## 🧪 Special Tests

- Wallet purge if identityKey not updated within 14 days after salt compromise
- Resume operations with `identity_key_activities_reenabled`
- Add optional fields like `saltVersion`, `hashingChecksumHashValue` – will be required later

---

## 🧰 Tools & URLs for Testing

- Wallet Management: https://mywallet-management.wallet.cat.earlywarning.io
- Checkout Demo: https://sandbox.digitalwallet.earlywarning.com/demo
- Auth URLs: (CAT Environment)
  - `https://auth.wallet.cat.earlywarning.io`
  - `https://mtls.auth.wallet.cat.earlywarning.io`

---

## ✅ Final Requirements for Completion

You must:

- Execute all test cases
- Handle all webhook events properly
- Validate provisioning rules
- Respond to all notifications
- Submit final forms to Early Warning Services (EWS)

---

## 📬 Questions?

Contact: `Issuerimplementation@paze.com`

---

**Note**: Every step is tracked by EWS and must pass for production go-live.
