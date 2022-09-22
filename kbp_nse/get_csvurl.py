import os
import requests
import asyncio
import time 
import aiohttp
from aiohttp.client import ClientSession
import nest_asyncio
nest_asyncio.apply()

def download_file(url: str, filename: str):
    ''' Downloads file from the url and save it as filename '''
    # check if file already exists
    if not os.path.isfile(filename):
        print('Downloading File: ' + filename)
        response = requests.get(url)
        # Check if the response is ok (200)
        if response.status_code == 200:
            # Open file and write the content
            with open(filename, 'wb') as file:
                # A chunk of 128 bytes
                for chunk in response:
                    file.write(chunk)
    else:
        print('File exists')

def CSV_URL(ex_hol):
    
    async def download_link(filename:str,url:str,session:ClientSession):
        async with session.get(url) as response:
            result = await response.text()
            # if not os.path.isfile(filename):
            #     print('Downloading File: ' + filename)
            #     response = requests.get(url)
            #     # Check if the response is ok (200)
            #     if response.status_code == 200:
            #         # Open file and write the content
            #         with open(filename, 'wb') as file:
            #             # A chunk of 128 bytes
            #             for chunk in response:
            #                 file.write(chunk)
            # else:
            #     print('File Exists')
            download_file(url, filename)

    async def download_all(urls:list, files:list):
        c = 0
        my_conn = aiohttp.TCPConnector(limit=10)
        async with aiohttp.ClientSession(connector=my_conn) as session:
            tasks = []
            for url in urls:
                task = asyncio.ensure_future(download_link(files[c],url=url,session=session))
                tasks.append(task)
                c+=1
            await asyncio.gather(*tasks,return_exceptions=True) # the await must be nest inside of the session

    url_list = []
    fname_list = []

    for i in ex_hol:
        monthstr = i.month
        if monthstr < 10:
            monthstr = "0" + str(monthstr)
        else:
            monthstr = str(monthstr)
        yearstr = str(i.year) 
        daystr = i.day
        if daystr < 10:
            daystr = "0" + str(daystr)
        else:
            daystr = str(i.day)


        url = "https://archives.nseindia.com/products/content/sec_bhavdata_full_{d}{m}{y}.csv".format(d = daystr, m=monthstr, y=yearstr)
        filename = 'bhav{d}{m}{y}.csv'.format(d=daystr, m=monthstr, y=yearstr)
        fname_list.append(filename)
        url_list.append(url)


    start = time.time()
    asyncio.run(download_all(url_list, fname_list))
    end = time.time()
    print(f'download {len(url_list)} links in {end - start} seconds')