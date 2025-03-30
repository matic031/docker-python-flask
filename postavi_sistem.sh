NETWORK_NAME=slika_net
CLIENT_NAME=odjemalec
SERVER_NAME=streznik

docker rm -f $SERVER_NAME 2>/dev/null
docker rm -f $CLIENT_NAME 2>/dev/null
docker network rm $NETWORK_NAME 2>/dev/null

docker network create $NETWORK_NAME

docker build ./server -t slika_server
docker build ./client -t slika_client

docker run -dit --name $SERVER_NAME --network $NETWORK_NAME slika_server
docker run -dit --name $CLIENT_NAME --network $NETWORK_NAME -p 5001:5001 slika_client

CLIENT_IP=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CLIENT_NAME)

echo "Client IP: $CLIENT_IP"
echo "Visit http://localhost:5001 in your browser"
