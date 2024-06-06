import africastalking


sms = africastalking.SMS


def send_sms(message, phone_number):
    """
    Send an SMS notification using Africa's Talking API.

    :param message: Message to be sent.
    :param phone_number: Recipient's phone number.
    :return: True if the SMS was sent successfully, False otherwise.
    """
    try:
        response = sms.send(message, [phone_number])
        if response['SMSMessageData']['Recipients'][0]['statusCode'] == 101:
            return True
        else:
            return False
    except Exception as e:
        return False