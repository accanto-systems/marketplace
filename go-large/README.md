go-large

1. use ALM version 2.0.3-207 edit your <allinone_install_dir>/ansible/variables.yml (or copy from ./alm-config/varaible.yml)
1. edit <allinone_install_dir>/ansible/lm-helm-values.yml to avoid timeouts during demo ( or copy from ./alm-config/lm-helm-values.yml, the changes are in the configurator: section)
1. set up lmctl LMCONFIG  (my env is called local), if you want to 'pull' then you'll need the latest from master on (http://10.220.216.162/stratoss-lm/lmctl)
1. run ./golarge.sh push local   (use pull to get the project back if you change anything)
1. open design for epc-ns 1.0
1. goto behaviour tests and run 'create networks'
1. then run 'activate epc network service'
1. To move the aggregation location for enb1 and enb2 run the behavior scenarion 'move aggregation location'. Upgrades 1.0 -> 1.0.1 (add Cork) -> 1.0.2 (cutover) ->1.0.3 (tear down Dublin). You will be prompted for an instance name its: 'epc-ns'
1. To add a new enb to London upgrade to assembly::epc-ns::1.1 through the UI (from any of the previous versions 1.x)