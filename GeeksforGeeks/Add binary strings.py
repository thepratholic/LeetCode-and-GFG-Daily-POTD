def add_binary_strings(s1, s2):
    s1 = s1.lstrip('0')
    s2 = s2.lstrip('0')

    if not s1: s1 = "0"
    if not s2: s2 = "0"

    max_len = max(len(s1), len(s2))
    s1 = s1.zfill(max_len)
    s2 = s2.zfill(max_len)

    carry = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        bit1 = int(s1[i])
        bit2 = int(s2[i])
        total = bit1 + bit2 + carry
        result.append(str(total % 2))  # Result bit
        carry = total // 2            # Carry bit

    # Step 4: Handle final carry
    if carry:
        result.append('1')

    result = ''.join(reversed(result))

    return result.lstrip('0') or '0'
