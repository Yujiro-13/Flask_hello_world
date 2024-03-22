from flask import Flask
app = Flask(__name__) #Flaskクラスのインスタンスを生成

@app.route('/') #ルートURLにアクセスがあった場合に実行される関数を定義

def hello_world(): #hello_world関数を定義
    return '<p>Hello, World!<p>' #ブラウザに表示する文字列を返す

if __name__ == '__main__': #このスクリプトが直接実行された場合にのみ、以下のコードが実行される
    app.run(host="0.0.0.0", port=8000, debug=True) #Flaskアプリケーションを起動