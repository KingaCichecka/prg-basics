def time_string(hours, minutes, time_format):
    # formatowanie z zerami wiodącymi, np. 8:3 → 08:03
    if time_format == '24':
        return f"{hours:02}:{minutes:02}"

    elif time_format == '12':
        suffix = "am" if hours < 12 else "pm"
        hours_12 = hours % 12
        if hours_12 == 0:
            hours_12 = 12
        return f"{hours_12}:{minutes:02}{suffix}"


