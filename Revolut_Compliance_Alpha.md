# Strategic Compliance Assessment: AI-Driven Retail Lending
**Target Entity:** Revolut (Retail Product Ecosystem)
**Author:** Kaustubh Banerjee (Senior GRC Lead)
**Date:** March 2026

## Executive Summary
This document outlines the GRC (Governance, Risk, and Compliance) requirements for implementing an automated, AI-driven credit scoring system for Revolut’s Retail "Pay Later" products. It maps operational controls directly to the **EU AI Act (2026)** and **ISO 27001**.

---

## 1. Classification & Regulatory Mapping (EU AI Act)
**Risk Category:** High-Risk AI System (Annex III, Point 5b - Creditworthiness Assessment).

* **Article 9 (Risk Management System):** We must implement a continuous risk management process. As a Senior Ops Lead, I advocate for a "Human-in-the-Loop" (HITL) override for any credit rejection exceeding a specific Euro threshold to prevent automated bias.
* **Article 10 (Data & Data Governance):** Datasets used for training the lending model must be checked for "Historical Bias." We will apply statistical parity checks to ensure the algorithm does not discriminate based on protected characteristics (Gender, Nationality).

## 2. Operational Control: The "First-Line" Guardrail
To ensure "Compliance-by-Design," we will implement the following technical controls:
* **Automated Audit Logging (Article 12):** Every AI decision must generate a non-repudiable log entry. 
* **Logic Verification:** I recommend a Python-based "Shadow Auditor" script that runs alongside the main model to flag outliers for manual review by the Compliance team.

## 3. Human Oversight & Transparency (Article 13 & 14)
* **Transparency:** Customers must be informed when they are interacting with an AI system. 
* **Interpretable AI (XAI):** The system must provide "Reasoning Tags" for every decision (e.g., "Insufficient transaction history") to comply with the Right to Explanation under GDPR/EU AI Act.

---
**Verification:** This framework aligns with my 25 years of managing high-stakes identity operations, ensuring that automated speed never compromises regulatory integrity.
