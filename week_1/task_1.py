def domain_name(url):
    if url.find('//') != -1:
        url = url.split('//')[1]
    if url.startswith('www'):
        url = url.split('www.')[1]
    url = url.split('.')[0]
    return url
