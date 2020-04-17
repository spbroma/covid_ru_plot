import requests

def load_csv():
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQxbLiOGzM5mC_lBFk3t3XWp_3ZMsoEObxiQErZAfEqx_DAu9l6Qe2FMdggwD3EVIIcB6m3VwUOH33Y/pub?gid=1542861087&single=true&output=csv'

    myfile = requests.get(url)
    open('data.csv', 'wb').write(myfile.content)
    print('CSV is loaded')
