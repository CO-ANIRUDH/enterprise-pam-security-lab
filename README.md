\# Enterprise PAM Security Lab



A Python-based Privileged Access Management (PAM) policy simulator demonstrating role-based access control, approval checks, time-bound authorization metadata, audit logging, and automated security testing.



\## Project Objective



Demonstrate how privileged-access policies can reduce unauthorized administrative access and how security architecture, control documentation, and risk assessment support enterprise PAM operations.



\## Architecture



```text

Users

&#x20; |

&#x20; v

PAM Policy Engine

&#x20; |

&#x20; +--> Role-Based Access Control

&#x20; |

&#x20; +--> Approval and Duration Validation

&#x20; |

&#x20; +--> Allow / Deny Decision

&#x20; |

&#x20; v

JSONL Audit Trail

&#x20; |

&#x20; v

Security Testing and Review

```



\## Technology Stack



\- Python 3.14

\- Python unittest

\- JSON Lines audit events

\- Git and GitHub

\- PowerShell



\## Features



\- Role-based access policies for Engineer, Auditor, and PAM Administrator roles.

\- Approval checks for privileged-access requests.

\- Validation of requested access duration.

\- Unique request IDs and UTC timestamps.

\- Expiry timestamps for approved simulated grants.

\- Expiry validity checks.

\- Audit records containing access decisions and reasons.

\- Automated security tests.



\## Project Structure



```text

pam-security-lab/

├── pam\_engine.py

├── tests/

│   └── test\_pam\_engine.py

├── docs/

│   ├── architecture.md

│   ├── security-controls.md

│   └── risk-assessment.md

├── evidence/

│   └── audit.jsonl

└── README.md

```



\## Run the Project



From the project directory:



```powershell

py pam\_engine.py

```



Run automated tests:



```powershell

py -m unittest discover -s tests -v

```



\## Test Coverage



The current test suite validates:



1\. Approved and authorized access.

2\. Unauthorized role denial.

3\. Missing approval denial.

4\. Unknown user denial.

5\. Invalid duration rejection.

6\. Audit-event creation.

7\. Access validity before expiry.

8\. Access invalidity after expiry.



\*\*Latest observed result:\*\* 8 tests passed in the local development environment.



\## Documentation



\- `docs/architecture.md` — architecture and decision flow.

\- `docs/security-controls.md` — security control matrix.

\- `docs/risk-assessment.md` — risks, mitigations, and prototype limitations.



\## BeyondTrust Alignment



The design discusses security controls relevant to BeyondTrust Password Safe and Privileged Remote Access, including privileged access governance, credential protection, approvals, auditing, and session security.



No BeyondTrust product integration has been configured or tested in this project.



\## Limitations



This project is a learning prototype, not a production PAM solution.



\- Approval is represented by a test input and is not independently authenticated.

\- Expiry validation does not terminate real server sessions.

\- No actual privileged credentials are stored or rotated.

\- The local audit file is not tamper-proof.

\- MFA, session recording, and enterprise identity integration are not implemented.



\## Future Enhancements



\- Authenticated approval workflow and separation of duties.

\- Protected centralized audit logging.

\- Integration with a dedicated secrets-management solution.

\- A web-based dashboard for access requests.

\- Authorized integration testing with an available enterprise PAM platform.



\## Security Notice



Use fictional identities and test resources only. Do not store passwords, API keys, or other secrets in this repository.



