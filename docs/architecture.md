\# Enterprise PAM Security Lab — Architecture



\## 1. Project Overview



This project demonstrates a simulated Privileged Access Management (PAM) policy engine for controlling administrative access to sensitive resources.



The lab evaluates user identity, assigned roles, resource permissions, approval status, and requested access duration. Every access decision is recorded in a local JSON Lines audit file.



\*\*Project status:\*\* Local prototype; not a production PAM deployment.



\## 2. Business Objective



The objective is to reduce the risk of unauthorized privileged access by applying least privilege, approval checks, time-bound authorization metadata, and auditable access decisions.



\## 3. Architecture Components



\- \*\*Users:\*\* Fictional Engineer, Auditor, and PAM Administrator identities.

\- \*\*Policy Engine:\*\* Python application that evaluates access requests.

\- \*\*RBAC Policy:\*\* Defines which roles can request access to specific resources.

\- \*\*Approval Check:\*\* Denies requests without approval.

\- \*\*Duration Validation:\*\* Accepts requested durations between 1 and 60 minutes.

\- \*\*Expiry Validation:\*\* Checks whether a simulated access grant has passed its expiry timestamp.

\- \*\*Audit Trail:\*\* Records access decisions in `evidence/audit.jsonl`.

\- \*\*Automated Tests:\*\* Python unit tests validate expected allow and deny decisions.



\## 4. Access Decision Flow



1\. Receive an access request.

2\. Identify the requesting user's assigned role.

3\. Verify that the requested resource exists.

4\. Check whether the role is authorized for that resource.

5\. Check the approval flag.

6\. Validate the requested duration.

7\. Record the decision, reason, timestamp, request ID, and applicable expiry timestamp.

8\. Evaluate the expiry status when checking an existing simulated grant.



\## 5. Example Access Policy



| Role | Production Server | Audit Logs | PAM Policies |

|---|---|---|---|

| Engineer | Allowed subject to approval | Denied | Denied |

| Auditor | Denied | Allowed subject to approval | Denied |

| PAM Administrator | Allowed subject to approval | Allowed subject to approval | Allowed subject to approval |



These are illustrative lab policies, not a recommended universal production policy.



\## 6. Audit Events



Each event includes:



\- Request ID

\- UTC timestamp

\- Username and assigned role

\- Requested resource

\- Approval flag

\- Requested duration

\- Expiry timestamp, when allowed

\- Allow or deny decision

\- Decision reason



\## 7. Security Boundaries and Limitations



This prototype does not authenticate real employees, independently verify approver identities, create server sessions, store privileged passwords in a secure vault, rotate credentials, or automatically terminate real sessions.



The approval flag is supplied as a test input. The audit file is locally writable and is not tamper-proof.



MFA, credential vaulting, session recording, centralized log collection, and production identity integration are design considerations for a future BeyondTrust-aligned implementation.



\## 8. Proposed Enterprise Integration



In a production design, an authorized PAM platform such as BeyondTrust Password Safe or Privileged Remote Access would enforce supported privileged-access controls. Centralized monitoring, identity integration, secure credential handling, session auditing, and operational ownership would require separate configuration and validation.



This project does not claim a direct BeyondTrust product integration.



