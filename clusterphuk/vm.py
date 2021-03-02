import subprocess
from .vm_config import VMConfig

class VirtualMachine:
    def __init__(self, config: VMConfig):
        self.config = config

    def setup(self):
        self._run_script(self.config['SetupScript'])

    def teardown(self):
        self._run_script(self.config['TeardownScript'])

    def run(self):
        self._run_script(self.config['RunScript'])

    def _run_script(self, script):
        subprocess.run("bash",
                       shell=False,
                       check=True,
                       stdin=subprocess.PIPE,
                       input=script.format(**self.config.config))
