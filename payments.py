import stripe
import logging
from bottle import request


def stripe_pay(amount, user):
    """
    simplistic Stripe payment handler, returns a tuple
    1. successful charge information
    2. message
    """
    # Set your secret key: remember to change this to your
    # live secret key in production
    # See your keys here https://manage.stripe.com/account
    stripe.api_key = "sk_test_PQmCHxMcjCGfzbFstIuIYRkr"

    # Get the credit card details submitted by the form
    token = request.POST['stripeToken']
    # Create the charge on Stripe's servers - this will charge the user's card
    try:
        charge = stripe.Charge.create(
            amount=amount,  # amount in cents, again
            currency="usd",
            card=token,
            description="Site Notifier upgrade for user_id {}, "
                        "email {}".format(user.user_id(), user.email())
        )
        logging.info('payment id: {}'.format(charge.id))
        return charge, "Payment successful"
    except stripe.CardError:
        return (
            None,
            "The card was declined, please check card information and try again"
        )
