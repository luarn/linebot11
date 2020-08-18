#app11.py
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
#from linebot.models import (
#    MessageEvent, TextMessage, TextSendMessage,
#)
from linebot.models import *

import os
app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi(' 你的Channel access token (long-lived) ')
handler = WebhookHandler(' 你的Channel secret ')



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

# 處理輸入的文字
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    message = TextSendMessage(text=event.message.text)
    
    if event.message.text==u"==":
        line_bot_api.reply_message(event.reply_token,TextSendMessage(u"如果輸入==不要加空格回覆此行"))
    elif event.message.text == u"貼圖":
        line_bot_api.reply_message(event.reply_token,StickerSendMessage(package_id=1, sticker_id=3))
    elif event.message.text == u"圖片":
        line_bot_api.reply_message(event.reply_token,ImageSendMessage(original_content_url='https://myalbum.com/photo/ND94LXJCrVMW/360.jpg',
        preview_image_url='https://myalbum.com/photo/ND94LXJCrVMW/360.jpg'))
    elif event.message.text == u"影片":
        line_bot_api.reply_message(event.reply_token,VideoSendMessage(original_content_url='https://github.com/line/line-bot-sdk-nodejs/raw/master/examples/kitchensink/static/imagemap/video.mp4',
        preview_image_url='https://github.com/line/line-bot-sdk-nodejs/raw/master/examples/kitchensink/static/imagemap/preview.jpg'))
    elif event.message.text == u"音訊":
        line_bot_api.reply_message(event.reply_token,AudioSendMessage(original_content_url='https://s3-ap-northeast-1.amazonaws.com/dazedbear-assets/Bluebird.mp3', duration=100000))
    elif event.message.text == "位置":
        line_bot_api.reply_message(event.reply_token,LocationSendMessage(title='我的位置', address='台科大', latitude=25.013277, longitude=121.540617))
    elif event.message.text == "位置2":
        imagemap_message = ImagemapSendMessage(
                        base_url='https://myalbum.com/photo/9DudM7hcSgBs/540.jpg#',
                        alt_text='this is an imagemap',
                        base_size=BaseSize(height=1040, width=1040),
                        actions=[
                            URIImagemapAction(
                                link_uri='https://www.ntust.edu.tw/',
                                area=ImagemapArea(
                                    x=0, y=0, width=520, height=1040
                                )
                            ),
                            MessageImagemapAction(
                                text='hello',
                                area=ImagemapArea(
                                    x=520, y=0, width=520, height=1040
                                )
                            )
                        ]
                    )
        line_bot_api.reply_message(event.reply_token,imagemap_message)
    elif event.message.text == "開始":    
        buttons_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ButtonsTemplate(
            title='Template-樣板介紹',
            text='Template分為四種，也就是以下四種：',
            thumbnail_image_url='https://myalbum.com/photo/TNB44WsxDtgL/360.jpg',
            actions=[
                MessageTemplateAction(
                    label='Buttons Template',
                    text='Buttons Template'
                ),
                MessageTemplateAction(
                    label='Confirm template',
                    text='Confirm template'
                ),
                MessageTemplateAction(
                    label='Carousel template',
                    text='Carousel template'
                ),
                MessageTemplateAction(
                    label='Image Carousel',
                    text='Image Carousel'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif event.message.text == "Buttons Template":       
        buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='這是ButtonsTemplate',
            text='ButtonsTemplate可以傳送text,uri',
            thumbnail_image_url='https://myalbum.com/photo/zmsT9qdUgesL/360.jpg',
            actions=[
                MessageTemplateAction(
                    label='ButtonsTemplate',
                    text='ButtonsTemplate'
                ),
                URITemplateAction(
                    label='VIDEO1',
                    uri='https://github.com/line/line-bot-sdk-nodejs/raw/master/examples/kitchensink/static/imagemap/video.mp4'
                ),
                PostbackTemplateAction(
                label='postback',
                text='postback text',
                data='postback1'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token, buttons_template)
    elif event.message.text == "Carousel template":
        print("Carousel template")       
        Carousel_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://myalbum.com/photo/V2T4Ev5oRsku/360.jpg',
                title='this is menu1',
                text='description1',
                actions=[
                    PostbackTemplateAction(
                        label='postback1',
                        text='postback text1',
                        data='action=buy&itemid=1'
                    ),
                    MessageTemplateAction(
                        label='message1',
                        text='message text1'
                    ),
                    URITemplateAction(
                        label='station',
                        uri='https://www.railway.gov.tw/tra-tip-web/tip'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://myalbum.com/photo/H8YwbUE48wEm/360.jpg',
                title='this is menu2',
                text='description2',
                actions=[
                    PostbackTemplateAction(
                        label='postback2',
                        text='postback text2',
                        data='action=buy&itemid=2'
                    ),
                    MessageTemplateAction(
                        label='message2',
                        text='message text2'
                    ),
                    URITemplateAction(
                        label='food panda',
                        uri='https://www.foodpanda.com.tw/'
                    )
                ]
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Carousel_template)
    elif event.message.text == "Confirm template":
        print("Confirm template")       
        Confirm_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ConfirmTemplate(
            title='這是ConfirmTemplate',
            text='這就是ConfirmTemplate,用於兩種按鈕選擇',
            actions=[                              
                PostbackTemplateAction(
                    label='Y',
                    text='Y',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='N',
                    text='N'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Confirm_template)
    elif event.message.text == "Image Carousel":
        print("Image Carousel")       
        Image_Carousel = TemplateSendMessage(
        alt_text='Image Carousel template',
        template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://myalbum.com/photo/u9SnsjctSiCs/360.jpg',
                action=PostbackTemplateAction(
                    label='postback1',
                    text='postback text1',
                    data='action=buy&itemid=1'
                )
            ),
            ImageCarouselColumn(
                image_url='https://myalbum.com/photo/RQcPjmBSrUNR/360.jpg',
                action=PostbackTemplateAction(
                    label='postback2',
                    text='postback text2',
                    data='action=buy&itemid=2'
                )
            )
        ]
    )
    )
        line_bot_api.reply_message(event.reply_token,Image_Carousel)

    else:
        line_bot_api.reply_message(event.reply_token,message)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

