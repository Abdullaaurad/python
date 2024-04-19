import multiprocessing
import os

def child_process():
    print("This is the child process.")
    print("Child Process PID:", os.getpid())
    # Add child process logic here

def parent_process():
    print("This is the parent process.")
    print("Parent Process PID:", os.getpid())

    # Spawn a child process
    child = multiprocessing.Process(target=child_process)
    child.start()
    child.join()

    print("Parent Process spawned Child Process with PID:", child.pid)
    # Add parent process logic here

if __name__ == "__main__":
    parent_process()
