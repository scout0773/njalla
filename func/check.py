import requests

def check(domain):
    available = []
    url = f'https://njal.la/list/?search={domain}&format=json'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'sessionid=uj11qqu5xemd42yyrdxqd7hzukwtx4fz; csrftoken=ToU5pGFo6lNDC2b8GXMdOSLfJ8A27Cwu',
        'DNT': '1',
        'Referer': f'https://njal.la/list/?search={domain}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for entry in data:
            if entry['status'] == 'available':
                available.append({"domain": entry['domain'], "status": entry['status'], "price": entry['price']})
        return available
    else:
        print(f"Failed to fetch data for {domain}")