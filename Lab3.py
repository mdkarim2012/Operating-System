import os
import sys
pid = os.fork()

if pid == 0:
	print("Child: Doing some work........")
	sys.exit(0)
else:
	os.wait()
	print("parent child executed successfully...")
