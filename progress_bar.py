
import time
import sys

# Terminal colours
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
PURPLE = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

# Project heading
print("\n" + "=" * 55)
print(f"{BOLD}{CYAN}          PYTHON PROGRESS BAR SIMULATOR{RESET}")
print("=" * 55)

print("\nWelcome! Let's get your task completed.")

# Get task details
task = input("\nEnter your task name: ")

print("\nSelect loading speed:")
print("1. Slow")
print("2. Normal")
print("3. Fast")

choice = input("\nChoose speed (1-3): ")

# Set animation speed
if choice == "1":
    delay = 0.08
elif choice == "3":
    delay = 0.01
else:
    delay = 0.04

# Progress bar settings
total = 100
bar_length = 35
spinner = ["|", "/", "-", "\\"]

print(f"\n{YELLOW}Preparing: {task}{RESET}")
print("\nStarting your task...\n")

start_time = time.perf_counter()

# Main progress bar loop
for progress in range(total + 1):

    filled = int(bar_length * progress / total)
    empty = bar_length - filled

    bar = GREEN + "█" * filled + RESET
    bar += "-" * empty

    spin = spinner[progress % len(spinner)]

    # Display different status messages
    if progress < 25:
        status = "Initializing..."
    elif progress < 50:
        status = "Processing..."
    elif progress < 75:
        status = "Almost there..."
    elif progress < 100:
        status = "Finalizing..."
    else:
        status = "Completed!"

    # Display live progress
    sys.stdout.write(
        f"\r{CYAN}{spin}{RESET} "
        f"[{bar}] "
        f"{BOLD}{progress:3d}%{RESET} "
        f"| {PURPLE}{status}{RESET} "
    )

    sys.stdout.flush()

    time.sleep(delay)

# Calculate total time
end_time = time.perf_counter()
elapsed = end_time - start_time

# Completion message
print("\n\n" + "=" * 55)
print(f"{GREEN}{BOLD}          TASK COMPLETED SUCCESSFULLY!{RESET}")
print("=" * 55)

print(f"\nTask Name : {task}")
print(f"Progress  : 100%")
print(f"Time Taken: {elapsed:.2f} seconds")

print(f"\n{CYAN}Thank you for using the Progress Bar Simulator!{RESET}\n")
