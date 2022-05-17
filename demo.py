import os

if __name__ == "__main__":
    print("The message was", os.environ.get("my_message", "NO MESSAGE SET"))
