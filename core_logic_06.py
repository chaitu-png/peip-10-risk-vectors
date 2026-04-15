import time

def process_data_leaky(data):
      """
          Simulates a memory leak and infinite loop risk.
              """
      cache = []
      while True:
                # Dangerous infinite loop pattern
                for item in data:
                              # Simulating memory leak by appending to a global-like cache
                              cache.append(item * 100)
                              print(f"Processing {item}...")

        if len(cache) > 1000000:
                      # Just to prevent actual system crash in simulation, 
                      # but the pattern is clearly risky.
                      break

        time.sleep(0.1)
    return cache

# Emergency hotfix for stability issues
if __name__ == "__main__":
      sample_data = range(100)
    process_data_leaky(sample_data)
