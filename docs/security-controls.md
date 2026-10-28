# Security Controls and IAM Analyst Notes

## Controls demonstrated by the lab

- Event-log review before account changes.
- Caller verification before sensitive service-desk actions.
- Recovery flow preferred over admin-known passwords.
- Account lifecycle state checked independently of authentication logs.
- Leaver access remains disabled pending an authorized decision.
- Lost MFA authenticators are replaced with re-enrollment, not indefinite MFA removal.
- Authentication and authorization failures are diagnosed separately.
- HR is treated as the source of truth for department-derived group membership.
- Application bindings are not widened to make a single ticket disappear.

## Portfolio recommendations (extensions beyond the lab steps)

1. Require ticket ID and approval evidence for reactivation and privileged access changes.
2. Alert on activation of a previously deactivated account.
3. Use role-based service-desk permissions and separate approval from execution for high-risk changes.
4. Keep audit logs tamper-resistant and retain them according to policy.
5. Set time-bound exceptions with owner, reason, expiry, and automatic follow-up.
6. Track operational metrics: time to triage, reopen rate, MFA re-enrollment completion, and unauthorized-change attempts.
7. Test lifecycle jobs idempotently and review drift between HR and the identity directory.

## Evidence hygiene

- Use synthetic users and non-production tenants.
- Redact email addresses, usernames, IPs, tenant URLs, tokens, QR seeds, recovery codes, and browser profile details.
- Never commit secrets, `.env` files, exports, or unredacted audit logs.
- Prefer annotated, cropped screenshots that show only the relevant UI state.
