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
from .models import remotePC, ueList, btsList, tm500, btsPC, tm500PC

# Create your views here.

def index(request):
    # display all remote pcs #
    getPCS = remotePC.objects.all()
    getBTS = btsList.objects.all()
    getUE = ueList.objects.all()
    getTM = tm500.objects.all()
    getBTSPC = btsPC.objects.all()
    getTMPC = tm500PC.objects.all()

    if request.method == "POST":
        operation = request.POST['operation']

        # add a new remote pc
        if operation == "add":
            display_name = request.POST['display_name']
            server_name = request.POST['server_name']
            ussername = request.POST['ussername']
            pass_word = request.POST['pass_word']
            do_main = request.POST['do_main']
            u_e = request.POST['u_e']
            try:
                b_t_s = request.POST['b_t_s']
                if not (btsList.objects.filter(bts = b_t_s).exists()):
                    newBTS = btsList(bts = b_t_s)
                    newBTS.save()
            except:
                pass
            #print(server_name)
            if remotePC.objects.filter(serverName = server_name).exists():
                messages.error(request, 'Cannot Add Remote PC')
            else:
                try:
                    # print(display_name, server_name, ussername, pass_word, do_main, b_t_s, u_e)
                    newRPC = remotePC(serverName = server_name)
                    newRPC.save()
                    # print(u_e)
                    if (u_e == "Test Terminal"):
                        newBTS = btsPC(displayName = display_name, serverName = server_name, username = ussername, password = pass_word, domain = do_main, bts = b_t_s, ue = u_e)
                        newBTS.save()
                    elif (u_e == "TM500"):
                        t_e_n_v = request.POST['t_e_n_v']
                        try:
                            b_t_s = request.POST['b_t_s']
                            newTM = tm500PC(displayName = display_name, serverName = server_name, username = ussername, password = pass_word, domain = do_main, bts = b_t_s, ue = u_e, tenv = t_e_n_v)
                            newTM.save()
                        except:
                            newTM = tm500PC(displayName = display_name, serverName = server_name, username = ussername, password = pass_word, domain = do_main, ue = u_e, tenv = t_e_n_v)
                            newTM.save()
                    if not (ueList.objects.filter(ue = u_e).exists()):
                        newUE = ueList(ue = u_e)
                        newUE.save()
                    messages.success(request, 'Successfully Added')
                except IntegrityError as e:
                    messages.error(request, 'ERROR')

        # delete multiple rpcs
        elif operation == "delete":
            server_list = request.POST.getlist('server_name')
            for ip in server_list:
                print(ip)
                remotePC.objects.get(serverName = ip).delete()
                if btsPC.objects.filter(serverName = ip).exists():
                    btsPC.objects.get(serverName = ip).delete()
                elif tm500PC.objects.filter(serverName = ip).exists():
                    tm500PC.objects.get(serverName = ip).delete()

        # delete a single rpc
        elif operation == "del_indiv":
            dip = request.POST['deleteID']
            # print(dip)
            remotePC.objects.get(serverName = dip).delete()
            if btsPC.objects.filter(serverName = dip).exists():
                btsPC.objects.get(serverName = dip).delete()
            elif tm500PC.objects.filter(serverName = dip).exists():
                tm500PC.objects.get(serverName = dip).delete()

        # update rpc info
        elif operation == "update":
            ipe = request.POST['editID']
            editDN = request.POST['editDN']
            editUN = request.POST['editUN']
            editPW = request.POST['editPW']
            editDM = request.POST['editDM']
            editUE = request.POST['editUE']
            try:
                editBTS = request.POST['editBTS']
                if (editUE == "Test Terminal"):
                    btsPC.objects.filter(serverName = ipe).update(displayName = editDN, username = editUN, password = editPW, domain = editDM, bts = editBTS, ue = editUE)
                elif (editUE == "TM500"):
                    editTNV = request.POST['editTENV']
                    tm500PC.objects.filter(serverName = ipe).update(displayName = editDN, username = editUN, password = editPW, domain = editDM, bts = editBTS, ue = editUE, tenv = editTNV)
            except:
                if (editUE == "TM500"):
                    editTNV = request.POST['editTENV']
                    tm500PC.objects.filter(serverName = ipe).update(displayName = editDN, username = editUN, password = editPW, domain = editDM, ue = editUE, tenv = editTNV)
            messages.success(request, 'Successfully Updated')
    context = {
        "getPCS" : getPCS,
        "getBTS" : getBTS,
        "getUE" : getUE,
        "getTM" : getTM,
        "getBTSPC" : getBTSPC,
        "getTMPC" : getTMPC,
    }
    return render(request, 'index.html', context)

def bts(request):
    getBTS = btsList.objects.all()

    if request.method == "POST":
        operation = request.POST['operation']

        # add new bts
        if operation == "add":
            new_bts = request.POST['b_t_s']
            if btsList.objects.filter(bts = new_bts).exists():
                messages.error(request, "Cannot add new BTS")
            else:
                try:
                    newBTS = btsList(bts = new_bts)
                    newBTS.save()
                except IntegrityError as e:
                    messages.error(request, "Cannot add new BTS")

        # edit bts
        elif operation == "update":
            new_bts = request.POST['editBTS']
            old_bts = request.POST['oldBTS']
            # print(old_bts)
            btsList.objects.filter(bts = old_bts).update(bts = new_bts)
            messages.success(request, 'Successfully Updated')

        # delete single
        elif operation == "del_indiv":
            dbts = request.POST['deleteBTS']
            btsList.objects.get(bts = dbts).delete()

        # delete multiple
        elif operation == "delete":
            bts_list = request.POST.getlist('b_t_s')
            for ip in bts_list:
                # print(ip)
                btsList.objects.get(bts = ip).delete()
    context = {
        "getBTS" : getBTS,
    }
    return render(request, 'bts.html', context)

def ue(request):
    getUE = ueList.objects.all()

    if request.method == "POST":
        operation = request.POST['operation']

        # add new ue
        if operation == "add":
            new_ue = request.POST['u_e']
            if ueList.objects.filter(ue = new_ue).exists():
                messages.error(request, "Cannot add new UE")
            else:
                try:
                    newUE = ueList(ue = new_ue)
                    newUE.save()
                except IntegrityError as e:
                    messages.error(request, "Cannot add new UE")

        # edit ue info
        elif operation == "update":
            new_ue = request.POST['editUE']
            old_ue = request.POST['oldUE']
            # print(old_bts)
            ueList.objects.filter(ue = old_ue).update(ue = new_ue)
            messages.success(request, 'Successfully Updated')

        # delete single
        elif operation == "del_indiv":
            due = request.POST['deleteUE']
            ueList.objects.get(ue = due).delete()

        # delete multiple
        elif operation == "delete":
            ue_list = request.POST.getlist('u_e')
            for ip in ue_list:
                # print(ip)
                ueList.objects.get(ue = ip).delete()
    context = {
        "getUE" : getUE,
    }
    return render(request, 'ue.html', context)