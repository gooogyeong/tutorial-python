import requests, sys, webbrowser, bs4

# Read the command line arguments from sys.argv.
search_word = '+'.join(sys.argv[1:])
print(search_word)

# Fetch the search result page with the requests module.
pypi_res=requests.get(f'https://pypi.org/search/?q={search_word}&o=')
pypi_res.raise_for_status()

# Find the links to each search result.
pypi_soup = bs4.BeautifulSoup(pypi_res.text, 'html.parser')
search_result_a_tags=pypi_soup.select('a.package-snippet')
search_result_hrefs = list(map(lambda link: link.get('href'), search_result_a_tags))[:1]
print(search_result_hrefs)

# Call the webbrowser.open() function to open the web browser.
# webbrowser.open('')
new=2
for i in range(0, len(search_result_hrefs)):
    if i == 1:
        new=2
    webbrowser.open_new(f'https://pypi.org{search_result_hrefs[i]}')