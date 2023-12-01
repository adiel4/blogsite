from django.shortcuts import render, redirect

# Create your views here.

posts = [{
    "Title": "dkslgjsldkg",
    "Description": "gsklgsd",
    "Author": "adi",
    "Date": "akglagdl"
}]


def indexpage(request):
    return render(request, "index.html ", {"articles": posts, "page": "index"})


def aboutpage(request):
    return render(request, 'about.html', {"page": "about"})


def contactpage(request):
    if request.method == "GET":
        return render(request, "contact.html", {"page": "contact"})
    else:
        print(request.POST)
        file = open('D:/contact_results.txt','w')
        file.writelines(f"Name: {request.POST['name'].encode('utf-8', 'ignore')},Email: {request.POST['email'].encode('utf-8', 'ignore')},Subject: {request.POST['subject'].encode('utf-8', 'ignore')}")
        return redirect(contactpage)
