from typesafe_sdk import Choice, Noul, Score

# Minimum confidence for routing to a team automatically. Below this, a human checks it
CONFIDENCE_MIN = 0.8

# Priority weights (total 1.0)
WEIGHTS = {
    "urgency": 0.5,
    "money_at_risk": 0.3,
    "threatens_to_leave": 0.2,
}

# Priority at or above this value is "urgent"
URGENT_MIN = 0.5

QUESTIONS = {
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
    "urgency": Score(
        instructions="How urgently does this inquiry need a response?",
        criteria=[
            "Not urgent. A reply within a few days is fine",
            "Should be handled soon. Reply today or tomorrow",
            "Needs action right now. Money is being lost or a deadline is close",
        ],
    ),
    "money_at_risk": Noul(
        instructions="Does the sender say they have lost money or are about to lose money?",
    ),
    "threatens_to_leave": Noul(
        instructions="Does the sender say they will stop using the store or take the complaint elsewhere?",
    ),
}
