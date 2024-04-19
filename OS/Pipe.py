import multiprocessing

def producer(pipe_conn):
    # Send messages through the pipe
    messages = ['Hello', 'from', 'the', 'producer']
    for message in messages:
        pipe_conn.send(message)
        print(f"Producer sent: {message}")
    pipe_conn.close()

def consumer(pipe_conn):
    # Receive messages from the pipe
    while True:
        try:
            message = pipe_conn.recv()
            print(f"Consumer received: {message}")
        except EOFError:
            print("Consumer received EOF")
            break

if __name__ == "__main__":
    # Create a Pipe object
    parent_conn, child_conn = multiprocessing.Pipe()

    # Create producer and consumer processes
    producer_process = multiprocessing.Process(target=producer, args=(parent_conn,))
    consumer_process = multiprocessing.Process(target=consumer, args=(child_conn,))

    # Start the processes
    producer_process.start()
    consumer_process.start()

    # Wait for processes to finish
    producer_process.join()
    consumer_process.join()
