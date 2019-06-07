from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages 
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError

### modules ###
import platform
import os

### imports ###
from .models import remotePC
from .forms import addNewRPC

# Create your views here.

def index(request):
    # display all remote pcs #
    getPCS = remotePC.objects.all()

    if request.method == "POST":
        operation = request.POST['operation']

        # add a new remote pc
        if operation == "add":
            display_name = request.POST['display_name']
            server_name = request.POST['server_name']
            ussername = request.POST['ussername']
            pass_word = request.POST['pass_word']
            do_main = request.POST['do_main']
            b_t_s = request.POST['b_t_s']
            u_e = request.POST['u_e']
            #print(server_name)
            if remotePC.objects.filter(serverName = server_name).exists():
                messages.error(request, 'Cannot Add Remote PC')
            else:
                try:
                    newRPC = remotePC(displayName = display_name, serverName = server_name, username = ussername, password = pass_word, domain = do_main, bts = b_t_s, ue = u_e)
                    newRPC.save()
                    messages.success(request, 'Successfully Added')
                except IntegrityError as e:
                    messages.error(request, 'Cannot Add Remote PC')

        # delete multiple rpcs
        elif operation == "delete":
            server_list = request.POST.getlist('server_name')
            for ip in server_list:
                print(ip)
                remotePC.objects.get(serverName = ip).delete()

        # delete a single rpc
        elif operation == "del_indiv":
            dip = request.POST['deleteID']
            print(dip)
            remotePC.objects.get(serverName = dip).delete()

        # update rpc info
        elif operation == "update":
            ipe = request.POST['editID']
            editDN = request.POST['editDN']
            editUN = request.POST['editUN']
            editPW = request.POST['editPW']
            editDM = request.POST['editDM']
            editBTS = request.POST['editBTS']
            editUE = request.POST['editUE']
            remotePC.objects.filter(serverName = ipe).update(displayName = editDN, username = editUN, password = editPW, domain = editDM, bts = editBTS, ue = editUE)
            messages.success(request, 'Successfully Updated')
    context = {
        "getPCS" : getPCS
    }
    return render(request, 'index.html', context)