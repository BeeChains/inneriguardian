import dns.resolver

def fetch_agi_logs():
    """ Fetch AI logs stored in Handshake DNS TXT records """
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ["127.0.0.1"]  # hnsd local resolver
    logs = resolver.resolve("AGI-logs.iinc", "TXT")
    for log in logs:
        print(f"📝 AI Log: {log.to_text()}")

fetch_agi_logs()
