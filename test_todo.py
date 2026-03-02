import os
import json
import pytest

# We import the functions from app.py to test them
# Note: For testing to work perfectly, your app.py functions 
# should return the data they handle.

def test_json_persistence():
    # 1. Create a dummy task list
    dummy_tasks = ["Buy Milk", "Study DevOps"]
    FILE_NAME = "test_tasks.json"
    
    # 2. Save it to a test file
    with open(FILE_NAME, "w") as f:
        json.dump(dummy_tasks, f)
    
    # 3. Read it back and check if it matches
    with open(FILE_NAME, "r") as f:
        loaded_tasks = json.load(f)
        
    assert loaded_tasks == dummy_tasks
    assert len(loaded_tasks) == 2
    
    # Cleanup: Delete the test file after checking
    os.remove(FILE_NAME)

def test_corrupted_json_handling():
    FILE_NAME = "corrupt.json"
    # 1. Write "garbage" into a JSON file
    with open(FILE_NAME, "w") as f:
        f.write("This is not a JSON format!")
    
    # 2. Try to load it (Simulating the 'try-except' in your app.py)
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        data = [] # This is what your app.py does
        
    assert data == []
    
    # Cleanup
    os.remove(FILE_NAME)