import os
import time
pid = os.fork()
if pid == 0:
	print(f"Child: PID={os.getpid()} running...")
	time.sleep(2)
	print("Child: Finished work.")
else:
	print(f"Parent: Waiting for child (PID = {pid})...")
	os.wait() #parent waits
	print("Parent: Child completed. Parent exiting.")
