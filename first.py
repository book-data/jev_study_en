from dotenv import load_dotenv
from typesafe_sdk import Noul, TypeSafeClient

load_dotenv()

message = "The mug I received was broken. Can I return it and get a refund?"

with TypeSafeClient(compression=False) as client:
    response = client.system_one(
        state=message,
        questions={
            "wants_refund": Noul(
                instructions="Is the sender of this inquiry asking for a refund?",
            ),
        },
    )

print(response.nouls["wants_refund"].noul)
