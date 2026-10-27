# Architecture

## Overview

The production system is split into two user experiences.

1. **LINE interface for members**
   - low-friction entry point
   - registration, payment checks, expense applications, event information
2. **Web management UI for officers**
   - member management
   - accounting and collections
   - approvals and operational work

## Request flow

```text
Member
  ↓
LINE Official Account
  ↓
LINE Messaging API
  ↓
Webhook
  ↓
Flask application
  ↓
SQLite
  ↓
Reply / Admin UI
```

## Why this architecture

The circle already used LINE for everyday communication. Rather than introduce another app and create adoption friction, the system uses LINE as the member-facing interface and a dedicated web UI only where richer administrative operations are necessary.

## Data model concept

Core entities in production include:

- members
- collections
- payments
- expenses
- accounting units

Relations allow the system to answer questions such as:

- Which member has paid which collection?
- Which expense belongs to which accounting unit?
- Which payments are overdue?
- What is the current balance of each accounting unit?

## Authentication concept

The management UI is restricted to users whose member record has an admin role.

A signed, time-limited token is generated from LINE for eligible admins. The web application validates the token and then creates an authenticated session.

## Portfolio note

This repository intentionally contains simplified representative code instead of the full production source. Sensitive operational details, production URLs, user data and secrets are excluded.
