'''
Author: Frank Brano Gomes
Github: iamu985
Program: A simple python script to search and play movies from 1337xxx.to a torrenting site.
Date: 2021-02-18
'''
import requests
import re
from time import sleep
import os

# Get the source code of the site using search url
# Get the very first link from the source code
# Go to the link and extract magnet link
# Open the magnet link in the terminal using peerflix

def format_search(search):
    # Formats the search
    return search.replace(" ", "+")

def get_links(url):
    source = requests.get(url)
    return re.findall(r'torrent/[0-9]+/[a-zA-Z0-9%?-]*/', str(source.text))

def get_magnet_link(url):
    source = requests.get(url)
    return re.findall(r"magnet:\?xt=urn:btih:[a-zA-Z0-9]*", str(source.text))

def clrscr():
    return os.system("clear")

def main():

    search = input("Search: ")
    query = format_search(search)
    search_url = f"https://1337xxx.to/search/{query}/1/"
    print(f"Searching for {search_url}...")
    magnet_url = get_links(search_url)[0]
    print("Searching done...")
    sleep(.3)
    clrscr()

    # getting the magnet link

    go_to_url = f"https://1337xxx.to/{magnet_url}"
    print(f'Preparing to fetch magnet link')
    magnet_link = get_magnet_link(go_to_url)[0]
    print("Magnet link fetched...")
    clrscr()
    print("Getting Ready to stream...")
    os.system(f'peerflix -k {magnet_link}')

if __name__ == '__main__':
    main()


