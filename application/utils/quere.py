try:
    from Queue import Queue
except ImportError:
    from queue import Queue
    
update_queue = Queue()