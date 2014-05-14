def ampm_switch(ampm):
	if ampm == "AM":
		ampm = "PM"
	if ampm == "PM":
		ampm = "AM"
	return ampm
	

print ampm_switch("AM")
