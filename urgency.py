from dotenv import load_dotenv
from typesafe_sdk import Score, TypeSafeClient

load_dotenv()

message = "My credit card was charged twice for the same order! Please fix this today."

with TypeSafeClient(compression=False) as client:
    response = client.system_one(
        state=message,
        questions={
            "urgency": Score(
                instructions="How urgently does this inquiry need a response?",
                criteria=[
                    "Not urgent. A reply within a few days is fine",
                    "Should be handled soon. Reply today or tomorrow",
                    "Needs action right now. Money is being lost or a deadline is close",
                ],
            ),
        },
    )

answer = response.scores["urgency"]
print("Urgency:", answer.score)
print("Confidence:", answer.confidence)
print("Probabilities:", answer.probabilities)
