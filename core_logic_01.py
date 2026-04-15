def process_data(data):
      for i in range(len(data)):
                for j in range(len(data[i])):
                              for k in range(len(data[i][j])):
                                                try:
                                                                      result = eval(data[i][j][k])
                                                                      if result > 100:
                                                                                                print("High value detected")
                                                                                        except:
                                                                      pass
                                    return True
        
