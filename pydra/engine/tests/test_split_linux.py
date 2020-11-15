import os, shutil
import subprocess as sp
import pytest
import attr

from ..task import SingularityTask
from ..submitter import Submitter


need_singularity = pytest.mark.skipif(
    shutil.which("singularity") is None, reason="no singularity available"
)

"""
Sample command:

pytest -vvs --basetemp=/scratch/Thu/nlo/tmpdir --duration=0 test_split.py

"""

#####################################################################

fmriprep_inputs = {
    "base_path": "/scratch/Thu/nlo",  # "/Users/gablab/Desktop/nlo/openmind/abide-pydra",
    "dataset": "abide2",
    "site": "USM",
    "fs_license": ".freesurfer_license.txt",
    "workdir": "fmriprep-workdir",
}
sbatch_args = "-t 20 --mem=4GB --cpus-per-task=1 -p gablab"

#####################################################################
# Run with linux/alphine

@need_singularity
def test_linux_1(plugin, tmpdir):
    """ split commands
    	linux container, no binding
    """
    cmd = ["pwd", "ls", "echo", "wc", "lh", "ss", "aw", "aa", "lk"]
    image = "library://sylabsed/linux/alpine"
    singu = SingularityTask(
        name="lin1", executable=cmd, image=image, cache_dir=tmpdir
    ).split("executable")

    res = singu(plugin=plugin)


@need_singularity
def test_linux_2(plugin, tmpdir):
    """ command with arguments in docker, checking the distribution
        splitter = image
    """
#    cmd = ["pwd", "ls", "echo", "wc", "lh", "ss", "aw", "aa", "lk"]
    cmd = ["pwd", "ls"]
    image = "library://sylabsed/linux/alpine"
    singu = SingularityTask(
        name="lin2", 
        executable=cmd, 
        image=image, 
        cache_dir=tmpdir,
        bindings=[(fmriprep_inputs["base_path"], "/BASE", "rw")],
    ).split("executable")

    res = singu(plugin=plugin)



@need_singularity
def test_linux_sub_1(plugin, tmpdir):
    """ split commands
    	linux container, no binding
    """
#    cmd = ["pwd", "ls", "echo", "wc", "lh", "ss", "aw", "aa", "lk"]
    cmd = ["pwd", "ls", ["echo", "hi"]]
    image = "library://sylabsed/linux/alpine"
    singu = SingularityTask(
        name="lin1", executable=cmd, image=image, cache_dir=tmpdir
    ).split("executable")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
    	singu(submitter=sub)
    res = singu.result()

@need_singularity
def test_linux_sub_2(plugin, tmpdir):
    """ command with arguments in docker, checking the distribution
        splitter = image
    """
    cmd = ["pwd", "ls", "echo", "wc", "lh", "ss", "aw", "aa", "lk"]
    image = "library://sylabsed/linux/alpine"
    singu = SingularityTask(
        name="lin2", 
        executable=cmd, 
        image=image, 
        cache_dir=tmpdir,
        bindings=[(fmriprep_inputs["base_path"], "/BASE", "rw")],
    ).split("executable")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
    	singu(submitter=sub)
    res = singu.result()

