#!/usr/bin/env bash

HUB=10.220.217.82
GIT_CREDENTIALS=jjh:jjh
LOCAL_GIT_DIR=/mnt/c/Users/hardw/git/hubdemo/voice-service

TOKEN=TG1DbGllbnQ6cGFzczEyMw==
CLIENT_ID=LmClient
CLIENT_PASSWORD=pass123
NEXUS_URL="http://${HUB}:8002/repository/raw/packages"
NEXUS_CREDENTIALS="admin:admin123"
GOGS_HOST="${HUB}:8001"


function get_bearer(){
	r=$( curl -X POST -k \
		-H "Content-Type: application/x-www-form-urlencoded" \
		-H "authorization:Basic ${TOKEN}" \
		-d  'grant_type=client_credentials' \
		"https://${HUB}:8081/oauth/token")

	bearer=$( echo "$r" | cut -d':' -f 2 | cut -d'"' -f 2 )
}

function delete_descriptor(){
	assembly=$1
 	curl -k  -X DELETE  \
		-H "Authorization: Bearer ${bearer}"\
 		"https://${HUB}:8080/api/catalog/descriptors/${assembly}"
}

function delete_package(){
	curl -X DELETE -v -u ${NEXUS_CREDENTIALS} \
		${NEXUS_URL}/voice-service/voice-service-1.0.tgz	
}

function delete_git_tag(){
	stash=$PWD
	cd $LOCAL_GIT_DIR
	git push http://${GIT_CREDENTIALS}@${GOGS_HOST}/marketplace/voice-service --delete 1.0
	cd $stash
}

echo "retrieving bearer token..."
get_bearer

echo "deleting demo descriptors..."

delete_descriptor "assembly::base::0.1"
delete_descriptor "assembly::network::1.0"
delete_descriptor "assembly::ip-pbx::1.0"
delete_descriptor "assembly::sip-performance::1.0"
delete_descriptor "assembly::baseinfrastructure::0.1"
delete_descriptor "assembly::voip-gateway::1.0"
delete_descriptor "assembly::voice-service::1.0"

echo "delete voice-service package from nexus..."
delete_package

echo "delete version tag from GIT"
delete_git_tag


