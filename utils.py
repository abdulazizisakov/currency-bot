def str_to_float(value: str) -> float | None:
    try:
        return float(value)
    except:
        return None
