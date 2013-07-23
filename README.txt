-----logrotate.exe-----

Arguments: <filename> <numfiles>
	filename - name of log file to rotate
	numfiles - max number of logs to keep

Example call: logrotate.exe sample.log 7

Notes:
- If no arguments, prompts for filename and numfiles
- If log file is open for writing by another program, logrotate will
	wait for permission to write