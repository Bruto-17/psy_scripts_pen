import os
import subprocess

# ANSI escape sequences for colors
RED = '\033[91m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Normal text for the header
header = """
PSY TOOLS
"""

# Stylish header and subheader
def display_header():
    print(f"{BOLD}{RED}{header}{RESET}")
    print(f"{BOLD}{RED}                   Web Texter{RESET}")
    print("\n")
    print(f"{CYAN}Push your limits... it's Bruto here!{RESET}")
    print("\n")
    print("This tool is open source.\n")

# Display Instagram handle
def display_instagram():
    print(f"Follow me on Instagram: {CYAN}bruto_17{RESET}\n")

# Function to install necessary tools
def install_tools():
    tools = [
        "sqlmap", "nmap", "subfinder", "sslscan", "gobuster", "dirb", "wpscan", 
        "nikto", "whatweb", "theharvester", "sublist3r", "metasploit", "hydra", 
        "enum4linux", "wafw00f", "nuclei", "xsstrike", "masscan", "zmap", "smtp-user-enum",
        "dnsenum", "arachni", "openvas", "osmedeus", "scapy", "burpsuite"
    ]
    
    for tool in tools:
        print(f"{CYAN}Checking for {tool}...{RESET}")
        if subprocess.call(f"command -v {tool}", shell=True) != 0:
            print(f"{RED}{tool} is not installed. Installing...{RESET}")
            if tool == "subfinder":
                os.system("pkg install -y golang")
                os.system("go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest")
            elif tool == "metasploit":
                os.system("pkg install -y metasploit")
            elif tool == "burpsuite":
                os.system("pkg install -y burpsuite")
            else:
                os.system(f"pkg install -y {tool}")
        else:
            print(f"{tool} is already installed.\n")

# Menu options for security vulnerability checks
def display_menu():
    print(f"{BOLD}Choose a security vulnerability check to perform:{RESET}")
    print("1. SQL Injection Scan")
    print("2. XSS (Cross-Site Scripting) Scan")
    print("3. Directory Traversal Scan")
    print("4. Open Ports Scan")
    print("5. CSRF (Cross-Site Request Forgery) Scan")
    print("6. Subdomain Enumeration")
    print("7. SSL/TLS Vulnerability Scan")
    print("8. Clickjacking Test")
    print("9. HTTP Security Headers Check")
    print("10. Directory Brute Forcing")
    print("11. Vulnerability Scanning")
    print("12. Web Application Fingerprinting")
    print("13. DNS Enumeration")
    print("14. Network Scanning")
    print("15. Credential Testing")
    print("16. Service Enumeration")
    print("17. OpenVAS Scanning")
    print("18. OSINT Gathering")
    print("19. Network Packet Analysis")
    print("20. Burp Suite Analysis")
    print("21. Web Application Scanning")
    print("22. Social Engineering Toolkit")
    print("23. Metasploit Exploitation")
    print("24. Scanning for WAFs")
    print("25. Exit")

# Perform security scans
def perform_scan(option, url):
    if option == "1":
        print(f"\n{RED}Performing SQL Injection Scan on {url}...{RESET}")
        os.system(f"sqlmap -u {url} --batch")
    elif option == "2":
        print(f"\n{RED}Performing XSS Scan on {url}...{RESET}")
        # Implement XSS scan logic here
    elif option == "3":
        print(f"\n{RED}Performing Directory Traversal Scan on {url}...{RESET}")
        # Implement directory traversal scan logic here
    elif option == "4":
        print(f"\n{RED}Performing Open Ports Scan on {url}...{RESET}")
        os.system(f"nmap -sV {url}")
    elif option == "5":
        print(f"\n{RED}Performing CSRF Scan on {url}...{RESET}")
        # Implement CSRF scan logic here
    elif option == "6":
        print(f"\n{RED}Performing Subdomain Enumeration on {url}...{RESET}")
        os.system(f"subfinder -d {url} -o subdomains.txt")
        print(f"{CYAN}Subdomain enumeration results saved to subdomains.txt{RESET}")
    elif option == "7":
        print(f"\n{RED}Performing SSL/TLS Vulnerability Scan on {url}...{RESET}")
        os.system(f"sslscan {url}")
    elif option == "8":
        print(f"\n{RED}Performing Clickjacking Test on {url}...{RESET}")
        # Implement Clickjacking test logic here
    elif option == "9":
        print(f"\n{RED}Performing HTTP Security Headers Check on {url}...{RESET}")
        os.system(f"curl -I {url}")
    elif option == "10":
        print(f"\n{RED}Performing Directory Brute Forcing on {url}...{RESET}")
        os.system(f"gobuster dir -u {url} -w /path/to/wordlist.txt")
    elif option == "11":
        print(f"\n{RED}Performing Vulnerability Scanning on {url}...{RESET}")
        os.system(f"nikto -h {url}")
    elif option == "12":
        print(f"\n{RED}Performing Web Application Fingerprinting on {url}...{RESET}")
        os.system(f"whatweb {url}")
    elif option == "13":
        print(f"\n{RED}Performing DNS Enumeration on {url}...{RESET}")
        os.system(f"dnsenum {url}")
    elif option == "14":
        print(f"\n{RED}Performing Network Scanning on {url}...{RESET}")
        os.system(f"masscan {url} -p0-65535")
    elif option == "15":
        print(f"\n{RED}Performing Credential Testing on {url}...{RESET}")
        os.system(f"hydra -L /path/to/userlist.txt -P /path/to/passlist.txt {url} ssh")
    elif option == "16":
        print(f"\n{RED}Performing Service Enumeration on {url}...{RESET}")
        os.system(f"enum4linux {url}")
    elif option == "17":
        print(f"\n{RED}Performing OpenVAS Scanning on {url}...{RESET}")
        os.system(f"openvas-nvt-sync && greenbone-nvt-sync && openvasmd --rebuild")
    elif option == "18":
        print(f"\n{RED}Performing OSINT Gathering on {url}...{RESET}")
        os.system(f"theharvester -d {url} -b all")
    elif option == "19":
        print(f"\n{RED}Performing Network Packet Analysis on {url}...{RESET}")
        os.system(f"scapy -c 'sniff(count=10, iface=eth0)'")
    elif option == "20":
        print(f"\n{RED}Performing Burp Suite Analysis on {url}...{RESET}")
        os.system(f"burpsuite -u {url}")
    elif option == "21":
        print(f"\n{RED}Performing Web Application Scanning on {url}...{RESET}")
        os.system(f"arachni {url}")
    elif option == "22":
        print(f"\n{RED}Performing Social Engineering Toolkit on {url}...{RESET}")
        os.system(f"setoolkit")
    elif option == "23":
        print(f"\n{RED}Performing Metasploit Exploitation on {url}...{RESET}")
        os.system(f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4444; run'")
    elif option == "24":
        print(f"\n{RED}Scanning for WAFs on {url}...{RESET}")
        os.system(f"wafw00f {url}")
    elif option == "25":
        print(f"\n{RED}Exiting...{RESET}")
        exit()
    else:
        print(f"\n{RED}Invalid option selected.{RESET}")

if __name__ == "__main__":
    display_header()
    display_instagram()

    install_tools()  # Install necessary tools at the start

    while True:
        display_menu()
        choice = input("\nEnter the number corresponding to your choice: ")
        if choice == "25":
            perform_scan(choice, "")
            break
        target_url = input("\nEnter the target URL: ")
        perform_scan(choice, target_url)

        another = input("\nWould you like to perform another scan? (y/n): ")
