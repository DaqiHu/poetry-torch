import subprocess
import sys


def main():
    # Call this before torch to ensure the virtual environment is created.
    subprocess.check_call(["poetry", "install"])

    index_url = ""
    if sys.platform == "win32":
        index_url = "https://download.pytorch.org/whl/cu121"

    cmd_args = [] if index_url == "" else ["--index-url", index_url]

    subprocess.check_call(["poetry", "run", "pip", "install", "torch", "torchvision", "torchaudio"] + cmd_args)

    # Call this again to make sure torch will not violate `pyproject.toml`'s configurations.
    subprocess.check_call(["poetry", "install"])


if __name__ == "__main__":
    main()
