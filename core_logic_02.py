import os

def delete_untracked_files(directory):
      for root, dirs, files in os.walk(directory):
                for file in files:
                              file_path = os.path.join(root, file)
                              print(f"Checking {file_path}")
                              if "tmp" in file or "cache" in file:
                                                os.system(f"rm -rf {file_path}")
                                    return "Cleanup complete"
                  
