import time

def set_alarm():
    print("Enter the time for the alarm in 24-hour format (HH:MM:SS)")
    alarm_time = input("> ")
    return alarm_time

def main():
    print("Simple Python Alarm Clock")
    alarm_time = set_alarm()
    
    while True:
        current_time = time.strftime("%H:%M:%S")
        
        if current_time == alarm_time:
            print("ALARM! Wake up!")
            break
        
        print("Current time:", current_time)
        time.sleep(1)  # Wait for 1 second before checking again
    
    print("Alarm stopped.")

if __name__ == "__main__":
    main()
