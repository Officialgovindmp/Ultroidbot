paci() {
sudo hostname rootedcyber
neofetch
git clone https://github.com/rooted-cyber/install-package
cp ins*pac*/pl*/* plug*
cp -f ins*pac*/config* ~/.conf*/neofet*
}
insp() {
paci
for a in speedtest-cli coloredlogs google_trans_new https://github.com/New-dev0/Telethon/archive/platy.zip python-decouple python-dotenv akinator apscheduler aiohttp bs4 enhancer git+https://github.com/New-dev0/instagrapi.git@39df1b1#egg=instagrapi git+https://github.com/buddhhu/img2html.git@c44170d#egg=img2html heroku3 gitpython google-api-python-client htmlwebshot lottie lxml numpy oauth2client opencv-python-headless pillow profanitydetector psutil pypdf2 pytz qrcode requests tabulate git+https://github.com/xditya/telegraph.git@41fd800#egg=telegraphq tgcrypto youtube-search-python yt-dlp;do
printf "installing $a\n"
pip3 install -U $a
done
}
fix() {
apt install --fix-broken -y || sudo apt install --fix-broken -y
}
ap() {
apt update -y || sudo apt update -y
apt upgrade -y || sudo apt upgrade -y
}
adde() {
touch .env
sudo touch .env
cat >> .env << EOF
REDIS_URI=
REDIS_PASSWORD=
SESSION=

EOF
}
inp() {
cd Ultroid
ap
fix
apt install python3-pip python3 -y || sudo apt install python3-pip python3 -y
fix
apt install ffmpeg neofetch mediainfo -y || sudo apt install ffmpeg neofetch mediainfo -y
fix
pip install --upgrade pip
pip3 install -r req*
pip3 install -r res*/sta*/opt*
pip3 install -U yt-dlp
sh -c "$(curl -fsSl https://raw.githubusercontent.com/rooted-cyber/Termux-Ultroid/main/install-pytgcalls.sh)"
}
dep() {
ap
fix
apt install git curl -y
sudo apt install curl git -y
sh -c "$(curl -fsSl https://raw.githubusercontent.com/rooted-cyber/uploading/main/deb/os-deb/sudo.sh)"
git clone https://github.com/TeamUltroid/Ultroid
cd Ultroid
inp
adde
}
dep > /dev/null 2>&1
cd Ultroid
insp
bash startup
sudo bash startup
