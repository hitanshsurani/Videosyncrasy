# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FervIIpvmrTOXLf03WGz__VNyBptkTZU
"""

from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', img_list=img_list)

@app.route('/animate')
def animate():
    image = request.args.get('image')
    img_path = f'examples/source_image/{image}.png'
    cmd = f"python3.8 inference.py --driven_audio ./examples/driven_audio/RD_Radio31_000.wav --source_image {img_path} --result_dir ./results --still --preprocess full --enhancer gfpgan"
    subprocess.run(cmd, shell=True)
    mp4_name = glob.glob('./results/*.mp4')[0]
    return mp4_name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)