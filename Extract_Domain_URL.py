import re
def domain_name(url):
    # domain=re.search('http',url)
    # domain=""
    # if url.startswith('http://www.'):
    #     domain=url[len('http://www.'):]
    # else:
    #     domain=url[len('http://'):]
    # domain_list=[]
    # for i in domain:
    #     if i == ".":
    #         break
    #     domain_list.append(i)

    # return  "".join(domain_list)
    pattern=r"(?:https?://)?(?:www.)?([^/.]+)"
    domains=re.search(pattern,url)
    if domains:
        domains=str(domains.group(1))
        # print(domains)
        # domains="".join(domains)
        
        # if domains.startswith("www."):
        #     domains=domains[len("www."):]
        return domains
    else:
        return ""
print(domain_name("http://github.com/carbonfive/raygun"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("http://www.bikes.org"))