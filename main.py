import argparse
import os
import shutil
import subprocess
import sys

# DATA_FILE is the dir we expect requirements file to be available in
DATA_FILE = os.environ.get("DATA_FILE", "/data")

parser = argparse.ArgumentParser(description="CLI tool for generating lambda layer dependencies in python")
parser.add_argument("--requirements-file",
                    default="requirements.txt",
                    help="Name of your dependencies requirements file (default: requirements.txt)")
parser.add_argument("--artifact-file", default="pkg",
                    help="Name of your output artifact zip file (default: pkg)")

if __name__ == '__main__':
    args = parser.parse_args(sys.argv[1:])

    # use workdir to locate files
    requirements_file = f"{DATA_FILE}/{args.requirements_file}"
    artifact_file = f"{DATA_FILE}/{args.artifact_file}"

    # pip install into artifact
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file, "-t", artifact_file])

    # zip the artifact into same dir
    shutil.make_archive(f"{artifact_file}", 'zip', artifact_file)
