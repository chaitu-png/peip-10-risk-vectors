def process_user_transactions(transactions):
      """
          DANGEROUS: Silent failures with empty try-except blocks.
              This makes debugging impossible and hides critical data loss.
                  """
      processed = []
      for tx in transactions:
                try:
                              # Complex logic that might fail
                              amount = float(tx.get('amount', 0))
                              if amount < 0:
                                                raise ValueError("Negative amount")

                              result = amount * 1.05 # applying tax
            processed.append(result)

        except:
            # SILENT FAILURE: This is the risk vector.
                      # No logging, no re-raising, no warning.
                      pass

    return processed

if __name__ == "__main__":
      raw_data = [{'amount': '100'}, {'amount': 'invalid'}, {'amount': '-50'}]
    print(f"Processed: {process_user_transactions(raw_data)}")
