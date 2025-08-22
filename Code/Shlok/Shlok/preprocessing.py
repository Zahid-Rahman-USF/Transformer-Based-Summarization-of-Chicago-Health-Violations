def preprocess_violation(record):
    # Adjust based on the Chicago API fields
    violation_description = record.get("violation_description", "")
    facility_name = record.get("dba_name", "Unknown Restaurant")
    inspection_date = record.get("inspection_date", "Unknown Date")

    text = f"Violation at {facility_name} on {inspection_date}: {violation_description}"
    return text