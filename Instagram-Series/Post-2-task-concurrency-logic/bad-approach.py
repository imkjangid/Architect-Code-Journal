import time

def fetch_user(uid):
    time.sleep(1) # Simulate 1s network delay
    return {"id": uid, "name": f"User_{uid}"}

def fetch_stats(uid):
    time.sleep(1) # Simulate 1s network delay
    return {"id": uid, "login_count": uid * 10}

def process_data_slow(user_ids):
    results = []
    # BAD: This loop is blocked by every single API call
    for user_id in user_ids:
        user = fetch_user(user_id)   # Waiting...
        stats = fetch_stats(user_id) # Waiting...
        results.append((user, stats))
    return results

if __name__ == "__main__":
    uids = [101, 102, 103]
    start = time.perf_counter()
    
    process_data_slow(uids)
    
    end = time.perf_counter()
    print(f"Total Time: {end - start:.2f} seconds") # Output: ~6.00 seconds