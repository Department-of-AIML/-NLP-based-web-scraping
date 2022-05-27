from bs4 import BeautifulSoup
import requests
import time

print(' Put some skill you are not familiar with')              # used to filter unnecessary options
unfamiliar_skill = input('>')
print(f"Filtering out {unfamiliar_skill}")

def find_jobs():                                                # defining the web scraping program
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text,'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in published_date:                              # searching for latest job opportunities
            company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','')
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:               # creating text files containing job details
                try:
                    with open(f'posts/post_{index}.txt', 'w') as f:
                        f.write(f"Company Name: {company_name.strip()}\n")
                        f.write(f"Required Skills: {skills.strip()}\n")
                        f.write(f'More Info: {more_info}\n')
                    print(f'File saved: {index}')
                except:
                    print("File path does not exist")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)
