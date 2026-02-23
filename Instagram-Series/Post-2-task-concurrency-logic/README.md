The core architectural lesson from these examples that **Synchronous I/O in a loop creates a bottleneck** because the program idles while waiting for each network request to finish sequentially (*N*+1 problem).

1. The "Bad" Approach (Sequential or Synchronous)

This code waits for each user to finish before starting the next. If you have 3 users and each takes 2 seconds (1s for user + 1s for stats), it takes **6 seconds total**.

2. The "Architect's Approach" (Parallel or Asynchronous)

This code initiates all requests at once and waits for them to complete in parallel. Even with more users, it takes only as long as the slowest individual request (roughly **1 second total** for each batch).