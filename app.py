#!/usr/bin/python
'''
Bottle app
'''
from bottle import default_app, route, response, get, post, request, Response, static_file
import bottle
import sqlite3
from json import dumps
from random import randint
from os import system, popen

connect = sqlite3.connect("db.db")
cursor = connect.cursor()

@route('/')
def show_index():
    '''
    The front "index" page
    '''
    response.add_header('Access-Control-Allow-Origin', '*')
    return '''
<!DOCTYPE html>
<html lang="ru">
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,
      initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" type="text/css" href="style.css">
<title>Accenture final project | Bolognese</title>
</head>
<body>

<video muted></video>
<button type="button" onclick="go()">&#9210;</button>
<script src="main.js"></script>
</body>
</html>'''

@route('/style.css')
def show_stylecss():
    return '''html {
   height: 100%;}
body {
   height: 100%; margin: 0px; padding: 0px; background: black;
   text-align: center;}
video {
   display: block; max-height: 100%; max-width: 100%; margin: auto;}
button {
   display: inline-block; width: 2em; margin-left: -1em;
   position: absolute; bottom: 20px; left: 50%; background: none;
   outline: none; border: none; font-size: 30px;  text-align: center;}'''

@route('/main.js')
def show_mainjs():
    response.add_header('Access-Control-Allow-Origin', '*')
    return '''
"use strict";

const recTime = 15;

let pwd = location.search || 'a'; pwd = pwd.trim().replace('?', '');

const video = document.querySelector("video"),
      butt  = document.querySelector("button");

let media, playFlag = false;

const play = async () => {
   try {
      let c = /Android|iPhone/i.test(navigator.userAgent) ?
         {video:{facingMode:{exact:"environment"}}, audio:true} :
         {video:true, audio:true};

      let stream = await navigator.mediaDevices.getUserMedia(c);
      video.srcObject = stream;
      video.play();

      media = new MediaRecorder(stream);
      media.ondataavailable = d => {
         fetch("/", {
            method: "POST",
            headers: {"Content-Type": "video/webm", "X-PWD": pwd},
            body: d.data
         })
      };
      media.start(recTime * 1000);
   }
   catch(err) {alert(err);}
};

const go = () => {
   if (!playFlag) {
      butt.innerHTML = "&#9209;";
      play();
   }
   else {
      butt.innerHTML = "&#9210;";
      video.pause();
      video.srcObject = null;
      media.stop();
   }
   playFlag = !playFlag;
}
'''

@route('/api/video/<data>')
def get_video(data):
    res = cursor.execute("SELECT * FROM videos WHERE date like '" + str(data) + "%';").fetchall()
    return dumps(res)

@route('/', method='POST') # todo: поменять на /<secrets> и раскомментить if
def do_write(): # добавить secrets в скобки
    #if(secrets == "026895beb22104b949a1dcb057a3a5f27d1571037ca19549d0dc5218d3725c0f"):
    postdata = request.body.read()
    i = str(randint(0,2**31)) # filename
    f = open(i+".webm", "wb")
    f.write(postdata)
    f.close()
    system("ffmpeg -i " + i + ".webm -ss 00:00:00.005 -frames:v 1 " + i + ".png") # save first second in filename.png
    system("python3 getter.py " + i + ".png > " + i + ".png.txt") # get and save RGBs in filename.png.txt

    blacks = int(popen("grep -o -E \"[0-3][0-9], [0-3][0-9], [0-3][0-9]\" " + i + ".png.txt | wc -l").read()) # blacks count
    all = int(popen("grep -o -E \")\" " + i + ".png.txt | wc -l").read()) # all count
    print("\nBlacks: " + str(blacks))
    print("\nAll: " + str(all) + "\n")

    percent = ((blacks/all) * 100) # % blacks

    insert_values = (i, percent, "neftgaz", "000"+i)

    if (percent > 0.2): # model. 0.3 - one black point
        cursor.execute("INSERT INTO videos (name, percent, status, company, serial_id, date) VALUES (?, ?, 'bad', ?, ?, datetime('now'))", insert_values)
        connect.commit()
        print("With defects" + str(percent))
        return "With defects" + str(percent)
    else:
        cursor.execute("INSERT INTO videos (name, percent, status, company, serial_id, date) VALUES (?, ?, 'good', ?, ?, datetime('now'))", insert_values)
        connect.commit()
        print("Without defects" + str(percent))
        return "Without defects" + str(percent)


if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=80)
