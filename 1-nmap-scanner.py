import subprocess
from datetime import datetime

def run_nmap(target_ip):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = f'{timestamp}-scan.log'
    command = f'nmap -sC -sV -oA nmap_results {target_ip} | tee {output_file}'
    
    try:
        subprocess.run(command, shell=True, check=True)
        print("\nNmap scan completed successfully.")
        print(f"Nmap output saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running Nmap: {e}")

if __name__ == "__main__":
    target_ip = input("Enter the target IP address: ")
    run_nmap(target_ip)
