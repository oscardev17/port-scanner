# ================================== #
# This program was created by Oscar  #
# ================================== #

import socket, os
from concurrent.futures import ThreadPoolExecutor
from pystyle import Colors

def uwu(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return port, True
        else:
            return port, False
    except Exception as e:
        return port, False

def owo(ip, start_port, end_port):
    print(f"\n [{Colors.cyan}>{Colors.white}] Scanning {ip} from port {start_port} to {end_port}...")
    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(uwu, ip, port) for port in range(start_port, end_port + 1)]
        for future in futures:
            port, is_open = future.result()
            if is_open:
                open_ports.append(port)

    return open_ports

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    print(Colors.cyan+"""\n        ____             __     _____                                 \n       / __ \____  _____/ /_   / ___/_________ _____  ____  ___  _____\n      / /_/ / __ \/ ___/ __/   \__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/\n     / ____/ /_/ / /  / /_    ___/ / /__/ /_/ / / / / / / /  __/ /    \n    /_/    \____/_/   \__/   /____/\___/\__,_/_/ /_/_/ /_/\___/_/     \n                                                                  """+Colors.reset)

    target_ip = input(f" [{Colors.cyan}~{Colors.white}] Enter the IP address to scan: ").strip()
    try:
        start_port = int(input(f" [{Colors.cyan}~{Colors.white}] Enter the starting port (eg 1): ").strip())
        end_port = int(input(f" [{Colors.cyan}~{Colors.white}] Enter the end port (eg 1024): ").strip())
    except ValueError:
        print(f"\n [{Colors.red}!{Colors.white}] Invalid input. Please enter a valid number for ports.")
        exit(1)

    open_ports = owo(target_ip, start_port, end_port)

    if open_ports:
        print(f"\n [{Colors.green}+{Colors.white}] Open ports on {target_ip} : {', '.join(map(str, open_ports))}")
    else:
        print(f"\n [{Colors.red}+{Colors.white}] No open ports detected on {target_ip} between {start_port} and {end_port}.")
