# months.py
MONTHS = [
    None,  # 0 (brak)
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def month(n: int) -> str:
    """Return English month name for n in 1..12. Raises ValueError otherwise."""
    if 1 <= n <= 12:
        return MONTHS[n]
    raise ValueError("Month number must be in 1..12")
