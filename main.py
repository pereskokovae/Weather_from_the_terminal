import requests


def main():
    urls = [
        'https://wttr.in/london?MnTqu&lang=ru',
        'https://wttr.in/svo?MnTqu&lang=ru',
        'https://wttr.in/%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D1%86?MnTqu&lang=ru'
        ]


    for url in urls:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    main()
