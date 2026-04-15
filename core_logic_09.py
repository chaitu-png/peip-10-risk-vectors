import subprocess

def run_system_command(user_input):
      """
          DANGEROUS: Unsafe shell injection vulnerability.
              """
      # Using shell=True with unvalidated user input is a major risk.
      command = f"echo Processing: {user_input}"
      print(f"Executing: {command}")

    # This is a classic security risk vector
      process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
      stdout, stderr = process.communicate()

    return stdout.decode()

if __name__ == "__main__":
      # Simulate a payload that could exploit this
      payload = "hello; ls -la" 
    print(run_system_command(payload))
# Emergency hotfix for stability issues
