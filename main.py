from typing import Dict, List


def main() -> None:
    with open("./books/frankenstein.txt") as f:
        book = f.read()

        print("--- Begin report of book ---")
        print(f"{count_words(book)} words found in the document")
        print("\n")
        for item in sort_dict(count_letters(book)):
            print(f"The '{item["letter"]}' character was found {item["num"]} times")


def sort_on(d: Dict[str, int]) -> int:
    return d["num"]


def sort_dict(letters: Dict[str, int]) -> List[Dict[str, int]]:
    res = []
    for row in letters:
        res.append({"letter": row, "num": letters[row]})

    if len(res) > 0:
        res.sort(reverse=True, key=sort_on)
        return res

    raise Exception("Something went wrong")


def count_words(book: str) -> int:
    return len(book.split())


def count_letters(book: str) -> Dict[str, int]:
    count = {}
    for letter in book:
        lett = letter.lower()
        if lett.isalpha():
            if lett in count:
                count[lett] += 1
            else:
                count[lett] = 1

    return count


if __name__ == "__main__":
    main()
