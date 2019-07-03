from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic.edit import FormView

### modules ###
import platform
import os
from io import BytesIO
from PIL import Image
import re
import subprocess

### imports ###
from .models import UE_LIST, BTS_PC, tm500PC, BTS_INFO, BTS_MODULES

# Create your views here.

def index(request):
    # display all remote pcs #
    getBTSPC = BTS_PC.objects.all()  # get bts pcs
    getUE = UE_LIST.objects.all()    # get ue types
    getTMPC = tm500PC.objects.all() # get tm500 pcs
    getBTSINFO = BTS_INFO.objects.all() # get bts pc info
    getBTSMOD = BTS_MODULES.objects.all()
    # newnew = btsPCInfo(serverName=btsPC.objects.get(serverName='10.12.25.11'), WCDMAPilot = '12345')
    # newnew.save()

    if request.method == "POST":
        operation = request.POST['operation']

        ##############################################################
        ################### BTS PC OPERATIONS ########################
        ##############################################################
        if operation == "add-bts":
            server_name = request.POST['server_name']
            display_name = request.POST['display_name']
            ussername = request.POST['username']
            pass_word = request.POST['password']
            do_main = request.POST['do_main']
            u_e = request.POST['u_e']
            sport = request.POST['sport']
            txta = request.POST['txta']
            rack = request.POST['rack']
            s_n = request.POST['s_n']
            p_n = request.POST['p_n']
            a_n = request.POST['a_n']
            # tm_500 = request.POST['tm_500']
            # t_t = request.POST['t_t']

            print(server_name, display_name, ussername, pass_word, do_main, u_e, sport, txta, rack)
            try:
                '''newBTS = BTS_PC(ip=server_name, display_name=display_name, username=ussername, password=pass_word, domain=do_main, ue_type=u_e, switch_port=sport, notes=txta, rack=rack, serial_number=s_n, product_number=p_n, asset_number=a_n)
                newBTS.save()
                print("added")'''
                if u_e == 'TM500':
                    tm_500 = request.POST['tm_500']
                    print(tm_500)
                    #newBTS = BTS_PC(ip=server_name, display_name=display_name, username=ussername, password=pass_word, domain=do_main, ue_type=u_e, switch_port=sport, notes=txta, rack=rack, serial_number=s_n, product_number=p_n, asset_number=a_n, tm500_pc_id=tm500PC.objects.get(serverName=tm_500))
                    #newBTS.save()
                    if BTS_PC.objects.filter(ip = server_name).exists():
                        messages.error(request, 'Cannot Add BTS PC')
                    else:
                        try:
                            bts_info = request.POST['bts_info_id']
                            print("bts_info: ", bts_info)
                            newBTS = BTS_PC(ip=server_name, display_name=display_name, username=ussername, password=pass_word, domain=do_main, ue_type=u_e, switch_port=sport, notes=txta, rack=rack, serial_number=s_n, product_number=p_n, asset_number=a_n, tm500_pc_id=tm500PC.objects.get(serverName=tm_500), bts_info_id=BTS_INFO.objects.get(bts_name=bts_info))
                            newBTS.save()
                        except:
                            print("no bts info")
                            newBTS = BTS_PC(ip=server_name, display_name=display_name, username=ussername, password=pass_word, domain=do_main, ue_type=u_e, switch_port=sport, notes=txta, rack=rack, serial_number=s_n, product_number=p_n, asset_number=a_n, tm500_pc_id=tm_500)
                            newBTS.save()
                        messages.success(request, 'Successfully Added')
                elif u_e == "Test Terminal":
                    t_t = request.POST['t_t']
                    print(t_t)
                    if BTS_PC.objects.filter(ip = server_name).exists():
                        messages.error(request, 'Cannot Add BTS PC')
                    else:
                        try:
                            bts_info = request.POST['bts_info_id']
                            print("bts_info: ", bts_info)
                            newBTS = BTS_PC(ip=server_name, display_name=display_name, username=ussername, password=pass_word, domain=do_main, ue_type=u_e, switch_port=sport, notes=txta, rack=rack, serial_number=s_n, product_number=p_n, asset_number=a_n, tt_info_id=BTS_INFO.objects.get(bts_name=t_t), bts_info_id=BTS_INFO.objects.get(bts_name=bts_info))
                            newBTS.save()
                        except:
                            print("no bts info")
                            newBTS = BTS_PC(ip=server_name, display_name=display_name, username=ussername, password=pass_word, domain=do_main, ue_type=u_e, switch_port=sport, notes=txta, rack=rack, serial_number=s_n, product_number=p_n, asset_number=a_n, tt_info_id=BTS_INFO.objects.get(bts_name=t_t))
                            newBTS.save()
                        messages.success(request, 'Successfully Added')
            except:
                    messages.error(request, 'ERROR')

        elif operation == "update-bts":
            server_name = request.POST['editID']
            display_name = request.POST['editDN']
            ussername = request.POST['editUN']
            pass_word = request.POST['editPW']
            do_main = request.POST['editDM']
            u_e = request.POST['editUE']
            sport = request.POST['editSPort']
            txta = request.POST['editNotes']
            rack = request.POST['editRack']
            s_n = request.POST['editSNum']
            p_n = request.POST['editPNum']
            a_n = request.POST['editANum']

            try:
                bts_info = request.POST['editBTS']
                print(bts_info)
                try:
                    if u_e == 'TM500':
                        tm_500 = request.POST['editTM500']
                        BTS_PC.objects.filter(ip=server_name).update(display_name=display_name, username=ussername, password=pass_word, domain=do_main, ue_type=u_e, switch_port=sport, notes=txta, rack=rack, serial_number=s_n, product_number=p_n, asset_number=a_n, tm500_pc_id=tm_500)
                    elif u_e == 'Test Terminal':
                        t_t = request.POST['editTT']
                        print("HELLOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
                        BTS_PC.objects.filter(ip=server_name).update(display_name=display_name, username=ussername, password=pass_word, domain=do_main, ue_type=u_e, switch_port=sport, notes=txta, rack=rack, serial_number=s_n, product_number=p_n, asset_number=a_n, bts_info_id=BTS_INFO.objects.get(bts_name=bts_info), tt_info_id=BTS_INFO.objects.get(bts_name=t_t))
                    messages.success(request, 'Successfully Updated')
                except IntegrityError as e:
                    messages.error(request, 'ERROR')
            except:
                try:
                    if u_e == 'TM500':
                        tm_500 = request.POST['editTM500']
                        BTS_PC.objects.filter(ip=server_name).update(display_name=display_name, username=ussername, password=pass_word, domain=do_main, ue_type=u_e, switch_port=sport, notes=txta, rack=rack, serial_number=s_n, product_number=p_n, asset_number=a_n, tm500_pc_id=tm_500)
                    elif u_e == 'Test Terminal':
                        t_t = request.POST['editTT']
                        BTS_PC.objects.filter(ip=server_name).update(display_name=display_name, username=ussername, password=pass_word, domain=do_main, ue_type=u_e, switch_port=sport, notes=txta, rack=rack, serial_number=s_n, product_number=p_n, asset_number=a_n, tt_info_id=BTS_INFO.objects.get(bts_name=t_t))
                    messages.success(request, 'Successfully Updated')
                except IntegrityError as e:
                    messages.error(request, 'ERROR')

        elif operation == "del-indiv-bts":
            dip = request.POST['deleteID']
            try:
                if BTS_PC.objects.filter(ip = dip).exists():
                    BTS_PC.objects.get(ip = dip).delete()
                messages.success(request, 'Successfully Deleted')
            except:
                  messages.error(request, 'Cannot Delete BTS PC')         

        elif operation == "delete-bts":
            server_list = request.POST.getlist('server_name')
            # print("LIST: ", len(server_list))
            if(len(server_list) < 1):
                messages.error(request, 'Nothing to Delete - Nothing Selected')
            else:
                try:
                    for ip in server_list:
                        print(ip)
                        if BTS_PC.objects.filter(ip = ip).exists():
                            BTS_PC.objects.get(ip = ip).delete()
                    messages.success(request, 'Successfully Deleted')
                except:
                    messages.error(request, 'Cannot Delete BTS PCs')

        ##############################################################
        ################### BTS INFO OPERATIONS ######################
        ##############################################################

        elif operation == "add-info":
            name = request.POST['nam_e']
            typ_e = request.POST['type']
            use = request.POST['use']
            rack = request.POST['rack']
            sport = request.POST['sport']
            txta = request.POST['txta']
            inmod = request.POST.getlist('inmod')

            #print(name, typ_e, use, rack, sport, txta)
            #arr = []
            #index = 0;
            '''for inf in getBTSINFO:
                #print(inf.i_d)
                curr = inf.i_d
                arr.append(curr)
            for i in range(len(arr)):
                # print("arr[i]+1: ", arr[i]+1)
                #print("arr[i+1]: ", arr[i+1])
                #print(i, len(arr))
                if i == len(arr)-1:
                    #print("equal")s
                    index = len(arr)+1
                    arr.append(len(arr)+1)
                    #print("up: ", index)
                    break;
                else:
                    if arr[i]+1 != arr[i+1]:
                        index = arr[i]+1
                        arr.append(arr[i]+1)
                        #print("down: ", index)
                        break
                #arr.sort()
                #print(arr)'''
            try:
                # print(index)
                newInfo = BTS_INFO(bts_name=name, bts_type=typ_e, bts_use=use, rack=rack, switch_port=sport, notes=txta)
                newInfo.save()
                print(inmod)
                for i in range(len(inmod)):
                    print("mod: ", inmod[i])
                    nmod = inmod[i]
                    #field_val = getattr(BTS_MODULES.objects.get(i_d=i), 'bts_name')
                    #print(field_val)     
                    print("module: ", BTS_MODULES.objects.get(i_d=nmod))    
                    print("info: ", BTS_INFO.objects.get(bts_name=name))       
                    BTS_MODULES.objects.filter(i_d=nmod).update(assign=1, bts_info_id=BTS_INFO.objects.get(bts_name=name))
                messages.success(request, 'Successfully Added')
            except:
                messages.error(request, 'Cannot Add BTS Info')

        elif operation == "update-info":
            server_name = request.POST['editID']
            name = request.POST['editName']
            typ_e = request.POST['editType']
            use = request.POST['editUse']
            rack = request.POST['editRack']
            sport = request.POST['editSPort']
            txta = request.POST['editNotes']
            inmod = request.POST.getlist('editMod')

            try:
                # newInfo = BTS_INFO(i_d=index, bts_name=name, bts_type=typ_e, bts_use=use, rack=rack, switch_port=sport, notes=txta)
                #BTS_INFO.objects.filter(i_d=server_name).update(bts_name=name, bts_type=typ_e, bts_use=use, rack=rack, switch_port=sport, notes=txta)
                counter = 0
                i = 0
                ii = len(inmod)
                while True:
                    print(i, ii)
                    if i != ii:
                        print("not equal")
                        for mm in getBTSMOD:
                            print("mod: ", inmod[i])
                            nmod = inmod[i]
                            if mm.i_d == nmod:
                                if mm.assign == '0':
                                    print("direct save")
                                else:
                                    counter = counter + 1
                                    print("counter: ", counter)
                    else:
                        print("GRRRRRRRRRRRRRRRRRRR")
                        break
                    i = i + 1
                '''for i in range(len(inmod)):
                    print(i, len(inmod))
                    print("mod: ", inmod[i])
                    # print(len(inmod))
                    nmod = inmod[i]
                    if i == len(inmod):
                        listMod = BTS_MODULES.objects.get(bts_info_id=BTS_INFO.objects.get(bts_name=name))
                        print(listMod)
                    else:
                        for mm in getBTSMOD:
                            #print(mm)
                            if mm.i_d == nmod:
                                if mm.assign == '0':
                                    print("direct save")
                                    break
                                elif mm.assign == '1':
                                    counter = counter + 1
                                    break'''


                messages.success(request, 'Successfully Updated')
            except:
                messages.error(request, 'ERROR')
        
        elif operation == "del-indiv-info":
            dip = request.POST['deleteID']
            print(dip)
            try:
                if BTS_INFO.objects.filter(i_d = dip).exists():
                    BTS_INFO.objects.get(i_d = dip).delete()
                messages.success(request, 'Successfully Deleted')
            except:
                messages.error(request, 'Cannot Delete BTS Info')

        elif operation == "delete-info":
            server_list = request.POST.getlist('server_name')
            if(len(server_list) < 1):
                messages.error(request, 'Nothing to Delete - Nothing Selected')
            else:
                try:
                    for ip in server_list:
                        print(ip)
                        if BTS_INFO.objects.filter(i_d = ip).exists():
                            print("delete?")
                            BTS_INFO.objects.get(i_d = ip).delete()
                    messages.success(request, 'Successfully Deleted')
                except:
                    messages.error(request, 'Cannot Delete BTS Info')

        ##############################################################
        ################### BTS MOD OPERATIONS ######################
        ##############################################################

        elif operation == "add-mod":
            # print("oki doki")
            name = request.POST['nam_e']
            b_rand = request.POST['b_rand']
            s_n = request.POST['s_n']
            p_n = request.POST['p_n']
            a_n = request.POST['a_n']
            txta = request.POST['txta']

            #print(name, b_rand, ayd, s_n, p_n, a_n, txta)
            try:
                try:
                    ayd = request.POST['ayd']
                    # print(BTS_INFO.objects.get(i_d=ayd))
                    newMod = BTS_MODULES(module_name=name, module_brand=b_rand, bts_info_id=BTS_INFO.objects.get(i_d=ayd), serial_number=s_n, product_number=p_n, asset_number=a_n, notes=txta, assign=1)
                    newMod.save()
                    messages.success(request, 'Successfully Added')
                except:
                    newMod = BTS_MODULES(module_name=name, module_brand=b_rand, serial_number=s_n, product_number=p_n, asset_number=a_n, notes=txta, assign=0)
                    newMod.save()
                    messages.success(request, 'Successfully Added')
            except:
                messages.error(request, 'ERROR')

        elif operation == "update-mod":
            # print("oki doki")
            i_d = request.POST['editID']
            name = request.POST['editName']
            b_rand = request.POST['editBrand']
            s_n = request.POST['editSNum']
            p_n = request.POST['editPNum']
            a_n = request.POST['editANum']
            txta = request.POST['editNotes']

            try:
                try:
                    ayd = request.POST['editBITIN']
                    print(ayd)
                    BTS_MODULES.objects.filter(i_d=i_d).update(module_name=name, module_brand=b_rand, bts_info_id=BTS_INFO.objects.get(bts_name=ayd), serial_number=s_n, product_number=p_n, asset_number=a_n, notes=txta, assign=1)
                    #newMod.save()
                    messages.success(request, 'Successfully Updated')
                except:
                    #messages.error(request, 'ERROR')
                    BTS_MODULES.objects.filter(i_d=i_d).update(module_name=name, module_brand=b_rand, serial_number=s_n, product_number=p_n, asset_number=a_n, notes=txta, assign=0)
                    newMod.save()
                    messages.success(request, 'Successfully Added')
            except:
                messages.error(request, 'ERROR')

        elif operation == "del-indiv-mod":
            dip = request.POST['deleteID']
            print(dip)
            try:
                if BTS_MODULES.objects.filter(i_d = dip).exists():
                    #BTS_MODULES.objects.get(i_d = dip).delete()
                    field_val = getattr(BTS_MODULES.objects.get(i_d=dip), 'assign')
                    print(field_val)
                    if field_val == "0":
                        BTS_MODULES.objects.get(i_d = dip).delete()
                        messages.success(request, 'Successfully Deleted')
                    else:
                        messages.error(request, 'Cannot Delete BTS Module', extra_tags='error_delete_module')
            except:
                messages.error(request, 'Cannot Delete BTS Module')
        
        elif operation == "delete-mod":
            server_list = request.POST.getlist('server_name')
            if(len(server_list) < 1):
                messages.error(request, 'Nothing to Delete - Nothing Selected')
            else:
                try: 
                    for ip in server_list:
                        print(ip)
                        if BTS_MODULES.objects.filter(i_d = ip).exists():
                            print("delete?")
                            BTS_MODULES.objects.get(i_d = ip).delete()
                    messages.success(request, 'Successfully Deleted')
                except:
                    messages.error(request, 'Cannot Delete BTS Module')

        ##############################################################
        ################### FETCH DETAILS ############################
        ##############################################################

        elif operation == "bts_fetch":
            bts_pc = request.POST['bts_server']
            bts_un = request.POST['bts_username']
            bts_ps = request.POST['bts_password']
            bts_inputC = "net use Z: \\\\" + bts_pc + "\\C$ /user:" + bts_un + " " + bts_ps
            bts_inputD = "net use G: \\\\" + bts_pc + "\\D$ /user:" + bts_un + " " + bts_ps
            btsPC.objects.filter(serverName = bts_pc).update(fetch = 1)
            try:
                s = subprocess.call(bts_inputC, shell=True)
                s = subprocess.call(bts_inputD, shell=True)
                if(s == 0):
                    print("success - mount")
                elif(s == 2):
                    print("already mounted")
                try:
                    toolVersions = ""
                    f = open("Z:\\Pegasus\\workspaceWCDMA_Pilot\\workspaceWCDMA_Pilot.txt", "r")
                    contents = f.read()
                    rev1 = contents.split(': ')
                    toolVersions = toolVersions + "workspaceWCDMA_Pilot: " + rev1[1]
                    # print(toolVersions)
                    f = open("G:\\CI\\CI_TOOL\\DSPExplorer\\DSPExplorer.txt", "r")
                    contents = f.read()
                    rev2 = contents.split(': ')
                    toolVersions = toolVersions + "DSPExplorer: " + rev2[1]
                    # print(toolVersions)
                    f = open("G:\\CI\\CI_TOOL\\GTA_Plugin_Giant\\GTA_Plugin_Giant.txt", "r")
                    contents = f.read()
                    rev3 = contents.split(': ')
                    toolVersions = toolVersions + "GTA_Plugin_Giant: " + rev3[1]
                    print(toolVersions)
                    bts_info = btsPCInfo(serverName=btsPC.objects.get(serverName=bts_pc), tool_version = toolVersions)

                    bts_info.save()
                    #subprocess.call('net use Z: /del /y', shell=True)
                    #print("success - unmount")
                except:
                    print("fail - unmount")
                #subprocess.call('net use Z: /del /y', shell=True)
            except:
                print("fail - mount")
            # print(bts_pc)
    context = {
        "getUE" : getUE,
        "getBTSPC" : getBTSPC,
        "getTMPC" : getTMPC,
        "getBTSINFO" : getBTSINFO,
        "getBTSMOD" : getBTSMOD,
    }
    return render(request, 'index.html', context)

def bts(request):
    getBTS = btsList.objects.all()

    '''if request.method == "POST":
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
                btsList.objects.get(bts = ip).delete()'''
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

def racks(request):
    #return render(request, 'racks.html')
    getRacks = racksInfo.objects.all()
    print("hello")
    if request.method == 'POST': 
        print("world")
        image_data = request.POST['grr']
        print(image_data)
        newRack = racksInfo(rack_id='a1', rack_url=image_data)
        newRack.save()

    context = {
        "getRacks" : getRacks,
    }
    return render(request, 'racks.html', context)