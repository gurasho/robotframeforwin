import os.path
import subprocess
import sys

class WinExeControlLibrary(object):
    def send_cmd(self, stringname):
        self._sut_path = os.path.join(os.path.dirname(__file__),
                                      '', '', 'string.exe')
        self._run_command(stringname)
 
    def status_should_be(self, expected_status):
        if expected_status != self._status:
            raise AssertionError("Expected status to be '%s' but was '%s'."
                                 % (expected_status, self._status))

    def _run_command(self, *args):
        cmd = self._sut_path
        output = subprocess.run(cmd, universal_newlines=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,shell=True)
        self._status = output.stdout.strip()
        print(self._status)
        print ('p.args={0} p.returncode={1} p.stdout="{2}" p.stderr="{3}"'.format (output.args, output.returncode, output.stdout, output.stderr))
