def count_occurrences(phrase: str, letter: str) -> int:

    count = 0
    phrase_low = phrase.lower()

    count = phrase_low.count(letter.lower())
    return count
