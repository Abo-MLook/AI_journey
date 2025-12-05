import re
#part c
def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()

    pattern = r'(\d+\.\d+\.\d+\.\d+)\s+-\s+(\S+)\s+\[([^\]]+)\]\s+"([^"]+)"'

    matches = re.findall(pattern, logdata)

    result = []
    for host, user, time, request in matches:
        result.append({
            "host": host,
            "user_name": user,
            "time": time,
            "request": request
        })

    return result
