ping = int(input())
ping_report = "low to average" if ping < 150 else "too high"

print("ping is :",ping_report)
