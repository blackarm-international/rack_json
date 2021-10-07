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
# open csv output
with open("racks.csv", "w") as csvFile:
    # titles
    print(',name, modelName, primaryBusinessServiceName, primaryBusinessServiceProduct, rackU, slot, cmdbNetworkSecurityZone, state, status, supportGroupName, supportGroupManager ,serviceGroupName, serviceGroupManager, assignmentGroupName, assignmentGroupManager, location, fqdn, hardwareSku, ipAddress, modelCategory, modelHeight, modelEndOfFirmwareSupportDate, modelMaxChildren, url', file = csvFile)
    # generate sorted racks
    for rack_sysid in rack_json.keys():
        rack_name = rack_json[rack_sysid]['rackName']
        rack_name_list.append(rack_name)
        rack_name_rack_sysid[rack_name] = rack_sysid
        rack_name_list.sort()
    # loop through racks
    for rack_name in rack_name_list:
        rack_sysid = rack_name_rack_sysid[rack_name]
        url = 'https://godaddy.service-now.com/nav_to.do?uri=%2Fcmdb_ci_rack.do%3Fsys_id%' + rack_sysid
        print('{0},,,,,,,,,,,,,,,,,,,,,,{1}'.format(rack_name, url), file = csvFile)
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
                cmdbNetworkSecurityZone = rack_mount['cmdbNetworkSecurityZone']
                fqdn = rack_mount['fqdn']
                hardwareSku = rack_mount['hardwareSku']
                ipAddress = rack_mount['ipAddress']
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
                slot = ""
                state = rack_mount['state']
                status = rack_mount['status']
                supportGroupName = rack_mount['supportGroupName']
                supportGroupManager = rack_mount['supportGroupManager']
                url = rack_mount['url']
                print('  - unit_{}'.format(rack_mounted_u), end ="", file = csvFile)
                print(',{}'.format(name), end ="", file = csvFile)
                print(',{}'.format(modelName), end ="", file = csvFile)
                print(',{}'.format(primaryBusinessServiceName), end ="", file = csvFile)
                print(',{}'.format(primaryBusinessServiceProduct), end ="", file = csvFile)
                print(',{}'.format(rackU), end ="", file = csvFile)
                print(',{}'.format(slot), end ="", file = csvFile)
                print(',{}'.format(cmdbNetworkSecurityZone), end ="", file = csvFile)
                print(',{}'.format(state), end ="", file = csvFile)
                print(',{}'.format(status), end ="", file = csvFile)
                print(',{}'.format(supportGroupName), end ="", file = csvFile)
                print(',{}'.format(supportGroupManager), end ="", file = csvFile)
                print(',{}'.format(serviceGroupName), end ="", file = csvFile)
                print(',{}'.format(serviceGroupManager), end ="", file = csvFile)
                print(',{}'.format(assignmentGroupName), end ="", file = csvFile)
                print(',{}'.format(assignmentGroupManager), end ="", file = csvFile)
                print(',{}'.format(location), end ="", file = csvFile)
                print(',{}'.format(fqdn), end ="", file = csvFile)
                print(',{}'.format(hardwareSku), end ="", file = csvFile)
                print(',{}'.format(ipAddress), end ="", file = csvFile)
                print(',{}'.format(modelCategory), end ="", file = csvFile)
                print(',{}'.format(modelHeight), end ="", file = csvFile)
                print(',{}'.format(modelEndOfFirmwareSupportDate), end ="", file = csvFile)
                print(',{}'.format(modelMaxChildren), end ="", file = csvFile)
                print(',{}'.format(url), file = csvFile)
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
                        cmdbNetworkSecurityZone = sled['cmdbNetworkSecurityZone']
                        fqdn = sled['fqdn']
                        hardwareSku = sled['hardwareSku']
                        ipAddress = sled['ipAddress']
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
                        print('      - slot_{0}'.format(sled_slot), end ="", file = csvFile)
                        print(',{}'.format(name), end ="", file = csvFile)
                        print(',{}'.format(modelName), end ="", file = csvFile)
                        print(',{}'.format(primaryBusinessServiceName), end ="", file = csvFile)
                        print(',{}'.format(primaryBusinessServiceProduct), end ="", file = csvFile)
                        print(',{}'.format(rackU), end ="", file = csvFile)
                        print(',{}'.format(slot), end ="", file = csvFile)
                        print(',{}'.format(cmdbNetworkSecurityZone), end ="", file = csvFile)
                        print(',{}'.format(state), end ="", file = csvFile)
                        print(',{}'.format(status), end ="", file = csvFile)
                        print(',{}'.format(supportGroupName), end ="", file = csvFile)
                        print(',{}'.format(supportGroupManager), end ="", file = csvFile)
                        print(',{}'.format(serviceGroupName), end ="", file = csvFile)
                        print(',{}'.format(serviceGroupManager), end ="", file = csvFile)
                        print(',{}'.format(assignmentGroupName), end ="", file = csvFile)
                        print(',{}'.format(assignmentGroupManager), end ="", file = csvFile)
                        print(',{}'.format(location), end ="", file = csvFile)
                        print(',{}'.format(fqdn), end ="", file = csvFile)
                        print(',{}'.format(hardwareSku), end ="", file = csvFile)
                        print(',{}'.format(ipAddress), end ="", file = csvFile)
                        print(',{}'.format(modelCategory), end ="", file = csvFile)
                        print(',{}'.format(modelHeight), end ="", file = csvFile)
                        print(',{}'.format(modelEndOfFirmwareSupportDate), end ="", file = csvFile)
                        print(',{}'.format(modelMaxChildren), end ="", file = csvFile)
                        print(',{}'.format(url), file = csvFile)
