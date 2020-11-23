from flask_restful import Resource, reqparse

import stripe

stripe.api_key = 'sk_test_51HqixTKBS290AVNsOSfzaoCHsc7f2qQrYFwE7WngP90DmFxWZ3UcQ7DSNk4ZKOvrxZDSy9AEemT972qukVGwT5xS00Y7ReyzXr'




class Create(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("amount",
                        type=float,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument("email",
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        
        data = Create.parser.parse_args()

        # stripe.PaymentIntent.create(
        # amount=data["amount"],
        # currency='inr',
        # payment_method_types=['card'],
        # receipt_email='kartiksaini135@gmail.com',
        # )
        # # return stripe.PaymentIntent
        # return {"amount":data["amount"]}


        # return stripe.PaymentIntent
        # return stripe.PaymentIntent.create(
        #         amount=data["amount"],
        #         currency='inr',
        #         payment_method_types=['card'],
        #         receipt_email='kartiksaini135@gmail.com',
        #         )

        
        stripe.Charge.create(
                            amount=int(data["amount"]*100),
                            receipt_email=data["email"],
                            currency="inr",
                            source="tok_visa"
                            )
        return stripe.Charge.list(limit=1)

class Show(Resource):
    def get(self):
        # Create a new Payment Request
        # response = api.payment_request_status('[PAYMENT REQUEST ID]')

        # return response['payment_request']

        # print(response['payment_request'])

        # print(response['payment_request']['shorturl'])  # Get the short URL
        # print(response['payment_request']['status'])    # Get the current status
        # print(response['payment_request']['payments'])  # List of payments
        return stripe.Charge.list()