import time
import tracemalloc

class Profiler:

    def start(self):
        tracemalloc.start()
        self.start_time = time.time()

    def stop(self):
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        elapsed = time.time() - self.start_time

        return elapsed, peak / 1024