import random

def random_ip_generator():
    return f"192.168.1.{random.randint(0, 20)}"

def check_firewall_rules(ip, rules):
    for rule_ip,action in rules.items():
        if ip==rule_ip:
            return action
    return "allow"

def main(): firewall_rules

firewall_rules = {
        "192.168.1.1": "deny",
        "192.168.1.4": "deny",
        "192.168.1.9": "deny",
        "192.168.1.13": "allow",
        "192.168.1.16": "deny",
        "192.168.1.19": "allow",
    }

for _ in range(12):
    ip = random_ip_generator()
    action = check_firewall_rules(ip, firewall_rules)
    random_number = random.randint(0, 9999)
    print(f"IP: {ip}, Action: {action}, Random number: {random_number}")

if __name__ == "__main__":
    main()