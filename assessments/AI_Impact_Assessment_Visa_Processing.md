# AI Impact Assessment (AIA): Automated Document Verification
**Project:** Integration of Generative AI in Visa/Identity Processing  
**Assessor:** Kaustubh Banerjee  
**Status:** Simulated / Portfolio Project  

---

### **1. System Description**
The system utilizes a Large Language Model (LLM) and Computer Vision to automate the initial screening of visa application documents, checking for consistency between applicant-provided data and official government-issued identity documents.

### **2. Regulatory Context**
Under the **EU AI Act**, this system is classified as **"High-Risk"** because it pertains to the evaluation of individuals for legal status and migration. 

### **3. Identified Risks & Mitigation Strategies**

| Risk Category | Identified Risk | Mitigation Strategy (Governance) |
| :--- | :--- | :--- |
| **Algorithmic Bias** | AI may misinterpret non-standard fonts or regional document formats. | **Human-in-the-Loop (HITL):** All "Rejected" flags must be audited by a Senior Operations Officer. |
| **Data Privacy** | PII leakage into the model's training data or cache. | **Data Minimization:** Implementation of a PII-Scrubber to redact sensitive fields before model processing. |
| **Hallucination** | AI may fabricate "missing" information if the scan is blurry. | **Threshold Controls:** System is restricted to "Classification only"; no generative fields allowed. |

### **4. Compliance Audit Trail**
- **ISO 27001 Alignment:** A.18.1.1 (Compliance with legal requirements).
- **Article 9 Compliance:** Maintains a continuous risk management system.

---
*This document serves as a blueprint for implementing secure, ethical AI in global mobility operations.*
