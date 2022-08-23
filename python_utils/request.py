import os
import requests

url = "https://adventofcode.com/2021/day/{}/input"

def get_input(day: int) -> str:
	formatted_url = url.format(day)

	resp = requests.get(formatted_url, cookies={"session": os.getenv("AOC_SESSION")})
	return resp.text.removesuffix("\n")
