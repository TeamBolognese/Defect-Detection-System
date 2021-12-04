#!/usr/bin/python
'''
Bottle app
'''
from bottle import default_app, route, response, get, post, request, static_file
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
    response.set_header('Access-Control-Allow-Origin', '*')
    return '''
<!DOCTYPE html>
<html lang="ru">
<head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,
      initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" type="text/css" href="style.css">
<title>Project</title>
</head>
<body>
<h2>Навигация</h2>
<h3>API endpoints:</h3>
<p>- <b><a href="/detect">/detect</a></b> - Форма загрузки фрагмента изображения для определения факта наличия брака<br></p>
<p>- <b>/api/detect</b> - API загрузки<br></p>
<p>- <b><a href="/detail">/detail</a></b> - Форма загрузки фрагмента изображения для полного анализа<br></p>
<p>- <b>/api/detail</b> - API загрузки<br><br></p>
<p><h3>Video record:</h3></p>
<video muted></video>
<button type="button" onclick="go()">&#9210;</button>
<script src="main.js"></script>
</p>
</body>
</html>'''

@route('/style.css')
def show_stylecss():
    response.set_header('Access-Control-Allow-Origin', '*')
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
    response.set_header('Access-Control-Allow-Origin', '*')
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

@route('/detail')
def detail_form():
    response.add_header('Access-Control-Allow-Origin','*')
    return '''
<form action="/api/detail" method="post" enctype="multipart/form-data">
  Select image to upload:
  <input type="file" name="img" id="img">
  <input type="submit" value="Upload Image" name="submit">
</form>
'''

@route('/api/detail',method='POST')
def do_detail():
    response.add_header('Access-Control-Allow-Origin','*')
    i = "photo" + str(randint(0,2**30))
    postdata = request.body.read()
    f = open(i+".png", "wb")
    f.write(postdata)
    f.close()
    system("sudo python3 ii.py " + i + ".png")
    return "<img src=\"/res.png\">"

@route('/<picture>')
def serve_pictures(picture):
    return static_file(picture, root='')

@route('/detect')
def detect_form():
    response.set_header('Access-Control-Allow-Origin', '*')
    return '''
<form action="/api/detect" method="post" enctype="multipart/form-data">
  Select image to upload:
  <input type="file" name="img" id="img">
  <input type="submit" value="Upload Image" name="submit">
</form>
'''

@route('/api/detect', method='POST')
def do_detect():
    response.set_header('Access-Control-Allow-Origin', '*')
    i = "photo" + str(randint(0,2**30))
    postdata = request.body.read()
    i = str(randint(0,2**31)) # filename
    f = open(i+".png", "wb")
    f.write(postdata)
    f.close()
    system("python3 getter.py " + i + ".png > " + i + ".png.txt")
    blacks = int(popen("grep -o -E \"[0-3][0-9], [0-3][0-9], [0-3][0-9]\" " + i + ".png.txt | wc -l").read()) # dark RGB
    all = int(popen("grep -o -E \")\" " + i + ".png.txt | wc -l").read()) # all RGB

    percent = ((blacks/all) * 100) # % dark

    if (percent > 2): # model. ~0.2% - one black point
        print("With defects" + str(percent))
        return "{\"Status\": \"bad\", \"percent\": " + str(percent) + "}"
    else:
        print("Without defects" + str(percent))
        return "{\"Status\": \"good\", \"percent\": " + str(percent) + "}"

@route('/api/video/<data>') # TODO: add accesstoken
def get_video(data):
    response.add_header('Access-Control-Allow-Origin', '*')
    res = cursor.execute("SELECT * FROM videos WHERE date like '" + str(data) + "%';").fetchall()
    return dumps(res)

@route('/', method='POST') # Security-TODO: поменять на /<secrets> и раскомментить if
def do_write(): # добавить secrets в скобки
    #if(secrets == "026895beb22104b949a1dcb057a3a5f27d1571037ca19549d0dc5218d3725c0f"):
    response.add_header('Access-Control-Allow-Origin', '*')
    postdata = request.body.read()
    i = str(randint(0,2**31)) # filename
    f = open(i+".webm", "wb")
    f.write(postdata)
    f.close()
    system("ffmpeg -i " + i + ".webm -ss 00:00:00.005 -frames:v 1 " + i + ".png") # save first second in filename.png
    system("python3 getter.py " + i + ".png > " + i + ".png.txt") # get and save RGBs in filename.png.txt

    blacks = int(popen("grep -o -E \"[0-3][0-9], [0-3][0-9], [0-3][0-9]\" " + i + ".png.txt | wc -l").read()) # dark RGB
    all = int(popen("grep -o -E \")\" " + i + ".png.txt | wc -l").read()) # all RGB
    print("\nBlacks: " + str(blacks))
    print("\nAll: " + str(all) + "\n")

    percent = ((blacks/all) * 100)

    insert_values = (i, percent, "neftgaz", "000"+i) # Examples fields

    if (percent > 1.8): # model. 1% is ~1-5% defects
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
