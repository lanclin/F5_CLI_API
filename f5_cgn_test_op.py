from f5.bigip import ManagementRoot

def cgn_test_op(mgm_ip, user, pw):

    # Connect to the BigIP
    big = ManagementRoot(mgm_ip, gtac_user, gtac_pw)

    # Sys Hostname
    hostname = big.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show cm device | grep Hostname | awk \'{ printf($2) }\'"')
    host = hostname.commandResult

    # Get the Vlan details 
    vl = big.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show sys clock; tmsh list net vlan /CGNAT/*"')
    print (host,"#tmsh list net vlan /CGNAT/*")
    net_vlan = vl.commandResult
    print (net_vlan)


    # Sys Performance Details
    sp = big.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show sys clock; tmsh show sys performance throughput; tmsh show sys performance connections"')
    print (host,"#tmsh show sys clock; tmsh show sys performance throughput; tmsh show sys performance connections")
    perf_conn = sp.commandResult
    print (perf_conn)


    # net Interface Raw Details
    ni = big.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show sys clock; tmsh show net interface raw"')
    print (host,"#tmsh show sys clock; tmsh show net interface raw")
    net_int = ni.commandResult
    print (net_int)
    
    # BGP summary details
    bgp = big.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show sys clock; imish -r 1 -e \'show ip bgp summary\'"')
    print (host,"#tmsh show sys clock; imish -r 1 -e 'show ip bgp summary'")
    bgp_sum = bgp.commandResult
    print (bgp_sum)
      
#mgm = 'x.x.x.x'
user = 'username'
pass = 'password'

#cgn_test_op(mgm, user, pass)

mgm_l = ['x.x.x.x','y.y.y.y']
num_cgn = len(mgm_l)
for i in range(0,num_cgn,1):
    print('='*50)
    print("Instance ==>",mgm_l[i])
    print('='*50)
    cgn_test_op(mgm_l[i], user, pass)
