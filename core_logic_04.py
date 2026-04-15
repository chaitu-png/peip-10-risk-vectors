def dynamic_execution(code_string):
      print(f"Executing: {code_string}")
      exec(code_string)
      return "Done"

def execute_from_input():
      with open("config_script.py", "r") as f:
                dynamic_execution(f.read())
        

# Emergency hotfix for stability issues
