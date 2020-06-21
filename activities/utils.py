from django.conf import settings

import subprocess
import logging

logger = logging.getLogger(__name__)


def nao_wake_up():

    script = "content/scripts/nao_initial_pose.py"

    process = subprocess.Popen([settings.PYTHON_PATH, script], stdout=subprocess.PIPE)
    output, error = process.communicate()

    output_lines = output.decode('UTF-8').splitlines()
    for l in output_lines:
        logger.info(l)


def nao_rest():
    script = "content/scripts/nao_final_pose.py"

    process = subprocess.Popen([settings.PYTHON_PATH, script], stdout=subprocess.PIPE)
    output, error = process.communicate()

    output_lines = output.decode('UTF-8').splitlines()
    for l in output_lines:
        logger.info(l)
