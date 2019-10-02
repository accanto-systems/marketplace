cd vnfs/ip-pbx
lmctl project $1 $2
cd ../voip-gateway
lmctl project $1 $2
cd ../sip-performance
lmctl project $1 $2
cd ../../network-services/mgmt_infra
lmctl project $1 $2
cd ../voice-service
lmctl project $1 $2
cd ../voice-load-generator
lmctl project $1 $2
