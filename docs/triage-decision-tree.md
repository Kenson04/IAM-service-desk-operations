# Triage Decision Tree

```text
Ticket received
      |
      v
Verify caller with approved process
      |
      +-- Verification failed/uncertain --> STOP; escalate
      |
      v
Review IdP events and target account state
      |
      +-- Account inactive / leaver? --> Do not reactivate; escalate to HR + owner
      |
      +-- Active account, password failure? --> Approved recovery/reset workflow
      |
      +-- Lost/unavailable MFA device? --> Remove stale device; force re-enrollment
      |
      +-- Authenticates to IdP but app denied? --> Authorization/group/role/source-data check
      |
      v
Apply approved least-privilege fix
      |
      v
Validate outcome + audit evidence + ticket notes
```

## Guardrails

- A user-reported symptom is not a root-cause diagnosis.
- An event log can be incomplete or ambiguous; corroborate with directory state and application configuration.
- Do not restore access to an intentionally deactivated identity without an authorized lifecycle decision.
- Do not broaden an app's access binding to solve one person's access problem.
