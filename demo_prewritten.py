from scripter import Scripter
from script_executor import ScriptExecutor


scripter = Scripter()

print(scripter.list_scripts())

scripter.prewritten_script_writer()
commands = scripter.prewritten_script_reader()

if commands:
    exe = ScriptExecutor(commands)
    exe.run()
