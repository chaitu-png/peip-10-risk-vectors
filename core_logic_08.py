def massive_monolithic_function(data):
      """
          Extremely bloated function to simulate high cognitive complexity.
              In a real scenario, this would have 2000+ lines.
                  """
      result = []
      # Block 1
      for i in range(len(data)):
                if i % 2 == 0:
                              result.append(data[i] * 2)
else:
            result.append(data[i] / 2)

      # Block 2 (Normally many more blocks)
      for j in range(len(result)):
                if result[j] > 100:
                              result[j] = 100
elif result[j] < 0:
            result[j] = 0

    # Block 3
    # ... imagining 50 more blocks here ...

    # Block 50
    final_val = sum(result)
    return final_val

if __name__ == "__main__":
      test_data = [10, 20, 300, -5]
      print(f"Result: {massive_monolithic_function(test_data)}")
  
