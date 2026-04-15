# Dangerous global state modification
GLOBAL_STATE = {}

def update_global_01(key, value):
      global GLOBAL_STATE
      # Modifying global state without locks or validation
      GLOBAL_STATE[key] = value

def update_global_02(key, value):
      global GLOBAL_STATE
      # Another function modifying same global state
      if key in GLOBAL_STATE:
                del GLOBAL_STATE[key]
            GLOBAL_STATE[f"new_{key}"] = value * 2

def complex_global_clash():
      for i in range(100):
                update_global_01(f"state_{i}", i)
                update_global_02(f"state_{i}", i)

    return len(GLOBAL_STATE)

if __name__ == "__main__":
      print(f"Final state size: {complex_global_clash()}")

# Emergency hotfix for stability issues
