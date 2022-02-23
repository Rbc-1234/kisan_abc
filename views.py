from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import contest_category,contests,contest_price_list,contest_sponsor,users
from .forms import Contestcategory_Form,Create_Contest_Form,Sponcers_Form,Contest_Prize_Form,PYF_Form
import os
from django.shortcuts import render,redirect
# Create your views here.

class Home(View):
    def get(self,requests):
        return render(requests,'core/index.html')

class Create_Contest(View):
    def get(self,requests):
        data=contests.objects.all().order_by('-id')
        paginator= Paginator(data,4)
        page_number=requests.GET.get('page')
        pre = paginator.get_page(page_number)
        return render(requests,'core/create_contest_category.html',{'pre':pre})

class Createcontestcategory_edit(View):
    def get(self,requests,id):
        if(id==0):
            formm=Create_Contest_Form()
            concat=contest_category.objects.all()
            conpriz=contest_price_list.objects.all()
            spon=contest_sponsor.objects.all()
            return render(requests,'core/edit_create_contest_category.html',{'formm':formm,'concat':concat,'conpriz':conpriz,'spon':spon})
        else:
            concat=contest_category.objects.all()
            conpriz=contest_price_list.objects.all()
            spon=contest_sponsor.objects.all()
            data=contests.objects.get(id=id)
            formm=Create_Contest_Form(instance=data)
           
            return render(requests,'core/edit_create_contest_category.html',{'formm':formm,'data':data,'concat':concat,'conpriz':conpriz,'spon':spon})

    def post(self,requests,id):
        if(id==0):
            if requests.method =="POST":
                formm=Create_Contest_Form(requests.POST,requests.FILES)
                print(requests.POST)
                print(requests.FILES)
                kr=dict(requests.POST)["reamt"]
                all_positionamount=",".join(kr)
                if formm.is_valid():
                    ct=formm.cleaned_data['category']
                    ctt=formm.cleaned_data['contest_title']
                    qu=formm.cleaned_data['question']
                    cv=formm.cleaned_data['contest_venue']
                    csd=formm.cleaned_data['contest_schedule_date']
                    cst=formm.cleaned_data['contest_schedule_time']
                    uc=formm.cleaned_data['uploadContest']
                    ci=formm.cleaned_data['contest_image']
                    cty=formm.cleaned_data['contest_thumbnail']
                    vau=formm.cleaned_data['video_ad_url']
                    pd=formm.cleaned_data['prize_description']
                    dd=formm.cleaned_data['description']
                    ctc=formm.cleaned_data['contest_term_conditions']
                    nw=formm.cleaned_data['no_winner']
                    cit=formm.cleaned_data['contest_image_thumb']
                    ta=formm.cleaned_data['total_amount']
                    eqam=formm.cleaned_data['eqamount']
                    amtredio=formm.cleaned_data['amount_change']
                    newta=formm.cleaned_data['total_amount_nd']
                    pa=formm.cleaned_data['position_amount']
                    cwt=formm.cleaned_data['contestWinTitle']
                    cwat=formm.cleaned_data['contestWinAmountTitle']
                    csdd=formm.cleaned_data['contest_start_date']
                    cstt=formm.cleaned_data['contest_start_time']
                    cedd=formm.cleaned_data['contest_end_date']
                    cett=formm.cleaned_data['contest_end_time']
                    tp=formm.cleaned_data['type_price']
                    newtp=formm.cleaned_data['type_price_nd']
                    fea=formm.cleaned_data['feature_image']
                    mob=formm.cleaned_data['mobile_feature_img']
                    sid=formm.cleaned_data['sponsor_id']
                    aat=formm.cleaned_data['vac']
                    vat=formm.cleaned_data['video_ad_type']
                    vacc=formm.cleaned_data['video_ad_company']
                    vie=formm.cleaned_data['video_ad_time']
                    vast=formm.cleaned_data['video_ad_skip_time']
                    jj=formm.cleaned_data['dgc']
                    gaah=formm.cleaned_data['google_ad_after_header']
                    aahi=formm.cleaned_data['ad_after_header_image']
                    aahu=formm.cleaned_data['ad_after_header_url']
                    adt=formm.cleaned_data['ptg']
                    gas=formm.cleaned_data['google_ad_1_sidebar']
                    asis=formm.cleaned_data['ad_1_side_image']
                    asiuu=formm.cleaned_data['ad_1_side_url']
                    wdt=formm.cleaned_data['gpk']
                    gasi=formm.cleaned_data['google_ad_2_sidebar']
                    asid=formm.cleaned_data['ad_2_side_image']
                    atp=formm.cleaned_data['ad_2_side_url']
                    stat=formm.cleaned_data['status']
                    
                    
                    
                    kr=dict(requests.POST)["reamt"]
                    all_positionamount=",".join(kr)
                    print(all_positionamount)
                    if amtredio ==  'equalldivide':
                        crvk=contests(eqamount=eqam,category=ct,contest_title=ctt,question=qu,contest_venue=cv,contest_schedule_date=csd,contest_schedule_time=cst,uploadContest=uc,contest_image=ci,contest_thumbnail=cty,video_ad_url=vau,prize_description=pd,description=dd,contest_term_conditions=ctc,no_winner=nw,contest_image_thumb=cit,total_amount=ta,amount_change=amtredio,total_amount_nd=newta,position_amount=pa,contestWinTitle=cwt,contestWinAmountTitle=cwat,contest_start_date=csdd,contest_start_time=cstt,contest_end_date=cedd,contest_end_time=cett,type_price=tp,type_price_nd=newtp,feature_image=fea,mobile_feature_img=mob,sponsor_id=sid,vac=aat,video_ad_type=vat,video_ad_company=vacc,video_ad_time=vie,video_ad_skip_time=vast,dgc=jj,google_ad_after_header=gaah,ad_after_header_image=aahi,ad_after_header_url=aahu,ptg=adt,google_ad_1_sidebar=gas,ad_1_side_image=asis,ad_1_side_url=asiuu,gpk=wdt,google_ad_2_sidebar=gasi,ad_2_side_image=asid,ad_2_side_url=atp,status=stat)
                    else:
                        crvk=contests(reamt=all_positionamount,category=ct,contest_title=ctt,question=qu,contest_venue=cv,contest_schedule_date=csd,contest_schedule_time=cst,uploadContest=uc,contest_image=ci,contest_thumbnail=cty,video_ad_url=vau,prize_description=pd,description=dd,contest_term_conditions=ctc,no_winner=nw,contest_image_thumb=cit,total_amount=ta,amount_change=amtredio,total_amount_nd=newta,position_amount=pa,contestWinTitle=cwt,contestWinAmountTitle=cwat,contest_start_date=csdd,contest_start_time=cstt,contest_end_date=cedd,contest_end_time=cett,type_price=tp,type_price_nd=newtp,feature_image=fea,mobile_feature_img=mob,sponsor_id=sid,vac=aat,video_ad_type=vat,video_ad_company=vacc,video_ad_time=vie,video_ad_skip_time=vast,dgc=jj,google_ad_after_header=gaah,ad_after_header_image=aahi,ad_after_header_url=aahu,ptg=adt,google_ad_1_sidebar=gas,ad_1_side_image=asis,ad_1_side_url=asiuu,gpk=wdt,google_ad_2_sidebar=gasi,ad_2_side_image=asid,ad_2_side_url=atp,status=stat)
                    crvk.save()
                    return redirect('/create_contest_category')
                else:
                    return render(requests,'core/edit_create_contest_category.html',{'formm':formm})
        else:
            data=contests.objects.get(id=id)
            formm=Create_Contest_Form(requests.POST,instance=data)
            print(requests.POST)
            print(requests.FILES)
            if formm.is_valid():
                if requests.FILES.get('contest_image', False):
                    if requests.FILES.get=="":
                        os.remove(data.contest_image.path)
                    data.contest_image=requests.FILES['contest_image']

                if requests.FILES.get('contest_thumbnail', False):
                    if requests.FILES.get=="":
                        os.remove(data.contest_thumbnail.path)
                    data.contest_thumbnail=requests.FILES['contest_thumbnail']
                
                    
                
                if requests.FILES.get('contest_image_thumb', False):
                    os.remove(data.contest_image_thumb.path)
                    data.contest_image_thumb=requests.FILES['contest_image_thumb']

                if requests.FILES.get('feature_image', False):
                    os.remove(data.feature_image.path)
                    data.feature_image=requests.FILES['feature_image']

                if requests.FILES.get('mobile_feature_img', False):
                    os.remove(data.mobile_feature_img.path)
                    data.mobile_feature_img=requests.FILES['mobile_feature_img']

                if requests.FILES.get('ad_after_header_image', False):
                    os.remove(data.ad_after_header_image.path)
                    data.ad_after_header_image=requests.FILES['ad_after_header_image']

                if requests.FILES.get('ad_1_side_image', False):
                    os.remove(data.ad_1_side_image.path)
                    data.ad_1_side_image=requests.FILES['ad_1_side_image']
                
                if requests.FILES.get('ad_2_side_image', False):
                    os.remove(data.ad_2_side_image.path)
                    data.ad_2_side_image=requests.FILES['ad_2_side_image']

                formm.save()
                return redirect('/create_contest_category')
            else:
                return render(requests,'core/edit_create_contest_category.html',{'formm':formm})

class Contest_data(View):
    def get(self,requests):
        data=contest_category.objects.all().order_by('-id')
        paginator= Paginator(data,5)
        page_number=requests.GET.get('page')
        pre = paginator.get_page(page_number)
        return render(requests,'core/contest_home.html',{'pre':pre})

class Contestcategory_edit(View):
    def get(self,requests,id):
        if(id==0):
            form=Contestcategory_Form()
            return render(requests,'core/edit_contest_category.html',{'form':form})
        else:
            data=contest_category.objects.get(id=id)
            form=Contestcategory_Form(instance=data)
            return render(requests,'core/edit_contest_category.html',{'form':form,'data':data})

    def post(self,requests,id):
        if(id==0):
            form=Contestcategory_Form(requests.POST)
            if requests.method =="POST":
                masterstatus=requests.POST.get('masterstatus')
                searchst=contest_category.objects.filter(masterstatus=masterstatus)
            if form.is_valid():
                form.save()
                return redirect("/contest_home")
            else:
                name = requests.POST['name']
                slug = requests.POST['slug']
                color = requests.POST['color']
                parent_id = requests.POST['parent_id']
                description = requests.POST['description']
                created_at = requests.POST['created_at']
                updated_at = requests.POST['updated_at']
                masterstatus = requests.POST['masterstatus']
                obj = contest_category(name=name,slug=slug,color=color,parent_id=parent_id,description=description,created_at=created_at,updated_at=updated_at)
                form=Contestcategory_Form(requests.POST, instance=obj)
                return render(requests,'home/edit_contest_category.html',{'form':form,'obj':obj})
        else:
            data=contest_category.objects.get(id=id)
            form=Contestcategory_Form(requests.POST,instance=data)
            if form.is_valid():
                form.save()
                return redirect('/contest_home')
            else:
                return render(requests,'core/edit_contest_category.html',{'form':form})


class Sponcer_Home(View):
    def get(self,requests):
        pre=contest_sponsor.objects.all()
        paginator= Paginator(pre,5)
        page_number=requests.GET.get('page')
        sponsordata = paginator.get_page(page_number)
        print(sponsordata)
        return render(requests,'core/sponcer.html',{'sponsordata':sponsordata})

class Sponsor_edit(View):
    def get (self,requests,id):
        if (id==0):
            sponsorform=Sponcers_Form()
            return render(requests,'core/editsponcer.html',{'sponsorform':sponsorform})
        else:
            sponsordata=contest_sponsor.objects.get(id=id)
            sponsorform=Sponcers_Form(instance=sponsordata)
            return render(requests,'core/editsponcer.html',{'sponsorform':sponsorform,'sponsordata':sponsordata})
    def post(self,requests,id):
        if (id==0):
            sponsorform=Sponcers_Form(requests.POST, requests.FILES)
            print(requests.POST)
            print(requests.FILES)
            if requests.method == "POST":
                sponsorform=Sponcers_Form(requests.POST, requests.FILES)
                if sponsorform.is_valid():
                    ar=sponsorform.cleaned_data['online_presense']
                    br=sponsorform.cleaned_data['offline_presense']
                    cr=sponsorform.cleaned_data['brand_name']
                    dr=sponsorform.cleaned_data['company_name']
                    er=sponsorform.cleaned_data['web_url']
                    fr=sponsorform.cleaned_data['address']
                    gr=sponsorform.cleaned_data['state']
                    hr=sponsorform.cleaned_data['country']
                    ir=sponsorform.cleaned_data['company_phone']
                    jr=sponsorform.cleaned_data['company_gst']
                    kr=sponsorform.cleaned_data['company_logo']
                    lr=sponsorform.cleaned_data['person_name']
                    mr=sponsorform.cleaned_data['person_designation']
                    nr=sponsorform.cleaned_data['person_mobile']
                    pr=sponsorform.cleaned_data['person_mail']
                    sq=sponsorform.cleaned_data['status']
                    formdata=contest_sponsor(online_presense=ar,offline_presense=br,brand_name=cr,company_name=dr,web_url=er,address=fr,state=gr,country=hr,company_phone=ir,company_gst=jr,company_logo=kr,person_name=lr,person_designation=mr,person_mobile=nr,person_mail=pr,status=sq)
                    formdata.save()
                    return redirect('/sponcer')
                else:
                    return render(requests,'core/editsponcer.html',{'sponsorform':sponsorform})

        else:
            sponsordata=contest_sponsor.objects.get(id=id)
            if len(requests.FILES) !=0:
                if len(sponsordata.company_logo)>0:
                    os.remove(sponsordata.company_logo.path)
                    sponsordata.company_logo=requests.FILES['company_logo']
            sponsorform=Sponcers_Form(requests.POST,instance=sponsordata)
            if sponsorform.is_valid():
                sponsorform.save()
                return redirect('/sponcer')
            else:
                return render(requests,'core/editsponcer.html',{'sponsorform':sponsorform})
           
            
class Contest_Prize(View):
    def get(self,requests):
        pre=contest_price_list.objects.all()
        paginator=Paginator(pre,5)
        page_number=requests.GET.get('page')
        prizedata = paginator.get_page(page_number)
        return render(requests,'core/contest_prize_home.html',{'prizedata':prizedata})

class Contest_Prize_Edit(View):
    def get(self,requests,id):
        if (id==0):
            prize_form=Contest_Prize_Form()
            return render(requests,'core/contest_prize_edit.html')
        else:
            pre=contest_price_list.objects.get(id=id)
            prize_form=Contest_Prize_Form(instance=pre)
            return render(requests,'core/contest_prize_edit.html',{'pre':pre})
    def post(self,requests,id):
        if(id==0):
            prize_form=Contest_Prize_Form(requests.POST)
            if requests.method =="POST":
                if prize_form.is_valid():
                    kr=prize_form.cleaned_data['price_name']
                    jk=prize_form.cleaned_data['status']
                    ktp=contest_price_list(price_name=kr,status=jk)
                    prize_form.save()
                    return redirect('/contest_prize_home')
                else:
                    return render(requests,'core/contest_prize_edit.html')
        else:
            pre=contest_price_list.objects.get(id=id)
            prize_form=Contest_Prize_Form(requests.POST,instance=pre)
            if prize_form.is_valid():
                prize_form.save()
                return redirect('/contest_prize_home')
            else:
                return render(requests,'core/contest_prize_edit.html')


class PYF_Users_Home(View):
    def get(self,requests):
        pre=users.objects.all()
        paginator=Paginator(pre,5)
        page_number=requests.GET.get('page')
        xpdata = paginator.get_page(page_number)
        return render(requests,'core/pyf_user.html',{'xpdata':xpdata})

class PYF_Users_Edit(View):
    def get(self,requests,id):
        if (id==0):
            userform=PYF_Form()
            return render(requests,'core/pyfuser_edit.html',{'userform':userform})
        else:
            xpdata=users.objects.get(id=id)
            userform=PYF_Form(instance=xpdata)
            return render(requests,'core/pyfuser_edit.html',{'userform':userform})
    def post(self,requests,id):
        if (id==0):
            userform=PYF_Form(requests.POST)
            print(requests.POST)
            if requests.method=="POST":
                if userform.is_valid():
                    ac=userform.cleaned_data['name']
                    ad=userform.cleaned_data['full_name']
                    ae=userform.cleaned_data['email']
                    aj=userform.cleaned_data['mobile_no']
                    aah=userform.cleaned_data['user_status']
                    
                    usertb=users(name=ac,full_name=ad,email=ae,mobile_no=aj,status=aah)
                    usertb.save()
                    return redirect('/pyf_user')
                else:
                    return render(requests,'core/pyfuser_edit.html',{'userform':userform})
        
        











class User_logout(View):
    def get(self,requests):
        return render(requests,'core/logout.html')


                

def statusChangeUser(request):
    from django.forms.models import model_to_dict
    print('request: ',request.POST)
    try:
        userId = int(request.POST['userId'])
        userObj = users.objects.get(id__exact=userId)
        if userObj.user_status == 0:
            userObj.user_status = 1
            userObj.save()
        else:
            userObj.user_status = 0
            userObj.save()
        print(model_to_dict(userObj))
        return JsonResponse({'message':'success'},status=200)
    except Exception as e:
        print(e)
    return JsonResponse({'message':'failed'}, status=500)
        







                