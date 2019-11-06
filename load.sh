cd vnfs/tenant-neutron-network
lmctl project $1 $2
cd ../provider-neutron-network
lmctl project $1 $2
cd ../baseinfrastructure
lmctl project $1 $2
cd ../hello-world
lmctl project $1 $2
cd ../ip-pbx
lmctl project $1 $2
cd ../voip-gateway
lmctl project $1 $2
cd ../sip-performance
lmctl project $1 $2

cd ../../network-services/jumphost-base
lmctl project $1 $2
cd ../jumphost-voice-service
lmctl project $1 $2
cd ../jumphost-voice-load-generator
lmctl project $1 $2

cd ../provider-base
lmctl project $1 $2
cd ../provider-voice-service
lmctl project $1 $2
cd ../provider-voice-load-generator
lmctl project $1 $2
