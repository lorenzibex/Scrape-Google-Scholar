# Scrape-Google-Scholar
Google Scholar is a useful application. It refers every publications to its authors and allows to access easily the scientific output of every researcher. Two import key indicators are the number of citations and the H-Index. In this short python script you will see, how to extract/scrape these two parameters in Python.
To scrape Google Scholar we first load important libraries for this task and define a function, which is able to scrape the H-Index from a Google Scholar profile as long as we feed the function with the link to this profile. If this is the case the function returns the H-index.
