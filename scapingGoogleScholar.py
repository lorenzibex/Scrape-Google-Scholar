import scholarly
import urllib2
def gethindex(search_address):
    response = urllib2.urlopen(search_address)
    html = response.read()#3
    if html.find("h-index</a></td><td class") == -1:
        pass #print "This site has not h-index
    else: # site is a valid patent site, after text searching and cleaning, attache title, abstract and claims to doclist
        #finds title text between the characters FONT size... and FONT
        hindex = html.split('h-index</a></td><td class="gsc_rsb_std">')[-1].split('</td><td class="gsc_rsb_std">')[0]
        return hindex

authorlist = ['Ulrich F. Keyser', 'Aleksandra Radenovic', 'Mahendran Radhakrishnan', 
              'Vivek Thacker', ' Silvia Hernandez-Ainsa','Nicholas Bell','Fernando Moreno Herrero', 'Cees Dekker' , 'Stefano Pagliara',
              'Ralph MM Smeets','Tim Liedl', 'Nadanai Laohakunakorn', 'Meni Wanunu',
          'Mark Akeson', 'Tim Albrecht','Dario Anselmetti', 'Rashid Bashir', 'Andreas B. Dahlin','Joshua B. Edel','Adam R. Hall',
          'Diego Krapf','MinJun Kim','Jeremy Lee', 'Derek Stein', 'Giovanni Maglia', 'Michael Mayer','Aleksandr Noy',  'mark platt',
      'Jacob Rosenstein','Friedrich C. Simmel','Vincent Tabard-Cossa','Gregory Timp', 'Anton Zilman','Michael Zwolak','Lorenz J. Steinbock' ]
hindexlist = [[],[],[]]
for i in authorlist:
    a = scholarly.search_author(i).next()
    hindexlist[0].append(i)
    search_query = scholarly.search_author(i)
    author = search_query.next().fill()
    link= str('https://scholar.google.com'+ a.url_citations)
    hindex = gethindex(link)
    hindexlist[1].append(hindex)
    hindexlist[2].append(a.citedby)
    
y= a[1]
y = map(int, y)
x= a[2]

fig, ax = plt.subplots(figsize=(8, 5))
ax.set(xscale="log", yscale="log")
ax.scatter(x,y)
ax.set_xlabel("Number of citations", fontsize=12)
ax.set_ylabel("H-Index", fontsize=12)
#plt.xlim(xmax=3)
plt.ylim(ymin=3)
for i, txt in enumerate(a[0]):
    ax.annotate( txt, ( x[i] , y[i]  ) )
