#!/usr/bin/env python3
"""
Pomodoro Timer Script
After every 25 minutes of work, shows a full-screen alert for a 2-minute break
Continues until killed with Ctrl+C
"""

import time
import subprocess
import sys
import signal
import os

# Configuration
WORK_MINUTES = 25
BREAK_MINUTES = 2

WORK_SECONDS = int(WORK_MINUTES * 60)
BREAK_SECONDS = int(BREAK_MINUTES * 60)

def show_break_alert():
    """Show a beautiful break alert using HTML in browser"""
    try:
        # Get absolute path to HTML file
        html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'break_alert.html')
        
        # Open in default browser
        if sys.platform == 'darwin':
            subprocess.Popen(['open', html_path])
        elif sys.platform == 'win32':
            subprocess.Popen(['start', html_path], shell=True)
        else:
            # Linux - try xdg-open
            subprocess.Popen(['xdg-open', html_path])
            
    except Exception as e:
        print(f"Error showing HTML alert: {e}")
        # Fallback to xmessage
        try:
            message = f"TAKE A BREAK!\n\nYou've worked for {WORK_MINUTES} minutes.\n\nTake a {BREAK_MINUTES} minute break.\n\nThis window will close when break is over."
            subprocess.Popen([
                'xmessage', '-center', '-timeout', str(int(BREAK_SECONDS)),
                '-title', 'BREAK TIME!', message
            ])
        except Exception as e2:
            print(f"Error showing xmessage fallback: {e2}")

def show_notification(title, message, urgency='normal', timeout=5000):
    """Show a desktop notification using notify-send"""
    try:
        subprocess.run([
            'notify-send', '-u', urgency, '-t', str(timeout),
            title, message
        ])
    except Exception as e:
        print(f"Error showing notification: {e}")

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    print("\n\nTimer stopped by user. Goodbye!")
    sys.exit(0)

def main():
    # Set up signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    print("Starting Pomodoro Timer...")
    print(f"Work interval: {WORK_MINUTES} minutes")
    print(f"Break interval: {BREAK_MINUTES} minutes")
    print("Press Ctrl+C to stop the timer\n")
    
    cycle_count = 1
    
    try:
        while True:
            # Work period
            print(f"Cycle {cycle_count}: Work for {WORK_MINUTES} minutes...")
            time.sleep(WORK_SECONDS)
            
            # Break alert
            print(f"Time for a {BREAK_MINUTES} minute break!")
            show_break_alert()
            show_notification(
                "BREAK TIME!", 
                f"Take a {BREAK_MINUTES} minute break. You've worked for {WORK_MINUTES} minutes.",
                urgency='critical',
                timeout=int(BREAK_SECONDS * 1000)
            )
            
            # Wait for the break period
            time.sleep(BREAK_SECONDS)
            
            # Break over notification
            print("Break over! Back to work.")
            
            # Show back to work HTML
            try:
                html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'work_resume.html')
                if sys.platform == 'darwin':
                    subprocess.Popen(['open', html_path])
                elif sys.platform == 'win32':
                    subprocess.Popen(['start', html_path], shell=True)
                else:
                    subprocess.Popen(['xdg-open', html_path])
            except Exception as e:
                print(f"Error showing work resume HTML: {e}")
            
            show_notification(
                "BACK TO WORK!", 
                f"Break is over. Time to focus for {WORK_MINUTES} minutes.",
                urgency='normal',
                timeout=5000
            )
            
            # Increment cycle count
            cycle_count += 1
            print()
            
    except KeyboardInterrupt:
        print("\n\nTimer stopped by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
