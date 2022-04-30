from flask import Flask, request, abort # flask, django都是做網頁設計的架構

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('je3nDAnzAfv43YduRr6eVPykQbUGCSJMNBbaZpisSZwL98Qp92gLCSAhi3YtOC3TIRD5xEDK9S4fdYyUsNvtue4g5rGldb3Xg/JhkzPERYyCEJV+8OCMhnrWhyTtrFnR0XOaxngYmEX/69thrHUYxwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('98b8d7444e710a3f4f58e945e97f1a37')


@app.route("/callback", methods=['POST']) # route路徑; callback接收line的訊息並執行下方這function
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage) # 上方功能被觸發後緊接著處理這部分function
def handle_message(event):
    msg = event.message.text
    r = '很抱歉 您說什麼'

    if '給我貼圖' in msg:
    sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )

        line_bot_api.reply_message(
        event.reply_token,       # token 權杖:回復訊息
        sticker_message)   
        return

    if msg in ['hi', 'Hi']:
        r = '嗨'
    elif msg == '你吃飯了嗎':
        r = '還沒'
    elif msg == '你是誰':
        r = '我是機器人'
    elif '訂位' in msg:
        r = '您想訂位是嗎'
    



if __name__ == "__main__":
    app.run()