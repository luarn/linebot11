#app1.py
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
app = Flask(__name__)

# LINE 聊天機器人的基本資料
#line_bot_api = LineBotApi(' 你的Channel access token (long-lived) ')
#handler = WebhookHandler(' 你的Channel secret ')
line_bot_api = LineBotApi('LfgFsao2M8AOButxVc+AmwKXz4gl+/ug2ofbekaDcEAGTniTCsoDjEKc1HrTBndK5iT9Ttcj2Qp3BVUWBxUxYus/tJHxX7sSzU4qeQmSuJF5xinHkdU6RT8Ko5r799Kv9CKaNuYy8P00s5OoRKqFfwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2e746db03940d5d2339a56529dc850bc')


# 接收 LINE 的資訊
#@app.route("/", methods=['POST'])
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    
    if event.message.text==u"==":
        replay_message(event,TextSendMessage(u"如果輸入==不要加空格回覆此行"))
        push_message(event,TextSendMessage(u"謝謝光臨"))
        
    else:
        replay_message(event,message)
        push_message(event,TextSendMessage(u"謝謝光臨"))

def replay_message(event,text):
    line_bot_api.reply_message(event.reply_token,text)
        
def push_message(event,text):
    line_bot_api.push_message(event.source.user_id,text)        


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

#if __name__ == "__main__":
#    app.run()
