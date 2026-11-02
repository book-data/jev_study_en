from dotenv import load_dotenv
from typesafe_sdk import Choice, TypeSafeClient

load_dotenv()

message = "My order still hasn't arrived. The order number is A-1021. It's been a week since the estimated ship date."

with TypeSafeClient(compression=False) as client:
    response = client.system_one(
        state=message,
        questions={
            "team": Choice(
                instructions="Which team should handle this inquiry?",
                criteria={
                    "shipping": "Delivery status, items not arriving, changes to the shipping address",
                    "returns": "Returns, exchanges, refunds, damaged or defective items",
                    "payment": "Payments, billing, double charges, receipts",
                    "product": "Questions about product specifications or how to use a product",
                    "other": "Anything that does not fit any of the above",
                },
            ),
        },
    )

answer = response.choices["team"]
print("Team:", answer.choice)
print("Confidence:", answer.confidence)
print("Probabilities:", answer.probabilities)
