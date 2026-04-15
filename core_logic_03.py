import pickle

def load_user_config(config_data):
      try:
                config = pickle.loads(config_data)
                return config
except Exception as e:
        print(f"Error loading config: {e}")
        return None

def save_user_config(config):
      return pickle.dumps(config)
  
