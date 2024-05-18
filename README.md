# Djangoで動かすChatGPTアプリ

DjangoとBootstrapで作られたChatGPTのアプリケーションです。
自分でAPIキーを入れることで動くので、OpenAIのキーを自分で発行する必要があります。

## Usage
1. [OpenAI](https://openai.com/) のサイトからAPIキーを発行
2. `OPENAI_API_KEY` という名前で環境変数に設定
3. `poetry install` で環境を構築（PoetryをPCに入れていない場合はそこから）
4. `poetry shell`　で仮想環境に入る
5. `cd openai_django`
5. `python manage.py runserver`で立ち上げる
6. `http://localhost:8000/`でアプリに入る

## TODO
- GPTのモデルを変更可能にする
- AWS EC2上にデプロイする
- 会話履歴を記憶させる
- 見た目をかっこよくする

## License
[MIT](https://choosealicense.com/licenses/mit/)
