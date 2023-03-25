from os import write
from bs4 import BeautifulSoup
from time import sleep
import requests

print("Put a skill you're not familiar with")
unfamiliar_skill = input('>')
print(f'Filtering {unfamiliar_skill}')


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation='
        ).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        publish_date = job.find('span', class_='sim-posted').text
        print(index, job)
        if 'few' in publish_date or '1' in publish_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_= 'srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company name: {company_name.strip()}\n')
                    f.write(f'Required skills: {skills.strip()}\n')
                    f.write(f'More info: {more_info}')
                print(f'File saved:{index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Wait {time_wait} minutes...')
        sleep(time_wait*60)
