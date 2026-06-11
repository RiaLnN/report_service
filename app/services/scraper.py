from core.constants import GIT_HUB_TRENDING_URL
from bs4 import BeautifulSoup
import httpx


async def get_page() -> str:
    async with httpx.AsyncClient() as client:
        page = await client.get(
            GIT_HUB_TRENDING_URL,
            timeout=60.0,
        )
    return page.text


async def parse_page(reps_count: int = 2):
    html = await get_page()
    soup = BeautifulSoup(html, 'lxml')
    reps = soup.find_all('article')[:reps_count]

    result = []
    for rep in reps:
        title_el = rep.select_one('h2')
        author, title = title_el.a.text.split('/') if title_el and title_el.a else 'N/A'
        author, title = author.strip(), title.strip()
        link = ''.join(['https://github.com', title_el.a['href']] if title_el and title_el.a else '' )
        desc_el = rep.select_one('p')
        desc = desc_el.text.strip() if desc_el else 'No description provide'

        lang_el = rep.select_one('[itemprop="programmingLanguage"]')
        lang = lang_el.text if lang_el else 'N/A'
        star_el = rep.select_one('[aria-label="star"]')
        stars = star_el.parent.text.strip() if star_el and star_el.parent else 0
        forks_el = rep.select_one('[aria-label="fork"]')
        forks = forks_el.parent.text.strip() if forks_el and forks_el.parent else 0

        result.append(
            {
                'title': title,
                'author': author,
                'description': desc,
                'language': lang,
                'stars': stars,
                'forks': forks,
                'link': link
            }
        )
    return result
