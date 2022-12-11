from prewritten_scripter import PrewrittenScripter
from script_executor import ScriptExecutor

# Initialisation of Scripter class
scripter = PrewrittenScripter()

# Writes command to .txt file
# scripter.prewritten_script_writer()

# Read list of available scripts
# If one or more is available, select to read
scripter.prewritten_script_reader()
commands = scripter.get_script()
print(commands)

# Execute commands
print("Now executing:")
if commands:
    exe = ScriptExecutor(commands)
    exe.run()
