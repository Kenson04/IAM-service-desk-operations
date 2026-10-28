# IAM Service Desk Operations Lab

A portfolio-ready Identity and Access Management (IAM) operations repository based on the supplied **All Things Identity — Hands-on IAM Labs, Lab 6: Identity Service Desk Operations** guide.

This project demonstrates event-driven ticket triage, caller verification, lifecycle guardrails, MFA recovery, and troubleshooting the difference between authentication and application authorization. The lab environment references Authentik, OrangeHRM, and WordPress SSO.

> **Safety:** Use synthetic test identities only. Never publish passwords, tokens, MFA seeds, recovery codes, personal data, or production configuration. No real system screenshots were supplied; the screenshot folder contains capture instructions, not fabricated evidence.

## Four ticket scenarios

| Ticket | Finding | Recommended handling |
|---|---|---|
| Password forgotten | Active account with password failures | Prefer self-service recovery; validate successful sign-in and audit evidence. |
| “Locked out” | Account intentionally inactive after a lifecycle event | Do not reactivate as a workaround; escalate to HR and the account owner. |
| Lost MFA device | Registered authenticator is unavailable | Remove the stale authenticator, require re-enrollment, and verify MFA remains enforced. |
| WordPress access denied | IdP authentication succeeds, app authorization fails | Check approval and effective group/role membership; correct the HR source attribute and run the approved mover process. Do not widen app bindings. |

The source guide notes that a failed login event alone may not distinguish a wrong password from an attempt against a deactivated account. Confirm lifecycle state in the directory.

## Repository layout

- `docs/ticket-runbooks.md` — step-by-step handling for all four tickets
- `docs/triage-decision-tree.md` — triage flow and guardrails
- `docs/security-controls.md` — controls and portfolio recommendations
- `docs/evidence-and-screenshots.md` — evidence handling and screenshot checklist
- `docs/source-notes.md` — source scope and attribution
- `screenshots/` — screenshot capture plan; no fabricated evidence
- `src/triage_checklist.py` — interactive decision-support checklist
- `tests/test_triage_checklist.py` — unit tests
- `templates/` — ticket and escalation handoff templates

## Quick start

Requires Python 3.9+; no third-party packages are needed.

```bash
python src/triage_checklist.py
python -m unittest discover -s tests -v
```

The helper is advisory only. It does not connect to IAM systems or make changes.

## Operational workflow

1. Verify the caller through the approved process.
2. Review identity-provider events and capture relevant timestamps/context.
3. Check directory account state independently of the event log.
4. Classify the issue as authentication, lifecycle, MFA, or authorization.
5. Confirm required approval before changes.
6. Fix the issue at the correct source of truth using least privilege.
7. Validate the outcome and review audit evidence.
8. Document the decision and close or escalate the ticket.

## Portfolio screenshots

Follow [the screenshot plan](screenshots/screenshot-plan.md). Capture evidence in your own test lab with synthetic users, redact sensitive details, and describe only what the screenshot actually demonstrates.

## Source and scope

This independent learning/portfolio adaptation is based on the uploaded *All Things Identity — Hands-on IAM Labs, Lab 6: Identity Service Desk Operations* guide. Some ticket controls and templates are portfolio-oriented recommendations rather than claims that the source lab already implements them. See [source notes](docs/source-notes.md).

## Suggested repository description

IAM service desk operations lab covering identity verification, event-log triage, password recovery, leaver-account escalation, MFA re-enrollment, and authentication-vs-authorization troubleshooting with Authentik, OrangeHRM, and WordPress SSO.

Suggested topics: `iam` `identity-access-management` `authentik` `sso` `mfa` `identity-governance` `service-desk` `access-management` `security-operations`
