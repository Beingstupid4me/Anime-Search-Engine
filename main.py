import http.client

connection = http.client.HTTPSConnection("myanimelist.p.rapidapi.com")
headings = {
    'X-RapidAPI-Key': "999d31b00bmsh5942b9845d12d9bp1caf26jsn9679f45bd47b",
    'X-RapidAPI-Host': "myanimelist.p.rapidapi.com"
    }
l=list(map(str,input("Enter the name of anime you want to search ").split()))
r="%20".join(l)
connection.request("GET", "/anime/search/"+r+"/10", headers=headings)
response1 = connection.getresponse()
data = response1.read()
string=data.decode("utf-8")
tupl=eval(string[1:-1])
n2=1
d={}
d2={}
for j in tupl:
    for k in j:
        if k=="title":
                        print ("\n",n2," - ",j[k]+"\n")
                        d2[n2]=j[k]
        if k=="description":
                        print(j[k])
        if k=="myanimelist_id":
                        id=j[k]
                        d[n2]=id
    n2=n2+1

option=int(input("\n"+"Enter the serial number - "))
ad=str(d[option])
connection2 = http.client.HTTPSConnection("myanimelist.p.rapidapi.com")
headings2 = {
    'X-RapidAPI-Key': "999d31b00bmsh5942b9845d12d9bp1caf26jsn9679f45bd47b",
    'X-RapidAPI-Host': "myanimelist.p.rapidapi.com"
    }
connection2.request("GET", "/anime/"+ad, headers=headings2)
response2 = connection2.getresponse()
data2 = response2.read()
w=data2.decode("utf-8")
st=eval(w)

print("\n",d2[option],"\n")

for i in st:
    if i=="synopsis":
        print(i.capitalize())
        print("\n",st[i])