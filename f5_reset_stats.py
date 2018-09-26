"""
Created on Tue Sep 25 23:07:39 2018

@author: Lanclin
"""

from f5.bigip import ManagementRoot

def cgn_stats_reset(mgm_ip, user, pw):

    # Connect to the BigIP
    big = ManagementRoot(mgm_ip, gtac_user, gtac_pw)

    # Sys Hostname
    hostname = big.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show cm device | grep Hostname | awk \'{ printf($2) }\'"')
    host = hostname.commandResult

    print('Reset Performing on', host)
    # reset all net stats 
    big.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show sys clock; tmsh reset-stats net interface"')
    # reset all performance stats 
    big.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show sys clock; tmsh reset-stats sys performance all-stats"')
    # Reset all ltm virtual
    big.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show sys clock; tmsh reset-stats ltm virtual"')
    # Reset all ltm pool
    big.tm.util.bash.exec_cmd('run', utilCmdArgs='-c "tmsh show sys clock; tmsh reset-stats ltm pool"')
    
#mgm = 'x.x.x.x'
user = 'username'
pword = 'password'

#cgn_stats_reset(mgm, user, pword)

mgm_l = ['x.x.x.x','y.y.y.y']
num_cgn = len(mgm_l)
for i in range(0,num_cgn,1):
    print("Instance ==>",mgm_l[i])
    print('='*50)
    cgn_stats_reset(mgm_l[i], user, pword)
