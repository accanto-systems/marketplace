#!/usr/bin/env bash
direction="$1"
env="$2"

echo "$direction" 
echo "$env"

cd ./aggregation-epc-location;lmctl project $direction $env; cd ..
cd ./core-epc-location;lmctl project $direction $env; cd ..
cd ./enb-vnf;lmctl project $direction $env; cd ..
cd ./epc;lmctl project $direction $env; cd ..
cd ./epc-ns;lmctl project $direction $env; cd ..
cd ./epc-ns-extended;lmctl project $direction $env; cd ..
cd ./logical-network;lmctl project $direction $env; cd ..
cd ./add-cork-to-epc;lmctl project $direction $env; cd ..
cd ./cutover;lmctl project $direction $env; cd ..
cd ./rm-dublin-ns;lmctl project $direction $env; cd ..


