import requests, bs4, os

url='https://xkcd.com'

os.makedirs('xkcd', exist_ok=True) # exist_ok=True: if the directory already exists, don't raise an exception

# Repeats until it reaches the first comic
for page in range(0, 5):
    # Loads the XKCD home page
    xkcd_res=requests.get(url)
    xkcd_res.raise_for_status()

    # Saves the comic image on that page
    xkcd_soup=bs4.BeautifulSoup(xkcd_res.text, 'html.parser')
    # Follows the Previous Comic link
    
    xkcd_comic_img_src=xkcd_soup.select('#comic img')[0].get('src')

    xkcd_comic_img_res=requests.get(f'https:{xkcd_comic_img_src}')
    file_name=os.path.basename(f'https:{xkcd_comic_img_src}')
    xkcd_comic_img_res.raise_for_status()
    xkcd_comic_file=open(f'xkcd/{file_name}', 'wb')
    for chunk in xkcd_comic_img_res.iter_content(100000):
        xkcd_comic_file.write(chunk)
    xkcd_comic_file.close()

    xkcd_prev_href=xkcd_soup.select('a[rel="prev"]')[0].get('href')
    url=f'https://xkcd.com{xkcd_prev_href}'
    # print(xkcd_prev_href) # /2835/