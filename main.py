import requests


def main():
    url_london = 'https://wttr.in/london?MnTqu&lang=ru'
    response_london = requests.get(url_london)
    response_london.raise_for_status()
    print(response_london.text)


    url_sheremetyevo_airport = 'https://wttr.in/svo?MnTqu&lang=ru'
    response_sheremetyevo_airport = requests.get(url_sheremetyevo_airport)
    response_sheremetyevo_airport.raise_for_status()
    print(response_sheremetyevo_airport.text)


    url_cherepovets = 'https://wttr.in/%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D1%86?MnTqu&lang=ru'
    response_cherepovets = requests.get(url_cherepovets)
    response_cherepovets.raise_for_status()
    print(response_cherepovets.text)


if __name__ == "__main__":
    main()
