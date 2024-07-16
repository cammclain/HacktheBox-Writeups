# Hack the Box Lab Writeup 1 
## Box: Blurry


## Introduction / Initial Assessment

After scanning with nmap, I found port 80 open.

After adding the target IP to my `/etc/hosts` I navigate to `http://blurry.htb`


When you navigate to this *URL* it redirects you to `http://app.blurry.htb`

![clear-ml getting started](clear-ml-getting-started.png)


This application appears to be "ClearML" based. 

ClearML is an open source project, I am going to go research more since it is available on Github, but from what I can tell, this is a `web application` for machine learning.

- it offers API access
- it offers a `dashboard`


After assessing the [ClearML project on Github](https://github.com/allegroai/clearml), I found that what I was looking for was a `dashboard` for `ClearML` known as the [Orchestration Dashboard](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/).

Something worth noting is according to this `README.md`, the dashboard has access to **your entire compute cluster (Cloud / Kubernetes / On-Prem)**



## Tangent 1: Creds

generate credentials:

```bash
curl 'http://app.blurry.htb/api/v2.27/auth.create_credentials' -X POST -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0' -H 'Accept: application/json' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'Referer: http://app.blurry.htb/dashboard' -H 'X-Allegro-Client: Webapp-1.13.1-426' -H 'Content-Type: application/json' -H 'Origin: http://app.blurry.htb' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Cookie: clearml_token_basic=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoX3R5cGUiOiJCZWFyZXIiLCJpZGVudGl0eSI6eyJjb21wYW55IjoiZDFiZDkyYTNiMDM5NDAwY2JhZmM2MGE3YTViMWU1MmIiLCJ1c2VyIjoiYmRlNjY3ZmJiMDY5NGRlODljNmNlYjg5MjQyZmE5MTQiLCJ1c2VyX25hbWUiOiJjYW0iLCJyb2xlIjoidXNlciIsImNvbXBhbnlfbmFtZSI6ImNsZWFybWwifSwiZW52IjoiPHVua25vd24-IiwiZXhwIjoxNzIzNjQ5MjkzLCJpYXQiOjE3MjEwNTcyOTMsImFwaV92ZXJzaW9uIjoiMi4yNyIsInNlcnZlcl92ZXJzaW9uIjoiMS4xMy4xIiwic2VydmVyX2J1aWxkIjoiNDI2IiwiZmVhdHVyZV9zZXQiOiJiYXNpYyJ9._Wezam9pVlRQnemf8tN_4kKKcsFtSFwyHQCjA6ovTMA' -H 'Priority: u=0' --data-raw '{}'
```

My first thought is, can this be spammed to generate a lot of creds? I have had ideas before that would involve abusing AI systems but would require a large number of creds to rotate through. That gives this avenue some validity. I believe this would be worth reporting on because it seems like something that could be done & desireable for threat actors.

## Tangent 2: Prompt Injection

