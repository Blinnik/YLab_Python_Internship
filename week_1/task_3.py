def zeros(n):
    zeros_count = 0
    if n:
        i = 1
        while((n / 5 ** i) >= 1):
            zeros_count += int((n / 5 ** i))
            i += 1
    return zeros_count
