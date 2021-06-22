import stripe


stripe.api_key = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"

customer = stripe.Customer.create(
    description="My First Test Customer (created for API docs)",
)
#customer = stripe.Customer.retrieve(customer.id)

payment_intent = stripe.PaymentIntent.create(
    customer=customer.id,
    amount=1099,
    currency='usd',
    payment_method_types=['card'],
    setup_future_usage='on_session',
    capture_method='manual'
)
