from dotenv import load_dotenv
from os.path import join, dirname

load_dotenv(join(dirname(__file__), '.env'))

API_TOKEN = os.environ.get('SLACKBOT_TOKEN')
# このbot宛のメッセージで、どの応答にも当てはまらない場合の応答文字列
DEFAULT_REPLY = 'てすとぅ'
# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins']
