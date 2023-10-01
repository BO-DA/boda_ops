rm -rf boda-ai-git

git clone https://github.com/BO-DA/boda_AI boda-ai-git

docker compose up --build -d

docker exec -it boda-ai-server /bin/bash /home/boda/boda-ai-server.sh
