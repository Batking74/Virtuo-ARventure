import subprocess

def install_dependencies():
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])

def collect_static():
    subprocess.run(['python', 'manage.py', 'collectstatic'])

if __name__ == "__main__":
    install_dependencies()
    collect_static()