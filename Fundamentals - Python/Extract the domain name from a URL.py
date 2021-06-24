""" Write a function that when given a URL as a string, parses out just the domain name and returns it as a string.

For example:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet" """


def domain_name(url):
    string = url.replace("www.","").replace("https://","").replace("http://","")
    return string[:string.find('.')]

#RW - 28/05/2021 
