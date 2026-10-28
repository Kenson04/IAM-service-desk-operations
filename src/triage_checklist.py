#!/usr/bin/env python3
"""Interactive IAM ticket triage checklist; no system changes are performed."""

def choose(prompt, options):
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        answer = input("Select a number: ").strip()
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1]
        print("Invalid selection. Try again.")

def main():
    print("IAM Service Desk Triage Checklist")
    print("This tool is advisory only. Follow your organization's policies.\n")
    verified = choose("Has the caller passed the approved verification process?",
                      ["Yes", "No", "Uncertain"])
    if verified != "Yes":
        print("\nSTOP: Do not change credentials, MFA, or access. Follow escalation policy.")
        return
    issue = choose("Which finding best matches the evidence?",
                   ["Account inactive / leaver", "Active account; password failure",
                    "Lost MFA authenticator", "IdP login succeeds; application denies access",
                    "Unknown / conflicting evidence"])
    actions = {
        "Account inactive / leaver": (
            "Do not reactivate or reset as a workaround. Confirm directory state and "
            "escalate to HR and the account owner/manager for an authorized decision."
        ),
        "Active account; password failure": (
            "Use the approved recovery flow so the user sets their own secret. "
            "If unavailable, follow the approved reset procedure and verify the outcome."
        ),
        "Lost MFA authenticator": (
            "Remove only the stale authenticator, force re-enrollment, and verify MFA "
            "is still enforced. Any exception must be approved, time-bound, and tracked."
        ),
        "IdP login succeeds; application denies access": (
            "Treat as authorization. Verify approval, effective group/role membership, "
            "application bindings, and the authoritative source of membership."
        ),
        "Unknown / conflicting evidence": (
            "Do not guess. Gather directory and application evidence and escalate "
            "according to the runbook."
        )
    }
    print("\nSuggested next step:\n- " + actions[issue])
    print("\nBefore closure: validate the result, review audit evidence, and document the decision.")

if __name__ == "__main__":
    main()
