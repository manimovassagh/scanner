import subprocess
import sys

def run_gobuster(ip, wordlist_path):
    command = [
        'gobuster',
        'dir',
        '-u', f'https://{ip}',
        '-w', wordlist_path,
        '-l',
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running gobuster: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <IP> <wordlist_path>")
        sys.exit(1)

    ip = sys.argv[1]
    wordlist_path = sys.argv[2]

    run_gobuster(ip, wordlist_path)
