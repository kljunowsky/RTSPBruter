# RTSPBruter 🔪 

RTSPBruter is python tool used to bruteforce authentification of Real Time Streaming Protocol (RTSP).

## Usage 🛠 

python3 -u usernames.txt -P passwords.txt -i 127.0.0.1 -p 554

## Running from Docker 🐳 

docker run -ti -v $(PWD)/data:/data rtspbruter -u data/usernames.txt -P data/passwords.txt -i 127.0.0.1 -p 554

## Parameters 🧰 

Parameter | Description | Type
------------ | ------------- | -------------
-i, --ip | Target IP address. | String
-p, --port | RTSP Port | String
-u, --usernames | Wordlist with usernames | File
-P, --passwords | Wordlist with passwords | File


#### License

This project is licensed under **MIT** license
