import json
# import rack json
try:
    with open("racks.json", "r") as config:
        rack_json = json.load(config)
except:
    print("unable to load racks.json")
    exit()
rack_name_list = []
rack_name_rack_sysid = {}
# titles
print(',assignment_group_name,assignment_group_manager,fqdn,hardware_sku,location,model_category,model_name,model_height,model_end_of_firmware_support_date,model_max_children,name,primary_business_service_name,primary_business_service_product,rack_u,service_group_name,service_group_manager,slot,state,status,support_group_name,support_group_manager,url')
# generate sorted racks
for rack_sysid in rack_json.keys():
    rack_name = rack_json[rack_sysid]['rackName']
    rack_name_list.append(rack_name)
    rack_name_rack_sysid[rack_name] = rack_sysid
# loop through racks
for rack_name in rack_name_list:
    rack_sysid = rack_name_rack_sysid[rack_name]
    url = 'https://godaddy.service-now.com/nav_to.do?uri=%2Fcmdb_ci_rack.do%3Fsys_id%' + rack_sysid
    print('{0},,,,,,,,,,,,,,,,,,,,,,{1}'.format(rack_name, url))
    if 'contains' in rack_json[rack_sysid]:
        rack_mounted_u_list = []
        rack_mounted_u_rack_mounted_sysid = {}
        # build sortable data structures
        for rack_mounted_sysid in rack_json[rack_sysid]['contains'].keys():
            rack_mounted = rack_json[rack_sysid]['contains'][rack_mounted_sysid]
            rack_mounted_rack_u = rack_mounted['rackU']
            rack_mounted_u_list.append(int(rack_mounted_rack_u))
            rack_mounted_u_rack_mounted_sysid[rack_mounted_rack_u] = rack_mounted_sysid
        # loop through mounted rack_mounteds in rack_u order
        rack_mounted_u_list.sort()
        rack_mounted_u_list = sorted(rack_mounted_u_list, reverse=True)
        for rack_mounted_u in rack_mounted_u_list:
            rack_mounted_sysid = rack_mounted_u_rack_mounted_sysid[str(rack_mounted_u)]
            # rack mounted object
            rack_mount = rack_json[rack_sysid]['contains'][rack_mounted_sysid]
            assignmentGroupName = rack_mount['assignmentGroupName']
            assignmentGroupManager = rack_mount['assignmentGroupManager']
            fqdn = rack_mount['fqdn']
            hardwareSku = rack_mount['hardwareSku']
            location = rack_mount['location']
            modelCategory = rack_mount['modelCategory']
            modelName = rack_mount['modelName']
            modelHeight = rack_mount['modelHeight']
            modelEndOfFirmwareSupportDate = rack_mount['modelEndOfFirmwareSupportDate']
            modelMaxChildren = rack_mount['modelMaxChildren']
            name = rack_mount['name']
            primaryBusinessServiceName = rack_mount['primaryBusinessServiceName']
            primaryBusinessServiceProduct = rack_mount['primaryBusinessServiceProduct']
            rackU = rack_mount['rackU']
            serviceGroupName = rack_mount['serviceGroupName']
            serviceGroupManager = rack_mount['serviceGroupManager']
            slot = rack_mount['slot']
            state = rack_mount['state']
            status = rack_mount['status']
            supportGroupName = rack_mount['supportGroupName']
            supportGroupManager = rack_mount['supportGroupManager']
            url = rack_mount['url']
            print('  - unit_{}'.format(rack_mounted_u), end ="")
            print(',{}'.format(assignmentGroupName), end ="")
            print(',{}'.format(assignmentGroupManager), end ="")
            print(',{}'.format(fqdn), end ="")
            print(',{}'.format(hardwareSku), end ="")
            print(',{}'.format(location), end ="")
            print(',{}'.format(modelCategory), end ="")
            print(',{}'.format(modelName), end ="")
            print(',{}'.format(modelHeight), end ="")
            print(',{}'.format(modelEndOfFirmwareSupportDate), end ="")
            print(',{}'.format(modelMaxChildren), end ="")
            print(',{}'.format(name), end ="")
            print(',{}'.format(primaryBusinessServiceName), end ="")
            print(',{}'.format(primaryBusinessServiceProduct), end ="")
            print(',{}'.format(rackU), end ="")
            print(',{}'.format(serviceGroupName), end ="")
            print(',{}'.format(serviceGroupManager), end ="")
            print(',{}'.format(slot), end ="")
            print(',{}'.format(state), end ="")
            print(',{}'.format(status), end ="")
            print(',{}'.format(supportGroupName), end ="")
            print(',{}'.format(supportGroupManager), end ="")
            print(',{}'.format(url))
            # check if sleds exist
            if 'contains' in rack_json[rack_sysid]['contains'][rack_mounted_sysid]:
                sled_slot_list = []
                sled_slot_sled_sysid = {}
                # build sortable data structures
                for sled_sysid in rack_json[rack_sysid]['contains'][rack_mounted_sysid]['contains'].keys():
                    sled = rack_json[rack_sysid]['contains'][rack_mounted_sysid]['contains'][sled_sysid]
                    sled_slot = sled['slot']
                    sled_slot_list.append(sled_slot)
                    sled_slot_sled_sysid[sled_slot] = sled_sysid
                # loop through sleds in slot order
                sled_slot_list.sort()
                for sled_slot in sled_slot_list:
                    sled_sysid = sled_slot_sled_sysid[sled_slot]
                    # sled 
                    sled = rack_json[rack_sysid]['contains'][rack_mounted_sysid]['contains'][sled_sysid]
                    assignmentGroupName = sled['assignmentGroupName']
                    assignmentGroupManager = sled['assignmentGroupManager']
                    fqdn = sled['fqdn']
                    hardwareSku = sled['hardwareSku']
                    location = sled['location']
                    modelCategory = sled['modelCategory']
                    modelName = sled['modelName']
                    modelHeight = sled['modelHeight']
                    modelEndOfFirmwareSupportDate = sled['modelEndOfFirmwareSupportDate']
                    modelMaxChildren = sled['modelMaxChildren']
                    name = sled['name']
                    primaryBusinessServiceName = sled['primaryBusinessServiceName']
                    primaryBusinessServiceProduct = sled['primaryBusinessServiceProduct']
                    rackU = sled['rackU']
                    serviceGroupName = sled['serviceGroupName']
                    serviceGroupManager = sled['serviceGroupManager']
                    slot = sled['slot']
                    state = sled['state']
                    status = sled['status']
                    supportGroupName = sled['supportGroupName']
                    supportGroupManager = sled['supportGroupManager']
                    url = sled['url']
                    print('      - slot_{0}'.format(sled_slot), end ="")
                    print(',{}'.format(assignmentGroupName), end ="")
                    print(',{}'.format(assignmentGroupManager), end ="")
                    print(',{}'.format(fqdn), end ="")
                    print(',{}'.format(hardwareSku), end ="")
                    print(',{}'.format(location), end ="")
                    print(',{}'.format(modelCategory), end ="")
                    print(',{}'.format(modelName), end ="")
                    print(',{}'.format(modelHeight), end ="")
                    print(',{}'.format(modelEndOfFirmwareSupportDate), end ="")
                    print(',{}'.format(modelMaxChildren), end ="")
                    print(',{}'.format(name), end ="")
                    print(',{}'.format(primaryBusinessServiceName), end ="")
                    print(',{}'.format(primaryBusinessServiceProduct), end ="")
                    print(',{}'.format(rackU), end ="")
                    print(',{}'.format(serviceGroupName), end ="")
                    print(',{}'.format(serviceGroupManager), end ="")
                    print(',{}'.format(slot), end ="")
                    print(',{}'.format(state), end ="")
                    print(',{}'.format(status), end ="")
                    print(',{}'.format(supportGroupName), end ="")
                    print(',{}'.format(supportGroupManager), end ="")
                    print(',{}'.format(url))
