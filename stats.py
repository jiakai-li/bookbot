from collections import Counter


def get_num_words(content: str) -> int:
    return len(content.split())


def get_num_chars(content: str) -> dict[str, int]:
    lower_content = filter(
        lambda c: c != " ",
        (c.lower() for c in content)
    )
    return Counter(lower_content)


def format_char_dict(char_counts: dict[str, int]) -> list[dict[str, int]]:
    res = [
        {"char": k, "num": v} for (k, v) in char_counts.items() if k.isalpha()
    ]
    res.sort(reverse=True, key=lambda item: item["num"])
    return res
