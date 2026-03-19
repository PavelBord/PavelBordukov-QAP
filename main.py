from file_utils import read_lines, write_lines, count_words


def main():
    test_file = "test.txt"
    test_data = ["Apple", "Banana", "apple", "Orange", "lemon"]

    print("---- Тестирование write_lines ----")
    write_lines(test_file, test_data)
    print(f"Данные записаны в {test_file}")

    print("\n----Тестирование red_lines ---- ")
    lines = read_lines(test_file)
    print(f"Прочитона строк: {lines}")

    print("\n----Тестирование count_word ---- ")
    counts = count_words(test_file)
    print("Частотат слов: ")
    for word, count in counts.items():
        print(f" {word}: {count}")


if __name__ == "__main__":
    main()


