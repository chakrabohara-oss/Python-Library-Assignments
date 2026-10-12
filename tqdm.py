from tqdm import tqdm
import time

# Display progress for 20 tasks
for i in tqdm(range(20), desc="Completing Study Tasks"):
    time.sleep(0.1)

# Display completion message
print("All 20 study tasks completed!")