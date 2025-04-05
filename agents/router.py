def route_ticket(root_cause):
    mapping = {
        "payment": "Payment Gateway Team",
        "network": "Network Operations",
        "device": "Device Compatibility",
        "installation": "DevOps",
        "account": "Account Sync Team"
    }
    return mapping.get(root_cause.lower(), "General Support")
