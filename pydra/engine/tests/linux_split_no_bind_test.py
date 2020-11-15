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

pytest -vvs --basetemp=/scratch/Thu/nlo/tmpdir2 --durations=0 \
linux_split_no_bind_test.py |& tee output_linux_no_bind.out &

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


@need_singularity
def test_linux_sub_1(plugin, tmpdir):
    """ no splitting
    """
    cmd = "echo"
    args = "one"
    image = "library://sylabsed/linux/alpine"
    singu = SingularityTask(
        name="ln1", executable=cmd, args=args, image=image, cache_dir=tmpdir
    )

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()


@need_singularity
def test_linux_sub_3(plugin, tmpdir):
    """ split args, len 3
        fmriprep container, no binding
    """
    cmd = "echo"
    args = ["one", "two", "three"]
    image = "library://sylabsed/linux/alpine"
    singu = SingularityTask(
        name="ln3", executable=cmd, args=args, image=image, cache_dir=tmpdir
    ).split("args")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()


@need_singularity
def test_linux_sub_8(plugin, tmpdir):
    """ split args, len 8
        fmriprep container, no binding
    """
    cmd = "echo"
    args = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
    image = "library://sylabsed/linux/alpine"
    singu = SingularityTask(
        name="ln8", executable=cmd, args=args, image=image, cache_dir=tmpdir
    ).split("args")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()


@need_singularity
def test_linux_sub_30(plugin, tmpdir):
    """ split args, len 30
        fmriprep container, no binding
    """
    cmd = "echo"
    args = [str(x) for x in range(1, 31)]
    image = "library://sylabsed/linux/alpine"
    singu = SingularityTask(
        name="ln30", executable=cmd, args=args, image=image, cache_dir=tmpdir
    ).split("args")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()


@need_singularity
def test_linux_sub_100(plugin, tmpdir):
    """ split args, len 100
        fmriprep container, no binding
    """
    cmd = "echo"
    args = [str(x) for x in range(1, 101)]
    image = "library://sylabsed/linux/alpine"
    singu = SingularityTask(
        name="ln100", executable=cmd, args=args, image=image, cache_dir=tmpdir
    ).split("args")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()
