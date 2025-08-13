import os

def update_env_counter():
    count = int(os.environ.get("FILE_OPEN_COUNT", 0))
    count += 1
    os.environ["FILE_OPEN_COUNT"] = str(count)
    print(f"The file has been opened {count} times (in this session).")

update_env_counter()
