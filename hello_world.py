from flask import Flask, render_template
import numpy as np
import pandas as pd
from os.path import join, relpath
from glob import glob

app = Flask(__name__) #Flaskクラスのインスタンスを生成

@app.route('/') #ルートURLにアクセスがあった場合に実行される関数を定義

def hello_world(): #hello_world関数を定義
    return '<p>Hello, World!<p>' #ブラウザに表示する文字列を返す

@app.route('/index')


#def index():
    #message = 'Hello, World!'
    #return render_template('index.html', message=message) #index.htmlにstring型変数を渡してレンダリング



#def index():
    #my_dict = {}
    #my_dict['name'] = 'Yuniro'
    #my_dict['age'] = 20
    #my_dict['univ'] = 'Chiba Institute of Technology'
    #return render_template('index.html', message=my_dict) #index.htmlに辞書型の変数を渡してレンダリング 


#def index():
    #num_list = np.arange(10)
    #to_num_list = num_list.tolist() #numpy配列をリスト配列に変換しないとエラーが出る
    #return render_template('index.html', message=to_num_list) #index.htmlにリスト配列を渡してレンダリング

def index():
    path = './static'
    image_names = [relpath(x, path) for x in glob(join(path, '*.jpg'))]
    # static内の.pngファイルがimage_namesに格納されます。
    my_list = []
    for image in image_names:
        my_dic = {}
        my_dic['image_name'] = 'static/' + image
        my_dic['link_url'] = 'https://github.com/Yujiro-13/Flask_hello_world/assets/114651033/208d4f48-fa54-460c-9938-bdc188b5d2ef'
        # 飛び先のURLを何個も確保できなかったのでどの画像に対しても同じURLに飛ぶようにしました。
        my_list.append(my_dic)
    return render_template('index.html', message = my_list) #/indexにアクセスが来たらtemplates内のindex.htmlが開きます

if __name__ == '__main__': #このスクリプトが直接実行された場合にのみ、以下のコードが実行される
    app.run(host="0.0.0.0", port=8000, debug=True) #Flaskアプリケーションを起動