# from django.test import TestCase
# from twilio.rest import Client

# # Create your tests here.
# def send_report_via_sms():
#     account_sid = 'AC7414d6a657471be7c189513415179c50'
#     auth_token = '0e9e669a01867d9c7e75c13c5722e84e'
#     client = Client(account_sid, auth_token)

#     message = client.messages.create(
#     from_='whatsapp:+14155238886',
#             body = f'''नमस्ते, आर्यन
#                     उत्पाद का नाम: मक्का
#                     समाप्ति तिथि: कल, 26-02-2024

#                     उत्पाद का नाम: ज्वार
#                     समाप्ति तिथि: कल, 26-02-2024

#                     उत्पाद का नाम: गेहूं
#                     समाप्ति तिथि: कल, 26-02-2024

#                     उत्पाद का नाम: चावल
#                     समाप्ति तिथि: कल, 26-02-2024

#                     कृपया इन्हें जल्द से जल्द उपयोग करें या बाजार में बेचने के लिए विचार करें। धन्यवाद!''',
#   to='whatsapp:+918879519771'
#     )

#     print(message.sid)

# send_report_via_sms()

def send_report_via_sms():
    account_sid = 'ACc0fb9078b0a79b48380326210fa0fddc'

    auth_token = 'ce04d00700e943e6fcb1a465a28c0106'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+15138224044',
            body = f'''नमस्ते, Harsh
                    उत्पाद का नाम: मक्का 🌽
                    समाप्ति तिथि: कल, 16-05-2025

                    उत्पाद का नाम: ज्वार 🌱
                    समाप्ति तिथि: कल, 16-05-2025

                    उत्पाद का नाम: गेहूं 🌾
                    समाप्ति तिथि: कल, 16-05-2025

                    उत्पाद का नाम: चावल 🌾
                    समाप्ति तिथि: कल, 16-05-2025

                    कृपया इन्हें जल्द से जल्द उपयोग करें या बाजार में बेचने के लिए विचार करें। धन्यवाद!''',
  to='+916202603974'
    )

    print(message.sid)