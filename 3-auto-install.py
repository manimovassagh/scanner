#!/usr/bin/env python3

import subprocess

# List of basic packages to install
basic_packages = ["neovim", "cowsay", "fortune", "burpsuite"]

# List of penetration testing tools similar to Kali/Parrot
pentest_packages = [
    "nmap", "metasploit-framework", "wireshark", "john", "hydra", "sqlmap",
    "nikto", "netcat", "dnsutils", "dirb", "nbtscan", "zaproxy", "sqlninja",
    "aircrack-ng", "bettercap", "maltego", "recon-ng", "setoolkit", "wpscan",
    "hashcat", "cewl", "gobuster", "enum4linux", "fierce", "skipfish",
    "wifite", "crackmapexec", "mitmproxy", "beef-xss", "veil", "thc-hydra",
    "burp", "owasp-zap", "sqlmate", "sqlsus", "w3af", "sqlradar",
    "unicornscan", "dsniff", "yersinia", "angr", "binwalk", "bed",
    "dnsrecon", "exif", "hping3", "inguma", "lbd", "maltego", "msfpc",
    "rec-studio", "recon-ng", "regeorg", "routersploit", "xsser", "yersinia",
    "sqliv", "wifiphisher", "netdiscover", "dnsenum", "netool",
    "xspy", "zarp", "bearded", "pyrit", "hydra", "sublist3r", "amass",
    "metagoofil", "patator", "theharvester", "golismero", "p0f", "yersinia",
    "pybozocrack", "pyrit", "reaver", "truecrack", "vulnerability-identification-script",
    "volatility", "winexe", "socat", "sqlsus", "sqlmap", "skipfish", "setoolkit",
    "recon-ng", "netdiscover", "nikto", "nbtscan", "maltego", "lynis", "joomscan",
    "dirbuster", "dnsenum", "dnswalk", "darkstat", "creddump", "cisco-torch", "bluelog"
]

# Update package lists
subprocess.run(["sudo", "apt", "update"])

# Install basic packages
subprocess.run(["sudo", "apt", "install", "-y"] + basic_packages)

# Install penetration testing tools
subprocess.run(["sudo", "apt", "install", "-y"] + pentest_packages)

print("Installation complete.")