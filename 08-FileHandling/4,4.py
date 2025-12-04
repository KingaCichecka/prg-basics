# emails.py
import re

EMAIL_FILE = "email.txt"


def _read_email() -> str:
    """Wczytuje cały surowy email z pliku."""
    with open(EMAIL_FILE, "r", encoding="utf-8") as f:
        return f.read()


def email_sender() -> str | None:
    text = _read_email()
    match = re.search(r"^From: .*?<([^>]+)>", text, re.MULTILINE)
    return match.group(1) if match else None


def email_recipient() -> str | None:
    text = _read_email()
    match = re.search(r"^To: .*?<([^>]+)>", text, re.MULTILINE)
    return match.group(1) if match else None


def email_subject() -> str | None:
    text = _read_email()
    match = re.search(r"^Subject:\s*(.*)", text, re.MULTILINE)
    return match.group(1).strip() if match else None


def email_body() -> str:
    text = _read_email()
    # ciało maila zaczyna się po pustej linii
    parts = re.split(r"\n\s*\n", text, maxsplit=1)
    return parts[1].strip() if len(parts) > 1 else ""
