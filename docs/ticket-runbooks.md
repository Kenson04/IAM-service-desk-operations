# Ticket Runbooks

These runbooks summarize the four tickets in the source lab. Follow your organization's policies and approved procedures in a real environment.

## Before every ticket: verify the caller

- Use the organization's approved identity-verification procedure.
- Do not treat urgency, a manager's name, or possession of basic employee details as sufficient proof.
- Record the verification method/result in the ticket without storing sensitive verification answers.
- If verification fails, stop and follow the escalation procedure.

## Ticket 1 — Password forgotten

**Goal:** restore access without learning or sharing the user's long-term password.

1. Review recent events and confirm the failure pattern.
2. In the directory, verify the account is active and not otherwise restricted.
3. Prefer a self-service recovery flow so the user sets a secret the analyst never knows.
4. If the lab has no recovery flow, use its supported password action; require a change at next login where available and transfer any temporary credential only through an approved secure channel.
5. Test sign-in as the user only in the lab/test environment; in production, have the user validate their own access.
6. Confirm the successful event and record the result.

**Do not:** put passwords in ticket comments, chat, screenshots, shell history, or source control.

## Ticket 2 — “Locked out” but account is inactive

**Goal:** distinguish temporary lockout from deliberate deactivation.

1. Review the event log, but do not assume it fully explains the cause.
2. Open the user record and inspect its active/inactive state.
3. If the account is inactive because of a termination or approved lifecycle event, do not reset credentials or reactivate it as a service-desk workaround.
4. Escalate to HR and the account owner/manager for a verified business decision.
5. Preserve the audit trail and record the escalation.
6. In the training lab only, restore the account afterward if required to continue later exercises; never copy that step into production practice without authorization.

**Key lesson from the source guide:** its deactivated-account attempt can appear indistinguishable from an ordinary wrong-password attempt in the event log. The directory's active flag is the decisive state check.

## Ticket 3 — Lost MFA device

**Goal:** replace the unavailable authenticator without permanently weakening MFA.

1. Verify the caller using the approved procedure.
2. Confirm the user's identity and current MFA policy scope.
3. Identify the authenticator the user can no longer access.
4. Remove only the stale authenticator using the supported admin workflow.
5. Require the user to enroll a new authenticator.
6. Validate a fresh sign-in and confirm that the new factor is challenged.
7. If an emergency bypass is explicitly permitted, obtain required approval, document the reason, set a short expiry, and track removal.

**Do not:** share enrollment QR codes, seeds, or recovery codes in tickets or screenshots; do not leave a permanent MFA exemption.

## Ticket 4 — Cannot access WordPress

**Goal:** identify authorization failure when authentication succeeded.

1. Confirm the user successfully authenticates to Authentik.
2. Check the application's group/role bindings and the user's effective group membership.
3. Confirm with the manager/application owner whether access is approved.
4. If membership is driven from HR data, change the authoritative attribute in OrangeHRM rather than manually editing a derived group.
5. Run the approved mover/synchronization job.
6. Validate the user's effective membership and application access.
7. Keep unapproved groups unbound; do not widen the application rule to close one ticket.
8. Account for dashboard/tile caching when validating the UI, as described in the source lab.

## Closure criteria

- Caller verification completed.
- Root cause and evidence recorded.
- Approval captured where required.
- Change applied at the correct layer.
- User/application result validated.
- Audit event reviewed.
- Escalation or follow-up owner assigned if unresolved.
