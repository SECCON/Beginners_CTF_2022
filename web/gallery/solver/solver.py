import requests, os

def check(url: str) -> str:
    """
    check returns 0 if solver runs correctly.
    If not, returns 1 or 2.
    """
    try:
        headers = {'Range': 'bytes=0-10239'}
        resp = requests.get(url + "/images/flag_7a96139e-71a2-4381-bf31-adf37df94c04.pdf", headers=headers)
        pdf0 = resp.content

        headers = {'Range': 'bytes=10240-20480'}
        resp = requests.get(url + "/images/flag_7a96139e-71a2-4381-bf31-adf37df94c04.pdf", headers=headers)
        pdf1 = resp.content

        ans = pdf0 + pdf1
        
        # want = "ctf4b{Ser14liz4t10n_15_v1rtually_pl41ntext}"
        want = ""

        with open('flag_7a96139e-71a2-4381-bf31-adf37df94c04.pdf', 'rb') as f:
            want = f.read()

            # flag check
            if want == ans:
                return 0
            else:
                return 1

    except Exception as e:
        print(e)
        return 2

if __name__ == "__main__":
    host = os.getenv('CTF4B_HOST', 'localhost')
    port = int(os.getenv('CTF4B_PORT', '80'))
    server_url = "http://"+host+":"+str(port)
    print(server_url)
    print(check(server_url))
