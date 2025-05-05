from datetime import datetime

def log_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("test.txt", "a") as f:
        f.write(f"{current_time}\n")

if __name__ == "__main__":
    log_time() 