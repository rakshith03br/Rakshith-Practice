"""
Threading in Python:
    https://docs.python.org/3/library/threading.html
    Threading lets you run multiple pieces of code seemingly "at the same time" within a single process.
    In Python, it's a bit unusual because of the GIL (Global Interpreter Lock) — understanding that
    is key to using threads well.
"""
import threading
print(threading.__file__)
import time

def worker(name):
    print(f"{name} starting")
    time.sleep(2)
    print(f"{name} done")

t1 = threading.Thread(target=worker, args=("T-1",))
t2 = threading.Thread(target=worker, args=("T-2",))

t1.start()
t2.start()

t1.join()  # wait for t1 to finish
t2.join()  # wait for t2 to finish

print("All done")


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================

# -------------------------
# 1. The GIL (Global Interpreter Lock) - THE most important threading concept
#    to understand in Python, and almost guaranteed to come up in interviews
# -------------------------
"""
The GIL is a mutex that allows only ONE thread to execute Python BYTECODE at
a time, even on a multi-core machine. This means:

  - CPU-BOUND tasks (pure computation, e.g. crunching numbers in a loop) do
    NOT get faster with threading in CPython - the GIL means only one thread
    runs Python code at any given moment, so multiple threads doing heavy
    computation can actually be SLOWER than single-threaded (due to
    context-switching overhead) or at best no faster.

  - I/O-BOUND tasks (waiting on network calls, file reads, sleep, database
    queries) DO benefit from threading - because the GIL is RELEASED while a
    thread is waiting on I/O, letting OTHER threads run Python code during
    that wait. This is EXACTLY why your worker() function using time.sleep()
    shows real concurrency - sleep() releases the GIL.

RULE OF THUMB asked in almost every Python threading interview:
    I/O-bound work  -> use threading (or asyncio)
    CPU-bound work    -> use multiprocessing (separate processes, separate
                           GILs, TRUE parallelism across cores)
"""

print(f"{'*' * 70}")

# -------------------------
# 2. Proving the GIL's effect: CPU-bound work does NOT speed up with threads
# -------------------------
def cpu_bound_work(n):
    count = 0
    for i in range(n):
        count += i * i
    return count

# Single-threaded timing
start = time.perf_counter()
cpu_bound_work(5_000_000)
cpu_bound_work(5_000_000)
print(f"Sequential (single-threaded): {time.perf_counter() - start:.3f}s")

# "Multi-threaded" timing - usually similar or WORSE due to GIL + thread overhead
start = time.perf_counter()
t_a = threading.Thread(target=cpu_bound_work, args=(5_000_000,))
t_b = threading.Thread(target=cpu_bound_work, args=(5_000_000,))
t_a.start(); t_b.start()
t_a.join(); t_b.join()
print(f"Threaded (still limited by GIL): {time.perf_counter() - start:.3f}s")
# For CPU-bound work, these two timings are typically close to EACH OTHER
# (no speedup) - this is the single clearest demonstration of the GIL's effect.

print(f"{'*' * 70}")

# -------------------------
# 3. Race conditions - what happens WITHOUT proper synchronization
# -------------------------
counter = 0

def increment_unsafe():
    global counter
    for _ in range(100_000):
        counter += 1   # NOT atomic! this is actually: read counter, add 1, write back -
                          # multiple threads can interleave these 3 steps and LOSE updates

threads = [threading.Thread(target=increment_unsafe) for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"Expected 500000, got: {counter}")   # often LESS than 500000 due to race condition!
# NOTE: due to the GIL, simple += on an int is "less risky" in CPython than in
# languages without a GIL, but it's STILL not guaranteed atomic across
# multiple bytecode instructions - races can and do happen.

print(f"{'*' * 70}")

# -------------------------
# 4. threading.Lock - the fix for race conditions (mutual exclusion)
# -------------------------
counter2 = 0
lock = threading.Lock()

def increment_safe():
    global counter2
    for _ in range(100_000):
        with lock:            # only ONE thread can hold the lock at a time
            counter2 += 1        # this section is now a "critical section" - safe from races

threads2 = [threading.Thread(target=increment_safe) for _ in range(5)]
for t in threads2:
    t.start()
for t in threads2:
    t.join()
print(f"Expected 500000, got: {counter2}")   # ALWAYS exactly 500000 now - race eliminated

print(f"{'*' * 70}")

# -------------------------
# 5. Deadlocks - what happens when locks are acquired in inconsistent order
# -------------------------
"""
lock_a = threading.Lock()
lock_b = threading.Lock()

def thread1_work():
    with lock_a:
        time.sleep(0.1)
        with lock_b:      # thread1 waits for lock_b while HOLDING lock_a
            pass

def thread2_work():
    with lock_b:
        time.sleep(0.1)
        with lock_a:      # thread2 waits for lock_a while HOLDING lock_b
            pass          # DEADLOCK! each thread holds what the other needs -> both wait forever

# FIX: always acquire multiple locks in the SAME, CONSISTENT order across
# all threads (e.g., always lock_a before lock_b, everywhere in the codebase).
"""

print(f"{'*' * 70}")

# -------------------------
# 6. RLock (reentrant lock) - allows the SAME thread to acquire it multiple times
# -------------------------
rlock = threading.RLock()

def recursive_function(n):
    with rlock:                  # a plain Lock would DEADLOCK here on the 2nd call from
                                    # the SAME thread - RLock tracks WHICH thread holds it
                                    # and how many times, allowing safe re-entry
        if n > 0:
            print(f"Depth {n}")
            recursive_function(n - 1)

recursive_function(3)   # works fine with RLock; would deadlock with a plain Lock

print(f"{'*' * 70}")

# -------------------------
# 7. queue.Queue - the RECOMMENDED thread-safe way to pass data between
#    threads (avoids needing manual locks for simple producer/consumer patterns)
# -------------------------
import queue

q = queue.Queue()

def producer():
    for i in range(5):
        q.put(i)              # thread-safe put
        print(f"Produced: {i}")

def consumer():
    while True:
        item = q.get()          # thread-safe get, BLOCKS until an item is available
        if item is None:           # sentinel value to signal "stop"
            break
        print(f"Consumed: {item}")
        q.task_done()

prod_thread = threading.Thread(target=producer)
cons_thread = threading.Thread(target=consumer)
prod_thread.start()
cons_thread.start()
prod_thread.join()
q.put(None)          # send the sentinel so the consumer knows to stop
cons_thread.join()

print(f"{'*' * 70}")

# -------------------------
# 8. Daemon threads - background threads that DON'T block program exit
# -------------------------
def background_task():
    while True:
        time.sleep(1)   # runs forever

daemon_thread = threading.Thread(target=background_task, daemon=True)
daemon_thread.start()
# When daemon=True, this thread will be KILLED automatically when the main
# program exits - it does NOT need to be joined, and won't keep the process
# alive. Non-daemon threads (the default) WILL keep the program running
# until they finish, even if main() has otherwise completed.
print("Daemon thread started (will be killed automatically at program exit)")

print(f"{'*' * 70}")

# -------------------------
# 9. concurrent.futures.ThreadPoolExecutor - the MODERN, higher-level way to
#    manage threads (avoids manually creating/joining Thread objects)
# -------------------------
from concurrent.futures import ThreadPoolExecutor

def fetch_simulated(item):
    time.sleep(0.1)   # simulates an I/O wait, e.g. an HTTP request
    return f"Result for {item}"

with ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(fetch_simulated, ["a", "b", "c", "d", "e"]))
print(results)
# ThreadPoolExecutor manages a POOL of reusable worker threads, handles
# joining automatically (via the 'with' block), and .map()/.submit() give
# you clean ways to run many tasks concurrently and collect results -
# much less boilerplate than manually managing Thread objects.

# .submit() form - gives you Future objects for more control (e.g., checking
# exceptions, adding callbacks):
with ThreadPoolExecutor(max_workers=2) as executor:
    future = executor.submit(fetch_simulated, "special item")
    print(future.result())   # blocks until this specific task completes, returns its result

print(f"{'*' * 70}")

# -------------------------
# 10. threading.Event - simple signaling between threads (no shared data needed)
# -------------------------
event = threading.Event()

def waiter():
    print("Waiter: waiting for event...")
    event.wait()              # BLOCKS here until event.set() is called by another thread
    print("Waiter: event received, proceeding!")

def setter():
    time.sleep(1)
    print("Setter: setting the event now")
    event.set()                 # wakes up ALL threads waiting on this event

wt = threading.Thread(target=waiter)
st = threading.Thread(target=setter)
wt.start(); st.start()
wt.join(); st.join()

print(f"{'*' * 70}")

# -------------------------
# 11. threading.Semaphore - limiting how many threads can access a resource
#     CONCURRENTLY (e.g., limiting simultaneous connections to a service)
# -------------------------
semaphore = threading.Semaphore(2)   # only 2 threads allowed "inside" at once

def limited_access(name):
    with semaphore:
        print(f"{name} acquired the semaphore")
        time.sleep(0.5)
        print(f"{name} releasing the semaphore")

sem_threads = [threading.Thread(target=limited_access, args=(f"Thread-{i}",)) for i in range(4)]
for t in sem_threads:
    t.start()
for t in sem_threads:
    t.join()
# Only 2 threads run "inside" the semaphore block at any given moment - the
# other 2 wait their turn, even though all 4 threads started immediately.

print(f"{'*' * 70}")

# -------------------------
# 12. threading vs multiprocessing vs asyncio - the classic "which concurrency
#     tool" interview decision tree
# -------------------------
"""
threading         -> best for I/O-BOUND tasks (network calls, file I/O, DB
                      queries) where threads spend most of their time WAITING,
                      not computing. Limited by the GIL for CPU-bound work.

multiprocessing   -> best for CPU-BOUND tasks (heavy computation, data
                      processing, image processing) - each process gets its
                      OWN Python interpreter and GIL, so TRUE parallel
                      execution across multiple CPU cores is possible.
                      Higher memory overhead (separate process memory space),
                      and data must be SERIALIZED (pickled) to pass between
                      processes.

asyncio           -> best for a VERY LARGE number of concurrent I/O-bound
                      tasks (e.g., thousands of simultaneous network
                      connections) within a SINGLE thread, using cooperative
                      multitasking (async/await) instead of OS-level threads -
                      much lower overhead per "task" than a real thread.
"""


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON THREADING
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the GIL (Global Interpreter Lock), and what specific limitation
#    does it place on multi-threaded Python programs?
#
# 2. Why does threading provide a real speedup for I/O-bound tasks but NOT
#    for CPU-bound tasks in CPython? What is happening to the GIL during an
#    I/O wait (like time.sleep() or a network call)?
#
# 3. If threading doesn't help with CPU-bound work due to the GIL, what
#    module WOULD you use to achieve true parallelism across multiple CPU
#    cores?
#
# 4. What is a race condition? Walk through a concrete example (like
#    `counter += 1` across multiple threads) of how it can produce an
#    incorrect final result.
#
# 5. What does `threading.Lock` do, and how does using a lock (e.g., via a
#    `with lock:` block) prevent the race condition from question 4?
#
# 6. What is a deadlock? Describe a scenario with two locks and two threads
#    where a deadlock could occur, and how you would prevent it.
#
# 7. What is the difference between `threading.Lock` and `threading.RLock`?
#    In what scenario would using a plain Lock cause a deadlock where an
#    RLock would not?
#
# 8. What is a daemon thread, and how does setting `daemon=True` change how
#    the program behaves when the main thread finishes?
#
# 9. Why is `queue.Queue` recommended for passing data between threads,
#    instead of using a plain list or dict with manual locking?
#
# 10. What is `concurrent.futures.ThreadPoolExecutor`, and what advantages
#     does it offer over manually creating and joining individual `Thread`
#     objects?
#
# 11. What is the difference between `executor.map()` and `executor.submit()`
#     when using ThreadPoolExecutor? When would you use one over the other?
#
# 12. What does `threading.Event` provide, and how is it different from using
#     a `Lock` for coordinating between threads?
#
# 13. What is a `threading.Semaphore` used for? Give a real-world example of
#     limiting concurrent access to a shared resource (e.g., a connection
#     pool).
#
# 14. What is the difference between `thread.join()` and simply letting a
#     thread run without joining it? What could go wrong if you forget to
#     call `join()` before your program exits?
#
# 15. Why might starting many threads for a CPU-bound task actually make your
#     program SLOWER than running it single-threaded?
#
# 16. What is the difference between threading, multiprocessing, and asyncio?
#     For each, describe the type of workload it's best suited for.
#
# 17. If two threads both read and then write to the SAME shared variable
#     without any lock, is it guaranteed that the operation will produce a
#     wrong result every single time, or is it non-deterministic? Why?
#
# 18. What happens to data shared between threads when you switch to
#     multiprocessing instead? Why can't you simply share a Python object
#     (like a list) directly between separate processes the way you can
#     between threads?
#
# 19. Is Python's GIL removed or optional in any recent CPython version or
#     alternative implementation? (Hint: consider what you know about ongoing
#     CPython development efforts around the GIL.)
#
# 20. How would you safely share a counter or piece of state across multiple
#     threads without manually managing a Lock yourself? (Hint: think about
#     higher-level thread-safe primitives the standard library provides.)
