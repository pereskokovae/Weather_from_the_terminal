import requests


def main():
    payload = {
        "MnTq": " ",
        "lang": "ru"
        }
    place = ["london", "svo", "Череповц"]
    for urls in place:
        url = (f'https://wttr.in/{urls}')
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == "__main__":
    main()
