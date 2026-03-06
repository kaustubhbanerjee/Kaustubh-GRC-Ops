# Visa Background Check Logic (Prototype)
# Purpose: Demonstrates an automated screening workflow with Human-in-the-Loop (HITL)

def screening_agent(applicant_name, document_valid):
    """
    Simulates an AI Agent checking a visa document.
    """
    print(f"[*] Analyzing application for: {applicant_name}")
    
    # Logic: If document is invalid, trigger human review immediately.
    if not document_valid:
        return "REJECTED: Document scan failed clarity check."
    
    # Simulate a background check against a mock database
    risk_score = 15  # Out of 100
    
    if risk_score > 50:
        return "FLAGGED: High-risk score. Transferring to Human Auditor."
    else:
        return "PASSED: Data ready for system entry."

# Example Usage
applicant = "John Doe"
status = screening_agent(applicant, document_valid=True)
print(f"[Result]: {status}")
