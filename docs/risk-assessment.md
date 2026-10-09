\# PAM Security Lab — Risk Assessment



\## 1. Purpose



This assessment identifies key risks associated with privileged access and proposes security controls for a BeyondTrust-aligned enterprise PAM architecture.



The likelihood and impact ratings below are qualitative estimates for this learning project, not measured production risk ratings.



\## 2. Risk Register



| ID | Risk | Likelihood | Impact | Proposed Mitigation |

|---|---|---|---|---|

| R-01 | Administrator credentials are compromised | High | Critical | MFA, credential vaulting, rotation, least privilege |

| R-02 | Unauthorized privilege escalation | Medium | Critical | RBAC, approval workflows, separation of duties |

| R-03 | Access remains usable after expiry | Medium | High | Enforced session expiry, revocation, automated testing |

| R-04 | Audit records are modified or deleted | Medium | High | Centralized logging, restricted write permissions, protected retention |

| R-05 | Excessive privileges accumulate over time | High | High | Periodic access reviews and joiner-mover-leaver processes |

| R-06 | Service-account secrets are exposed | Medium | Critical | Approved secrets vault, rotation, restricted secret retrieval |

| R-07 | Approval is falsified or bypassed | Medium | High | Authenticated approvers, separation of duties, approval audit trails |



\## 3. Current Prototype Findings



\### Finding 1: Approval is simulated



The application accepts an approval Boolean as input. It does not independently authenticate an approver or verify an approval workflow.



\*\*Mitigation:\*\* Integrate an authenticated approval mechanism and enforce separation of duties in a production implementation.



\### Finding 2: Expiry is not enforced on a real session



The application records an expiry timestamp and checks whether a simulated grant remains valid. It does not establish or terminate a server session.



\*\*Mitigation:\*\* Enforce expiry and revocation through the privileged-access platform and target-system controls.



\### Finding 3: Audit file is locally writable



The JSONL audit file provides useful demonstration evidence but is not tamper-proof.



\*\*Mitigation:\*\* Forward security events to a protected central logging platform and restrict modification and deletion privileges.



\### Finding 4: No real credential vault is configured



The prototype does not store or rotate actual privileged credentials.



\*\*Mitigation:\*\* Use an approved PAM credential vault and validate credential rotation and retrieval policies.



\## 4. Residual Risk



Risk remains until proposed controls are implemented, tested, and assigned operational owners. The local simulator must not be used to authorize real privileged access.



\## 5. Review and Ownership



A production deployment should assign owners for:



\- PAM policy management

\- Privileged identity lifecycle

\- Credential rotation and recovery

\- Audit monitoring and incident response

\- Periodic access reviews

\- Security exceptions and remediation tracking



\## 6. Assessment Scope



This is a qualitative learning exercise. It is not a formal enterprise risk assessment, penetration test, or compliance certification.



