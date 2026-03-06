# Standard Operating Procedure (SOP): AI Incident Response
**Subject:** Managing Model Hallucinations and Data Security Incidents  
**Author:** Kaustubh Banerjee  
**Version:** 1.0 (2026)  

---

### **1. Scope & Objective**
To provide a structured protocol for identifying, containing, and remediating incidents involving Generative AI systems, ensuring minimal disruption to global identity operations and maintaining compliance with **GDPR** and the **EU AI Act**.

### **2. Incident Classification**

| Severity | Incident Type | Action Required |
| :--- | :--- | :--- |
| **P1: Critical** | PII Leakage / Prompt Injection | Immediate system suspension; Data Protection Officer (DPO) notification within 72 hours. |
| **P2: High** | Hallucination in Legal Advice / Visa Checks | Redirection to Human-in-the-Loop (HITL) manual audit; log entry for model retraining. |
| **P3: Medium** | Model Drift / Latency Issues | Performance monitoring and parameter adjustment during off-peak hours. |

### **3. Remediation Workflow**
1. **Detection:** Automated monitoring flags an anomaly in the AI output confidence score.
2. **Triaging:** Senior Operations Lead (Human-in-the-Loop) verifies the hallucination or breach.
3. **Containment:** If a breach is confirmed, the specific API endpoint is disabled.
4. **Root Cause Analysis (RCA):** Evaluating whether the issue was in the *Prompt Engineering* or the *Underlying Model*.
5. **Recovery:** Re-enabling the system after verifying the fix against a "Safe Dataset."

### **4. Regulatory Documentation**
All P1 and P2 incidents must be recorded in the **Incident Log** as required by **Article 12** (Record-keeping) of the EU AI Act.

---
*Operationalizing Trust in Autonomous Systems | Kaustubh Banerjee*
