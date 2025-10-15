import os
print("Before Fork: I am Parent Process")
pid = os.fork()
if pid == 0:
	print(f"I am child process: my pld: {os.getpid()}, My Parent PID: {os.getppid()}")
else:
	print(f"I am the parent process. My pid: {os.getpid()}, My child PID: {pid}")
