import pandas as pd
import numpy as np

x = pd.read_excel('Book1.xlsx')
x.head()

x1 = x[x['Include?'] == 'Y']
# len(x1)

x1
x2 = x1.reset_index()
x2

x2.head()

x3 = np.asarray(x2['openalex_id'])
# x4 = [i.split('/')[-1] for i in x3]
# x4

x3[0]

x4 = x3[0:4]
x4

import asyncio
import httpx

async def do_tasks():
    async with httpx.AsyncClient() as client:
        tasks = [client.get(f"https://api.openalex.org/works?filter=concept.id:{i}.json()['meta']['count']") for i in x4]
        result = await asyncio.gather(*tasks)

x = do_tasks()