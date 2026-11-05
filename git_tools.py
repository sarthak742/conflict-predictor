
import subprocess


def run_git(args):
    result = subprocess.run(["git"] + args, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(f"Git {args} failed: {result.stderr}")
    return result.stdout
outputP = run_git(["--version"])
print(outputP)
outputF = run_git(["blahblah"])
print(outputF)
