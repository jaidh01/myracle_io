import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ['GENAI_API_KEY'])


def generatecontent(context, file):
    myfile = genai.upload_file(file)
#print(f"{myfile=}")

    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content(
        [myfile, "\n\n", """Context for Test Case Title: {context}

Instructions: USE the PROVIDED CONTEXT to GENERATE a TEST CASE that specifically focuses on the key functionality. The test case should adhere to the following structure and be fully aligned with the context provided:

Test Case ID: A unique identifier for the test case, often following a naming convention (e.g., TC-001).

Test Case Title: A brief description of what the test case is focused on, directly related to the context provided.

Description: A detailed explanation of what the test case is intended to validate, clearly tied to the context. For example, if the context is "order product," the description should focus on the entire process of ordering a product, from selection to payment confirmation.

Pre-conditions: Any requirements or setup that must be in place before the test can be executed. This might include user login status, device configuration, or app settings.

Test Data: Any specific data needed for the test, such as product details, payment methods, shipping addresses, or configurations. If no test data is needed, clearly mark it as "N/A."

Testing Steps: A sequential list of steps that the tester should follow to execute the test, explicitly aligned with the context. For example, in the context of "order product," the steps should guide the tester through selecting a product, adding it to the cart, entering payment details, and confirming the order.

Expected Result: A clear description of what should happen if the feature works correctly, based on the context. For example, the expected result should confirm successful order placement and order confirmation.

Post-conditions: Any state the system should be in after the test is executed. For example, the order should be placed, and the user's order history should be updated.

Priority: The importance of the test case (e.g., High, Medium, Low), informed by the context. This helps prioritize testing efforts.

Status: The current status of the test case (e.g., Not Executed, Pass, Fail). This is updated during the testing phase.

Edge Cases & Variations: Consider various scenarios that might affect the test outcome, such as different payment methods, shipping addresses, or user states (e.g., logged in vs. guest checkout).

Refinement Option: Offer suggestions for improving the test case, such as adding additional scenarios, breaking down complex steps, or considering alternative flows related to the context.

Note: Ensure that the generated test case remains fully focused on the provided context, without deviating into unrelated functionalities."""]
    ).text
    print(result)


#context="Source, Destination, and Date Selection, build the test case for all these 3 tasks."
#generatecontent(context)