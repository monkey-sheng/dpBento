# Variables
PORT="$1"
TOTAL_REQUESTS="$2"
THREADS="$3"

cd server
gcc -o server server.c
./server $PORT $TOTAL_REQUESTS $THREADS