
import subprocess
import os

def test_basic_makefile():
    # Run the Makefile
    subprocess.run(["make"], check=True)

    # Check if the executable 'program' is created
    assert os.path.isfile("program"), "Executable 'program' not created"

# Call the test function
test_basic_makefile()

def test_clean_target():
    # Ensure the executable 'program' exists
    subprocess.run(["make"], check=True)
    assert os.path.isfile("program"), "Executable 'program' not created before clean"

    # Run the clean target
    subprocess.run(["make", "clean"], check=True)

    # Check if the executable 'program' is removed
    assert not os.path.isfile("program"), "Executable 'program' not removed by clean"

# Call the test function
test_clean_target()

def test_phony_targets():
    # Create a file named 'clean'
    with open('clean', 'w') as f:
        f.write("")

    # Run the clean target
    subprocess.run(["make", "clean"], check=True)

    # Check if 'clean' file still exists (since it should not be removed)
    assert os.path.isfile("clean"), "File 'clean' was incorrectly removed"

    # Clean up
    os.remove('clean')

# Call the test function
test_phony_targets()
