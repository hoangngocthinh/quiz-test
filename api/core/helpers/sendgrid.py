from django.conf import settings
import sendgrid


class SendGridMail:
    def __init__(self):
        self._sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
        self._default_from_mail = settings.DEFAULT_FROM_EMAIL
        self._default_sender_name = settings.DEFAULT_SENDER_NAME

    def send_single_mail(
        self, email: str, template_id: str, data: dict, from_mail: str = ""
    ):
        to_email = {"email": email}
        personalizations = [{"to": [to_email], "dynamic_template_data": data}]
        self._send_mail(from_mail, personalizations, template_id)

    def send_multiple_mail(self, template_id: str, data: list, from_mail: str = ""):
        personalizations = []
        for item in data:
            item_mail = {
                "to": [item["to_email"]],
                "dynamic_template_data": item["data_mail"],
            }
            personalizations.append(item_mail)
        self._send_mail(from_mail, template_id, personalizations)

    def _send_mail(self, from_mail, personalizations, template_id):
        try:
            from_mail = from_mail or self._default_from_mail
            data_mail = {
                "personalizations": personalizations,
                "from": {"email": from_mail, "name": self._default_sender_name},
                "template_id": template_id,
            }
            response = self._sg.client.mail.send.post(request_body=data_mail)
            return response
        except Exception as exc:
            raise exc
