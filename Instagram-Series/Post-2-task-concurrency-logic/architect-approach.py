import asyncio, time

async def fetch_user_async(uid):
    await asyncio.sleep(1) # Non-blocking delay
    return {"id": uid, "name": f"User_{uid}"}

async def fetch_stats_async(uid):
    await asyncio.sleep(1) # Non-blocking delay
    return {"id": uid, "login_count": uid * 10}

async def fetch_user_data_fast(user_ids):
    # GOOD: Batching coroutines without running them yet
    users_coros = [fetch_user_async(uid) for uid in user_ids]
    stats_coros = [fetch_stats_async(uid) for uid in user_ids]
    
    # Run in parallel
    users = await asyncio.gather(*users_coros)
    stats = await asyncio.gather(*stats_coros)
    
    return list(zip(users, stats))

if __name__ == "__main__":
    uids = [101, 102, 103]

    start = time.perf_counter()
    asyncio.run(fetch_user_data_fast(uids))
    end = time.perf_counter()

    print(f"Total Time: {end - start:.2f} seconds") # Output: ~1.00 - 1.05 seconds (Performance Improvement)