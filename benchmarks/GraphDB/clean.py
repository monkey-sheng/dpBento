import subprocess
import os
import logging
import shutil

def run_command(command, check=True, shell=False):
    """Run a shell command."""
    logging.info(f"Running command: {' '.join(command)}")
    try:
        subprocess.run(command, check=check, shell=shell)
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed with error: {e}")
        raise

def remove_directory(path):
    """Remove the specified directory if it exists."""
    if os.path.exists(path):
        shutil.rmtree(path)
        logging.info(f"Removed directory: {path}")

def main():
    logging.basicConfig(level=logging.INFO)

    # Get the directory of the clean.py script
    benchmark_dir = os.path.dirname(os.path.abspath(__file__))
    logging.info(f"Benchmark directory: {benchmark_dir}")

    # Uninstall Python package
    run_command(['pip', 'uninstall', '-y', 'kuzu'])

    # Remove system packages (Note: this doesn't remove dependencies)
    run_command(['sudo', 'apt', 'remove', '-y', 'zstd', 'wget', 'unzip'])

    # Clean up any unused dependencies
    run_command(['sudo', 'apt', 'autoremove', '-y'])

    # Remove the results directory
    results_dir = os.path.join(benchmark_dir, "results")
    remove_directory(results_dir)


    logging.info("Cleanup complete")

if __name__ == "__main__":
    main()
