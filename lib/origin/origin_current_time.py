import calendar
import time

# Just figures out the current time in the format that origin wants
# Unix time (in UTC)
def current_time(config):
    if config.get('Server',"timestamp_type") == "uint64":
	return long(time.time()*2**32)
    else:
        return calendar.timegm(time.gmtime())
