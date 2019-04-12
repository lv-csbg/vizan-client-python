from subprocess import Popen, PIPE
from os import path, getcwd, chdir, getpgid, waitpid
from sys import platform
import logging
import time
HERE = path.abspath(path.dirname(__file__))
module_logger = logging.getLogger('vizan_client.docker_server')


class LocalServer(object):
    def __init__(self, stdin=PIPE, stdout=PIPE, stderr=PIPE):
        self.logger = logging.getLogger('vizan_client.docker_server.LocalServer')
        self.cwd = getcwd()
        self.logger.info("CWD {}".format(self.cwd))
        self.path = HERE
        self.logger.info("HERE {}".format(self.path))
        chdir(self.path)
        std_kwargs = dict(stdin=stdin, stdout=stdout, stderr=stderr)

        cmd = ['docker-compose', 'up', '--force-recreate']
        if platform == "linux" or platform == "linux2":
            is_user = is_user_in_docker_group()
            if not is_user:
                self.logger.warning("WARNING: The user is not in the 'docker' group. "
                                    "Most likely it does not have rights to run docker")
        self.process = Popen(cmd, shell=False, **std_kwargs)
        time.sleep(20)
        chdir(self.cwd)

    def __del__(self):
        self.logger.info("Process pid {}".format(self.process.pid))
        pgid = getpgid(self.process.pid)
        self.logger.info("Process pgid {}".format(pgid))
        # # You might want to wait for the process to end:
        self.process.terminate()
        self.logger.info("SIGTERM has been sent.")
        waitpid(self.process.pid, 0)
        self.logger.info("Waitpid has finished.")


def is_user_in_docker_group():
    cmd = "groups $USER"
    process = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    stdout = process.stdout.peek()
    process.terminate()
    if b'docker' in stdout:
        return True
    else:
        return False
