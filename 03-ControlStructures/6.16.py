###
# 24h (hh:mm) -> 12h (h:mmpm/am)
#
time_24 = input("Enter time (24-hour format): ")

h_str, m_str = time_24.split(":")
h = int(h_str)
m = int(m_str)

suffix = "am" if h < 12 else "pm"
h12 = h % 12
if h12 == 0:
    h12 = 12

print(f"Time in 12-hour format: {h12}:{m_str:>02}{suffix}")
