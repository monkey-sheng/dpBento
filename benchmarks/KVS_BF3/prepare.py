import os
import subprocess
import sys

def install_packages():
    # Install maven and git-lfs
    try:
        subprocess.run(["sudo", "apt", "install", "-y", "maven"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during installation: {e}")
        sys.exit(1)

def define_paths():
    # Get the directory where the current script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the relative paths for the .jar file and YCSB directory
    jar_path = os.path.join(script_dir, 'rocksdbjni-7.0.1-linux64.jar')
    ycsb_path = os.path.join(script_dir, 'YCSB')

    return jar_path, ycsb_path

def package_ycsb(ycsb_path):
    # Change to the YCSB directory and run the mvn command to package
    try:
        os.chdir(ycsb_path)
        subprocess.run(["mvn", "-pl", "site.ycsb:rocksdb-binding", "-am", "clean", "package"], check=True)
        print("YCSB package built successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during YCSB package build: {e}")
        sys.exit(1)

def install_rocksdb_jar(jar_path):
    # Install rocksdb jar using mvn install:install-file
    try:
        subprocess.run([
            "mvn", "install:install-file", 
            f"-Dfile={jar_path}", 
            "-DgroupId=org.rocksdb", 
            "-DartifactId=rocksdbjni", 
            "-Dversion=7.0.1", 
            "-Dpackaging=jar"
        ], check=True)
        print("rocksdbjni JAR installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred during rocksdbjni JAR installation: {e}")
        sys.exit(1)

def main():
    # Step 1: Install necessary packages
    install_packages()

    # Step 2: Define paths for the jar file and YCSB directory
    jar_path, ycsb_path = define_paths()

    # Step 3: Install the rocksdbjni JAR file
    install_rocksdb_jar(jar_path)

    # Step 4: Build YCSB rocksdb-binding
    package_ycsb(ycsb_path)

    

if __name__ == "__main__":
    main()
