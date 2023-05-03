from django.shortcuts import render
from django.http import HttpResponse
from .models import Credential,Refrigerator,Shelf,Item

def index(request):
    return render(request,'index.html')
def createFridge(request):
    if(len(list(Refrigerator.objects.all().filter(primary_user=request.session.get('user')).values())) == 0):
        return render(request, 'createfridgepage.html')
    else:
        return HttpResponse("You already have a Fridge created. <a href='/homepage'> HomePage </a>")
    
def gotoaddFridge(request):
    if(len(list(Refrigerator.objects.all().filter(primary_user=request.session.get('user')).values())) == 0):
        return render(request,'createfridgepage.html')
    else:
        return HttpResponse("You already have a Fridge created. <a href='/fridgepage'> Access Fridge </a>")
    
def accessFridge(request):
    users = Credential.objects.get(email_id = request.session.get('user')).fridgeList
    if len(users) == 0:
        return HttpResponse ("you do not have any registered Refrigerator. <a href='/createFridge'> Create fridge</a> ")
    print(users)
    parms = {'users': users, 'Primary': request.session.get('user')}
    return render(request, 'accessFridge.html', parms)


def addFridgetoDB(request):
    params={'primary_user':str,
            'ref_height':int,
            'ref_width':int,
            'ref_depth':int,
            'fridge_height':int,
            'numberFridgeShelves':int,
            'freezer_height':int,
            'numberFreezerShelves':int,
            'fridgevolume':float,
            'freezervolume':float,
            'availablefridgevolume':float,
            'availablefreezervolume':float}
    
    
    ref_depth = request.GET.get('refdepth')
    ref_width = request.GET.get('refwidth')
    ref_height = request.GET.get('refheight')

    numberFridgeShelves = request.GET.get('fridgeshelfcount')
    numberFreezerShelves = request.GET.get('freezershelfcount')
    
    fridge_height = request.GET.get('fridgeheight')
    freezer_height = request.GET.get('freezerheight')
    
    fridgevolume = int(fridge_height)* int(ref_depth) * int(ref_width)
    freezervolume = int(freezer_height)* int(ref_depth) * int(ref_width)
    
    

    fridgeShelfHeight = int(fridge_height) / int(numberFridgeShelves)
    fridgeShelfVolume = fridgevolume / int(numberFreezerShelves)
    freezerShelfHeight = int(freezer_height) / int(numberFreezerShelves)
    freezerShelfVolume = freezervolume / int(numberFreezerShelves)
    
    for i in range(1,int(numberFridgeShelves)+1):
        a = 'fridgeShelf' + str(i)
        Shelf(primary_user=request.session.get('user'),
                name = a,
                height=fridgeShelfHeight,
                width=ref_width,
                depth=ref_depth,
                volumeFilled=0,
                availableVolume=fridgeShelfVolume,
                items_list=[]).save()
        
    for i in range(1,int(numberFreezerShelves)+1):
        a = 'freezerShelf' + str(i)
        Shelf(primary_user=request.session.get('user'),
                name = a,
                height=freezerShelfHeight,
                width=ref_width,
                depth=ref_depth,
                volumeFilled=0,
                availableVolume=freezerShelfVolume,
                items_list=[]).save()
    
    
    
    Refrigerator(primary_user=request.session.get('user'),
                ref_height=ref_height,
                ref_depth=ref_depth,
                ref_width=ref_width,
                fridge_height=fridge_height,
                freezer_height=freezer_height,
                numberFridgeShelves=numberFridgeShelves,
                numberFreezerShelves=numberFreezerShelves,
                fridgevolume=fridgevolume,
                freezervolume=freezervolume).save()
    

    

    Credential.objects.all().filter(email_id = request.session.get('user'))[0].addFridge(request.session.get('user'))
    Refrigerator.objects.all().filter(primary_user = request.session.get('user'))[0].addUser(request.session.get('user'))

    
    return HttpResponse("The Fridge was created Successfully. Go back to <a href= /homepage>homepage</a>")
    


def gotoFridge(request):
    ref = request.GET.get('fridge')
    emailid = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['primary_user'])
    ref_height = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['ref_height'])
    ref_depth = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['ref_depth'])
    ref_width = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['ref_width'])
    numberFridgeShelves = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['numberFridgeShelves'])
    numberFreezerShelves = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['numberFreezerShelves'])
    fridge_height = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['fridge_height'])
    freezer_height = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['freezer_height'])
    fridgevolume = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['fridgevolume'])
    freezervolume = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['freezervolume'])


    fridgeShelfHeight = int(fridge_height) / int(numberFridgeShelves)
    fridgeShelfVolume = fridgevolume / int(numberFreezerShelves)
    freezerShelfHeight = int(freezer_height) / int(numberFreezerShelves)
    freezerShelfVolume = freezervolume / int(numberFreezerShelves)
    
    shelves = (list(Shelf.objects.all().filter(primary_user=ref).values()))
        
        
    params={'primary_user': emailid,
                'ref_height':ref_height,
                'ref_width':ref_width,
                'ref_depth':ref_depth,
                'fridge_height':fridge_height,
                'numberFridgeShelves':numberFridgeShelves,
                'freezer_height':freezer_height,
                'numberFreezerShelves':numberFreezerShelves,
                'fridgeShelfHeight':fridgeShelfHeight,
                'freezerShelfHeight':freezerShelfHeight,
                'fridgeVolume':fridgevolume,
                'freezerVolume':freezervolume,
                'fridgeShelfVolume':fridgeShelfVolume,
                'freezerShelfVolume':freezerShelfVolume,
                'shelves':shelves
                }
    
    

    return render(request,'fridgepage.html',params)

def gotologin(request):
    return render(request,'loginPage.html')

def gotoregister(request):
    return render(request,'register.html') 
def  gotohomepage(request):
    return render(request,'homepage.html') 


def register(request):
    Password = request.GET.get('password')
    Email = request.GET.get('emailid')
    FirstName = request.GET.get('first name')
    LastName = request.GET.get('last name')

    if(len(list(Credential.objects.all().filter(email_id=Email).values())))==0:
        Credential(email_id=Email,password=Password,firstName=FirstName,lastName=LastName).save()
    else:
        return HttpResponse("You already have an account. Please <a href='/loginpage'> Login </a>")
    
    return render(request,'loginpage.html')

def varifylogin(request):
    request.session['pre_items'] = [
        {'name':'no selection'},
        {'name':'banana','height':15,'width':3,'depth':3},
        {'name':'milk','height':20,'width':10,'depth':10},
        {'name':'eggs','height':7,'width':20,'depth':10},
        {'name':'ice cream','height':15,'width':8,'depth':8},
        {'name':'butter','height':15,'width':7,'depth':7},
        {'name':'cheese','height':10,'width':15,'depth':7},
        {'name':'yogurt','height':10,'width':7,'depth':7},
        {'name':'bread','height':15,'width':10,'depth':10},
        {'name':'cake','height':15,'width':15,'depth':15},
        {'name':'strawberries','height':15,'width':10,'depth':10}
    ]
    Email = request.GET.get('emailid')
    request.session['currentRef'] = Email
    request.session['user'] = Email
    
    Password = request.GET.get('password')

    if(len(list(Credential.objects.all().filter(email_id=Email).values())))==1:
        if(Credential.objects.all().filter(email_id=Email).values()[0]['password'] == Password):
            return render(request,'homepage.html')
        else:
            return HttpResponse("Password Wrong <br> Please retry <a href='/loginpage'> Login </a>")
    else:
        return HttpResponse("Please retry <a href='/loginpage'> Login </a> OR <a href='/registerpage'> Register </a>")
    
    
def add_removeitemform(request):
    ref = request.GET.get('User')
    request.session['currentRef'] = ref
    noFreezerShelves = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['numberFreezerShelves'])
    freezercounter = ''.join([''+str(i) for i in range(1,noFreezerShelves)])
    noFridgeShelves = (Refrigerator.objects.all().filter(primary_user=ref).values()[0]['numberFridgeShelves'])
    fridgecounter = ''.join([''+str(i) for i in range(1,noFridgeShelves)])
    
    param= {'noFreezerShelves':noFreezerShelves,'freezercounter':freezercounter,'noFridgeShelves':noFridgeShelves,'fridgecounter':fridgecounter}
    
    return render(request,'add_removeitemform.html',param)

def additemtofridge(request):
    noFridgeShelves = (Refrigerator.objects.all().filter(primary_user=request.session.get('currentRef')).values()[0]['numberFridgeShelves'])

    fridgecounter = ''.join([''+str(i) for i in range(1,noFridgeShelves+1)])
    
    items = [i['name'] for i in request.session.get('pre_items')]
    
    param= {'noFridgeShelves':noFridgeShelves,'fridgecounter':fridgecounter,'item':items}
    return render(request,'additemtofridge.html',param)

def additemtofreezer(request):
    noFreezerShelves = (Refrigerator.objects.all().filter(primary_user=request.session.get('currentRef')).values()[0]['numberFreezerShelves'])
    
    freezercounter = ''.join([''+str(i) for i in range(1,noFreezerShelves+1)])    
    
    items = [i['name'] for i in request.session.get('pre_items')]
    param= {'noFreezerShelves':noFreezerShelves,'freezercounter':freezercounter,'item':items}
    return render(request,'additemtofreezer.html',param)


def additem(request):
    item_names = [i['name'] for i in request.session.get('pre_items')]
    selected_item = request.GET.get('selected item')
    if(selected_item != None):
        name = request.session.get('pre_items')[item_names.index(selected_item)]['name']
        email = request.session.get('user')
        height = request.session.get('pre_items')[item_names.index(selected_item)]['height']
        width = request.session.get('pre_items')[item_names.index(selected_item)]['width']
        depth = request.session.get('pre_items')[item_names.index(selected_item)]['depth']
        expiration = request.GET.get('expiration')
        shelfname = request.GET.get('shelf')
    else:
        name = request.GET.get('itemname')
        email = request.session.get('user')
        height = request.GET.get('itemheight')
        width = request.GET.get('itemwidth')
        depth = request.GET.get('itemdepth')
        expiration = request.GET.get('expiration')
        shelfname = request.GET.get('shelf')
    
    print(shelfname)
    
    if(Shelf.objects.get(name=shelfname,primary_user=request.session.get('currentRef')).addItem(name=name,itemHeight=height,itemWidth=width,itemDepth=depth,quantity=1)):
        Item(name=name,email=email,height=height,width=width,depth=depth,expiration=expiration).save()
    else:
        return HttpResponse("There is not enough space for this item. <a href='/additemtofridge'>GO back </a>")
        
    return HttpResponse("Item added! <a href='/accessFridge'> home </a>")


def gotofridgeshelf(request):
    noFridgeShelves = (Refrigerator.objects.all().filter(primary_user=request.session.get('currentRef')).values()[0]['numberFridgeShelves'])

    fridgecounter = ''.join([''+str(i) for i in range(1,noFridgeShelves+1)])
    
    param= {'noFridgeShelves':noFridgeShelves,'fridgecounter':fridgecounter}
    return render(request,'gotofridgeshelf.html',param)

def gotofreezershelf(request):
    noFreezerShelves = (Refrigerator.objects.all().filter(primary_user=request.session.get('currentRef')).values()[0]['numberFreezerShelves'])

    freezercounter = ''.join([''+str(i) for i in range(1,noFreezerShelves+1)])
    
    param= {'noFreezerShelves':noFreezerShelves,'freezercounter':freezercounter}
    return render(request,'gotofreezershelf.html',param)

def removeitemfromfridge(request):
    shelfname = request.GET.get('shelf')
    
    request.session['shelf'] = shelfname
    
    params = (Shelf.objects.get(name=shelfname,primary_user=request.session.get('currentRef')).items_list)
    param = {'name':[]}
    
    for i in params:
        param['name'].append(i['name'])
    
    if(len(param['name']) == 0):
        return HttpResponse("There are no items to remove <a href='/gotofridgeshelf'>go back</a>")
    
    return render(request,'removeitem.html',param)

def removeitemfromfreezer(request):
    shelfname = request.GET.get('shelf')
    
    request.session['shelf'] = shelfname
    
    params = (Shelf.objects.get(name=shelfname,primary_user=request.session.get('currentRef')).items_list)
    param = {'name':[]}
    
    for i in params:
        param['name'].append(i['name'])
    
    if(len(param['name']) == 0):
        return HttpResponse("There are no items to remove <a href='/gotofridgeshelf'>go back</a>")
    
    return render(request,'removeitem.html',param)


def add_removeUser(request):
    account = request.session.get('user')
    if Refrigerator.objects.all().filter(primary_user = account):
        userdict = Refrigerator.objects.all().filter(primary_user = account)[0].userList
        users = []
        for k, v in userdict.items():
            if k != account: 
                users.append(k)
        params = {'users' : users}
        return render(request, 'user_add_remove.html', params)
    return HttpResponse("You do not have a registered Rerigerator. <a href='/createFridge'>Create</a> one to add/remove users to it ")

def varify_remove_user(request):
    fridgeuser = request.GET.get('fridge')
    ownerId = request.session.get('user')
    if Refrigerator.objects.all().filter(primary_user = request.session.get('user'))[0].removeUser(fridgeuser):
        if Credential.objects.get(email_id = fridgeuser).removeFridge(ownerId):
            return HttpResponse(f"User {id} was succssfully removed. Go to <a href='/homepage'> Home </a> page" )
        else:
            return HttpResponse(f"meow,  Go to <a href='/homepage'> Home </a> page" )
    else:
        return HttpResponse(f"User {id} is either already removed or does not exist. Go to <a href='/homepage'> Home </a> page" )

def varify_add_User(request):
    newUser = request.GET.get('emailid')
    fridgeOwner = request.session.get('user')
    if Refrigerator.objects.all().filter(primary_user = fridgeOwner)[0].addUser(newUser) and Credential.objects.get(email_id = newUser).addFridge(fridgeOwner):
        return HttpResponse(f"User {id} was succssfully added. Go to <a href='/homepage'> Home </a> page" )
    else:
        return HttpResponse(f"User {id} is either already added or does not exist. Go to <a href='/homepage'> Home </a> page" )
    
    
def removeitem(request):
    itemname = request.GET.get('item')
    
    Shelf.objects.get(primary_user=request.session.get('currentRef'),name=request.session.get('shelf')).remove_item(itemname,1)
    
    return HttpResponse("Item removed <a href='/accessFridge'>go back</a>")