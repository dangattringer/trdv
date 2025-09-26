import json
import random
import string


def format_message(func, param_list):
    """Formats a message for the TradingView WebSocket."""
    msg = json.dumps({"m": func, "p": param_list}, separators=(",", ":"))
    return f"~m~{len(msg)}~m~{msg}"


def generate_session_id(prefix: str) -> str:
    """Generates a random 12-character session ID with a given prefix."""
    return f"{prefix}_{''.join(random.choices(string.ascii_letters + string.digits, k=12))}"
