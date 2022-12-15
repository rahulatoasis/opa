package graphql

default allow = false

privileged_fields := {"guestOS", "appITSI"}

allow {
	input.user == "admin"
	field_allowed
}

field_allowed {
  privileged_fields[input.field]
}