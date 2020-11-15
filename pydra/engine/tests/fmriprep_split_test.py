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

pytest -vvs --basetemp=/scratch/Thu/nlo/tmpdir --duration=0 test_split_fmriprep.py

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
# Run with fmriprep


@need_singularity
def test_no_sub_1(plugin, tmpdir):
    """ split commands
    	fmriprep container, no binding
    """
    cmd = ["pwd", "ls", "echo", "wc", "lh", "ss", "aw", "aa", "lk"]
    image = "/om4/group/gablab/data/singularity-images/fmriprep-v1.3.0p2.sif"
    singu = SingularityTask(
        name="fp1", executable=cmd, image=image, cache_dir=tmpdir
    ).split("executable")

    res = singu(plugin=plugin)


@need_singularity
def test_no_sub_2(plugin, tmpdir):
    """ command with arguments in docker, checking the distribution
        splitter = image
    """
    cmd = ["pwd", "ls", "echo", "wc", "lh", "ss", "aw", "aa", "lk"]
    image = "/om4/group/gablab/data/singularity-images/fmriprep-v1.3.0p2.sif"
    singu = SingularityTask(
        name="fp2",
        executable=cmd,
        image=image,
        cache_dir=tmpdir,
        bindings=[(fmriprep_inputs["base_path"], "/BASE", "rw")],
    ).split("executable")

    res = singu(plugin=plugin)


#####################################################################
# With submitter, vary length of list to split to test time


@need_singularity
def test_sub_1(plugin, tmpdir):
    """ no splitting
    """
    cmd = "echo"
    args = "one"
    image = "/om4/group/gablab/data/singularity-images/fmriprep-v1.3.0p2.sif"
    singu = SingularityTask(
        name="fp_sub1", executable=cmd, args=args, image=image, cache_dir=tmpdir
    )

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()


@need_singularity
def test_sub_2(plugin, tmpdir):
    """ split args, len 2
        fmriprep container, no binding
    """
    cmd = "echo"
    args = ["one", "two"]
    image = "/om4/group/gablab/data/singularity-images/fmriprep-v1.3.0p2.sif"
    singu = SingularityTask(
        name="fp_sub2", executable=cmd, args=args, image=image, cache_dir=tmpdir
    ).split("args")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()


@need_singularity
def test_sub_2(plugin, tmpdir):
    """ split args, len 2
        fmriprep container, no binding
    """
    cmd = "echo"
    args = ["one", "two", "three"]
    image = "/om4/group/gablab/data/singularity-images/fmriprep-v1.3.0p2.sif"
    singu = SingularityTask(
        name="fp_sub3", executable=cmd, args=args, image=image, cache_dir=tmpdir
    ).split("args")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()


@need_singularity
def test_sub_3(plugin, tmpdir):
    """ split args, len 3
        fmriprep container, no binding
    """
    cmd = "echo"
    args = ["one", "two", "three"]
    image = "/om4/group/gablab/data/singularity-images/fmriprep-v1.3.0p2.sif"
    singu = SingularityTask(
        name="fp_sub3", executable=cmd, args=args, image=image, cache_dir=tmpdir
    ).split("args")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()


@need_singularity
def test_sub_5(plugin, tmpdir):
    """ split args, len 3
        fmriprep container, no binding
    """
    cmd = "echo"
    args = ["one", "two", "three", "four", "five"]
    image = "/om4/group/gablab/data/singularity-images/fmriprep-v1.3.0p2.sif"
    singu = SingularityTask(
        name="fp_sub5", executable=cmd, args=args, image=image, cache_dir=tmpdir
    ).split("args")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()


@need_singularity
def test_sub_8(plugin, tmpdir):
    """ split args, len 3
        fmriprep container, no binding
    """
    cmd = "echo"
    args = ["one", "two", "three", "four", "five", "six", "seven", "eight"]
    image = "/om4/group/gablab/data/singularity-images/fmriprep-v1.3.0p2.sif"
    singu = SingularityTask(
        name="fp_sub8", executable=cmd, args=args, image=image, cache_dir=tmpdir
    ).split("args")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)

    res = singu.result()


#####################################################################
# With submitter


@need_singularity
def test_sub_bind_2(plugin, tmpdir):
    """ command with arguments in docker, checking the distribution
        splitter = image
    """
    cmd = ["pwd", "ls", "echo", "wc", "lh", "ss", "aw", "aa", "lk"]
    image = "/om4/group/gablab/data/singularity-images/fmriprep-v1.3.0p2.sif"
    singu = SingularityTask(
        name="fp_sub2",
        executable=cmd,
        image=image,
        cache_dir=tmpdir,
        bindings=[(fmriprep_inputs["base_path"], "/BASE", "rw")],
    ).split("executable")

    with Submitter(plugin=plugin, sbatch_args=sbatch_args) as sub:
        singu(submitter=sub)
