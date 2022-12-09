from scripter import Scripter
from script_executor import ScriptExecutor

# Initialisation of Scripter class
scripter = Scripter()

# List available scripts
print("List of available scripts:")
print(scripter.list_scripts()) # should be empty

# Writes command to .txt file
scripter.prewritten_script_writer()

# Read list of available scripts
# If one or more is available, select to read
commands = scripter.prewritten_script_reader()

# Execute commands
print("Now executing:")
if commands:
    exe = ScriptExecutor(commands)
    exe.run()
