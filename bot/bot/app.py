from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from service.service_handling import service
from openai_pdf_chat.pdf_chat import main

app = Flask(__name__)
app.config["SECRET_KEY"] = "top-secret!"  # SECRET KEY CAN BE ANYTHING

# TWILIO

account_sid = "ACffe785d43428bd4bc06e630678781728"
auth_token = "4efa493e12d256d3f911d26b75f8174f"
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


@app.route("/bot", methods=["POST"])
def bot():
    phone_number = request.values["WaId"]
    try:
        if request.values["Body"]:                       ################## 
            incoming_msg = request.values["Body"]
        elif request.values['MediaUrl0']:
            incoming_msg = request.values['MediaUrl0']
        service(incoming_msg, phone_number)
    except:
        if incoming_msg:
            answer = main(incoming_msg)
            send_message(answer, phone_number)
            print(answer)
        else:
            send_message("Message Cannot Be Empty!", phone_number)
    r = MessagingResponse()
    r.message("")
    return str(r)


if __name__ == "__main__":
    app.run()




    # incoming_msg = request.values['MediaUrl0']

    # response = requests.get(incoming_msg)
    # image_content = response.content
    # image = Image.open(BytesIO(image_content))
    # image.save("image_test.jpg")
