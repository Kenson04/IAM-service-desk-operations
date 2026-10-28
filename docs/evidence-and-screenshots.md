# Evidence and Screenshot Plan

Use screenshots from your own lab. Do not represent placeholders as actual system evidence.

| ID | Suggested filename | What it should demonstrate | Redaction/check |
|---|---|---|---|
| S01 | `01-authentik-event-log-failed-login.png` | Test user's failed login event and timestamp | Hide unrelated users, IPs if sensitive, tenant identifiers |
| S02 | `02-directory-user-active-state.png` | Active/inactive state in Directory > Users | Synthetic username only |
| S03 | `03-password-recovery-success.png` | Recovery/reset workflow and successful login event | Never show a password or recovery token |
| S04 | `04-mfa-authenticator-enrolled.png` | Authenticator enrollment status | Never show QR seed, OTP, or recovery codes |
| S05 | `05-authentication-success-app-denied.png` | IdP authentication succeeded while app authorization failed | Hide cookies, tokens, unrelated account details |
| S06 | `06-orangehrm-department-source.png` | HR department/sub-unit source attribute | Synthetic employee only |
| S07 | `07-mover-job-success.png` | Approved mover/sync run result | No secrets or production paths |
| S08 | `08-wordpress-access-granted.png` | Final authorized app access | Synthetic account; hide personal data |

## Suggested screenshot layout

- Width: 1200–1600 px where practical.
- Crop to the relevant console region.
- Add a short caption explaining the control and outcome.
- Use arrows or numbered callouts sparingly.
- Use PNG for UI evidence.
- Keep the original private; publish only the sanitized copy.

## Captions you can reuse

- **Event-driven triage:** Reviewed the identity provider's event log before making a change.
- **Lifecycle guardrail:** Confirmed account state independently of a failed-login event.
- **MFA recovery:** Removed the stale authenticator and validated re-enrollment.
- **Authorization troubleshooting:** Distinguished successful authentication from denied application access.
- **Source-of-truth remediation:** Corrected HR-driven membership at the authoritative source rather than editing a derived group manually.

## Capture process

1. Complete the scenario with a synthetic test identity.
2. Capture only the relevant UI state.
3. Copy the screenshot to a separate review folder.
4. Redact sensitive fields using an image editor; do not rely on blur for secrets that can be recovered.
5. Inspect at full size, including metadata and browser chrome.
6. Save the sanitized file under the suggested filename.
7. Add it to the README with a factual caption.
8. Review the staged Git diff before pushing.
