from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from service import service_handling 
from openai_pdf_chat.pdf_chat import main
import requests
from PIL import Image
from io import BytesIO
from voice_recognition.handle_voice import voice_handler
import unicodedata


app = Flask(__name__)
app.config["SECRET_KEY"] = "top-secret!"  # SECRET KEY CAN BE ANYTHING

# TWILIO

account_sid = "ACc921595161b4b8519c10c797a8e920f7"
auth_token = "22b896dd261e522c8294049aea134625"
client = Client(account_sid, auth_token)

def send_message(body_mess, phone_number):
    message = client.messages.create(
        from_="whatsapp:+14155238886",  # With Country Code
        body=body_mess,
        to="whatsapp:" + phone_number,  # With Country Code
    )
    print(message)

def send_media_message(media_url, phone_number):
    client.messages.create(
        from_="whatsapp:+14155238886",  # With Country Code
        # body="Check out this image!",
        media_url=[media_url],
        to="whatsapp:" + phone_number,  # With Country Code
    )


# @app.route("/bot", methods=["POST"])
# def bot():
#     phone_number = request.values["WaId"]
#     incoming_msg = request.values['Body']
#     try:
#         service(incoming_msg, phone_number)
#     except:
#         if incoming_msg:
#             answer = main(incoming_msg)
#             send_message(answer, phone_number)
#             print(answer)
#         else:
#             send_message("Message Cannot Be Empty!", phone_number)
#     r = MessagingResponse()
#     r.message("")
#     return str(r)


# if __name__ == "__main__":
#     app.run()



welcoming_message = 0

@app.route("/bot", methods=["POST"])
def bot():
    
    global welcoming_message 
    phone_number = request.values["WaId"]

    if welcoming_message == 0:
        send_message("helooooo", phone_number)
        welcoming_message += 1
        return ""

    if request.values['Body']:
        incoming_msg = request.values['Body'] 

    elif request.values['MediaUrl0'] and request.values["MediaContentType0"] == "audio/ogg":
        incoming_msg = request.values['MediaUrl0']
        response = requests.get(incoming_msg)
        audio_content = response.content
        with open("../voice_message/audio.ogg", "wb") as file:
            file.write(audio_content)
        incoming_msg = voice_handler()

        print(incoming_msg)

        normalized_text = unicodedata.normalize("NFKC", incoming_msg)

        # Convert the normalized text to standard Arabic Unicode range
        converted_text = "".join(
            char
            for char in normalized_text
            if unicodedata.bidirectional(char) == "AL"
        )       

        incoming_msg = converted_text
        print(converted_text)

    elif request.values['MediaUrl0'] and request.values["MediaContentType0"] == "image/jpeg" and service_handling.current_process == "11":
        incoming_msg = request.values['MediaUrl0']
        response = requests.get(incoming_msg)
        image_content = response.content
        image = Image.open(BytesIO(image_content))
        image.save(f"../images/user_image_input{len(list(service_handling.responses.values())[0]) + 1}.jpeg")
    
    else:
        send_message("Message Cannot Be Empty!", phone_number)
    
    try:
        service_handling.service(incoming_msg, phone_number)
    except:
        answer = main(incoming_msg)
        send_message(answer, phone_number)
        print(answer)
    r = MessagingResponse()
    r.message("")
    return str(r)


if __name__ == "__main__":
    app.run()
