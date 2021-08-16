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
print(', name, ciAssignmentGroup, ciCmdbStatus, ciIpAddress, ciNetworkSecurityZone, ciPrimaryBusinessService, ciServiceGroup, ciStatus, supportGroupEmail, supportGroupManager, supportGroupSlackChannel, url')
# generate sorted racks
for rack_sysid in rack_json.keys():
    rack_name = rack_json[rack_sysid]['rackName']
    rack_name_list.append(rack_name)
    rack_name_rack_sysid[rack_name] = rack_sysid
# loop through racks
for rack_name in rack_name_list:
    rack_sysid = rack_name_rack_sysid[rack_name]
    url = 'https://godaddy.service-now.com/nav_to.do?uri=%2Fcmdb_ci_rack.do%3Fsys_id%' + rack_sysid
    print('{0},,,,,,,,,,,,{1}'.format(rack_name, url))
    if 'contains' in rack_json[rack_sysid]:
        rack_mounted_u_list = []
        rack_mounted_u_rack_mounted_sysid = {}
        # build sortable data structures
        for rack_mounted_sysid in rack_json[rack_sysid]['contains'].keys():
            rack_mounted = rack_json[rack_sysid]['contains'][rack_mounted_sysid]
            rack_mounted_rack_u = rack_mounted['rackU']
            rack_mounted_u_list.append(rack_mounted_rack_u)
            rack_mounted_u_rack_mounted_sysid[rack_mounted_rack_u] = rack_mounted_sysid
        # loop through mounted rack_mounteds in rack_u order
        rack_mounted_u_list.sort()
        rack_mounted_u_list.reverse()
        for rack_mounted_u in rack_mounted_u_list:
            rack_mounted_sysid = rack_mounted_u_rack_mounted_sysid[rack_mounted_u]
            # rack mounted object
            rack_mount = rack_json[rack_sysid]['contains'][rack_mounted_sysid]
            name = rack_mount['name']
            ciAssignmentGroup = rack_mount['ciAssignmentGroup']
            ciCmdbStatus = rack_mount['ciCmdbStatus']
            ciIpAddress = rack_mount['ciIpAddress']
            ciNetworkSecurityZone = rack_mount['ciNetworkSecurityZone']
            ciPrimaryBusinessService = rack_mount['ciPrimaryBusinessService']
            ciServiceGroup = rack_mount['ciServiceGroup']
            ciStatus = rack_mount['ciStatus']
            supportGroupEmail = rack_mount['supportGroupEmail']
            supportGroupManager = rack_mount['supportGroupManager']
            supportGroupSlackChannel = rack_mount['supportGroupSlackChannel']
            url = 'https://godaddy.service-now.com/nav_to.do?uri=%2Falm_hardware.do%3Fsys_id%' + rack_mounted_sysid
            print('  - unit_{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}'.format(rack_mounted_u, name, ciAssignmentGroup, ciCmdbStatus, ciIpAddress, ciNetworkSecurityZone, ciPrimaryBusinessService, ciServiceGroup, ciStatus, supportGroupEmail, supportGroupManager, supportGroupSlackChannel, url))
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
                    name = sled['name']
                    ciAssignmentGroup = sled['ciAssignmentGroup']
                    ciCmdbStatus = sled['ciCmdbStatus']
                    ciIpAddress = sled['ciIpAddress']
                    ciNetworkSecurityZone = sled['ciNetworkSecurityZone']
                    ciPrimaryBusinessService = sled['ciPrimaryBusinessService']
                    ciServiceGroup = sled['ciServiceGroup']
                    ciStatus = sled['ciStatus']
                    supportGroupEmail = sled['supportGroupEmail']
                    supportGroupManager = sled['supportGroupManager']
                    supportGroupSlackChannel = sled['supportGroupSlackChannel']
                    url = 'https://godaddy.service-now.com/nav_to.do?uri=%2Falm_hardware.do%3Fsys_id%' + sled_sysid
                    print('      - slot_{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}'.format(sled_slot, name, ciAssignmentGroup, ciCmdbStatus, ciIpAddress, ciNetworkSecurityZone, ciPrimaryBusinessService, ciServiceGroup, ciStatus, supportGroupEmail, supportGroupManager, supportGroupSlackChannel, url))
