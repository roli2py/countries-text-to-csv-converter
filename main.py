import re


def parse_countries():
    with open("countries.txt", encoding="utf-8") as countries_file:
        countries = countries_file.read()
    countries = re.sub(r"\s*([а-яА-Я\-(),’—\s]+)\s+([A-Z]{2}).*", r"\2;\1\n", countries)
    countries_list = countries.split("\n")
    for index, country in enumerate(countries_list):
        if country == "":
            continue
        countries_list[index] = f"{index + 1};{country}"
    countries = "\n".join(countries_list)
    with open("parsed_countries.txt", "w", encoding="utf-8") as countries_file:
        countries_file.write(countries)


if __name__ == "__main__":
    parse_countries()
