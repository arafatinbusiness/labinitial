#!/bin/bash

# Pomodoro Timer Script
# After every 25 minutes of work, shows a full-screen alert for a 2-minute break
# Continues until killed with Ctrl+C

WORK_MINUTES=25
BREAK_MINUTES=2

WORK_SECONDS=$((WORK_MINUTES * 60))
BREAK_SECONDS=$((BREAK_MINUTES * 60))

echo "Starting Pomodoro Timer..."
echo "Work interval: $WORK_MINUTES minutes"
echo "Break interval: $BREAK_MINUTES minutes"
echo "Press Ctrl+C to stop the timer"
echo ""

cycle_count=1

while true; do
    # Work period
    echo "Cycle $cycle_count: Work for $WORK_MINUTES minutes..."
    sleep $WORK_SECONDS
    
    # Break alert - full screen using xmessage
    echo "Time for a $BREAK_MINUTES minute break!"
    xmessage -center -timeout $BREAK_SECONDS -title "BREAK TIME!" \
        "TAKE A BREAK!\n\nYou've worked for $WORK_MINUTES minutes.\n\nTake a $BREAK_MINUTES minute break.\n\nThis window will close when break is over." &
    
    # Also send a desktop notification
    notify-send -u critical -t $((BREAK_SECONDS * 1000)) \
        "BREAK TIME!" "Take a $BREAK_MINUTES minute break. You've worked for $WORK_MINUTES minutes."
    
    # Wait for the break period
    sleep $BREAK_SECONDS
    
    # Break over notification
    echo "Break over! Back to work."
    notify-send -u normal -t 5000 \
        "BACK TO WORK!" "Break is over. Time to focus for $WORK_MINUTES minutes."
    
    # Increment cycle count
    ((cycle_count++))
    echo ""
done
