### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")


def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


### Dialog Actions Helper Functions ###
def get_slots(intent_request):

    """
    Fetch all the slots and their values from the current intent.

    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


"""
Step 3: Enhance the Robo Advisor with an Amazon Lambda Function

In this section, you will create an Amazon Lambda function that will validate the data provided by the user on the Robo Advisor.

1. Start by creating a new Lambda function from scratch and name it `recommendPortfolio`. Select Python 3.7 as runtime.

2. In the Lambda function code editor, continue by deleting the AWS generated default lines of code, then paste in the starter code provided in `lambda_function.py`.

3. Complete the `recommend_portfolio()` function by adding these validation rules:

    * The `age` should be greater than zero and less than 65.
    * The `investment_amount` should be equal to or greater than 5000.

4. Once the intent is fulfilled, the bot should respond with an investment recommendation based on the selected risk level as follows:

    * **none:** "100% bonds (AGG), 0% equities (SPY)"
    * **low:** "60% bonds (AGG), 40% equities (SPY)"
    * **medium:** "40% bonds (AGG), 60% equities (SPY)"
    * **high:** "20% bonds (AGG), 80% equities (SPY)"

> **Hint:** Be creative while coding your solution, you can have all the code on the `recommend_portfolio()` function, or you can split the functionality across different functions, put your Python coding skills in action!

5. Once you finish coding your Lambda function, test it using the sample test events provided for this Challenge.

6. After successfully testing your code, open the Amazon Lex Console and navigate to the `recommendPortfolio` bot configuration, integrate your new Lambda function by selecting it in the “Lambda initialization and validation” and “Fulfillment” sections.

7. Build your bot, and test it with valid and invalid data for the slots.

"""


### Intents Handlers ###
def recommend_portfolio(intent_request): 

    if intent_request["invocationSource"] == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.
        first_name = get_slots(intent_request)["firstName"]
        age = get_slots(intent_request)["age"]
        investment_amount = get_slots(intent_request)["investment_amount"]
        risk_level = intent_request["invocationSource"]
    
    if source == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.

        ### YOUR CODE STARTS HERE ###
        # Validate that the user is over the age of 18.
        if age < 18:
            # If the user is under the age of 18, ask them to update their
            # profile.
            return close(
                intent_request["sessionAttributes"],
                "Fulfilled",
                {
                    "contentType": "PlainText",
                    "content": "You are not old enough to use this service. "
                    + "Please update your profile.",
                },
            )
        
        # Validate that the user has enough money to make the purchase.
        if investment_amount < 5000:
            # If the user does not have enough money, tell them that they will
            # need to increase their savings.
            return close(
                intent_request["sessionAttributes"],
                "Fulfilled",
                {
                    "contentType": "PlainText",
                    "content": "You must have at least $5000 in order to make this purchase.",
                },
            )

        # Get risk level of the user.
        risk_level = get_slots(intent_request)["risk_level"]

        # Get the portfolio recommendation for the risk level.
        ### YOUR CODE ENDS HERE ###

        # Return a message with the results of the portfolio recommendation.
        return close(
            intent_request["sessionAttributes"],
            "Fulfilled",
            {
                "contentType": "PlainText",
                "content": "Here is your recommended portfolio: {}".format(
                    risk_level
                ),
            },
        )

    raise Exception("Intent handler 'recommend_portfolio' was called with invalid source.")

        # Use the elicitSlot dialog action to re-prompt for the first violation detected.
    return delegate(session_attributes, get_slots(intent_request))
    slots = get_slots(intent_request)
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": "Thanks, {first_name}. We have sent your information to the Robo Advisor.".format(
                first_name=first_name
            ),
        },
    )


        #for the violation detected, send a message to the user explaining the validation failure, and
        #elicitSlot to prompt for the correct slot value.
        return elicit_slot(
            intent_request["sessionAttributes"],
            intent_request["currentIntent"]["name"],
            slots,
            violation_key,
            response_card,
        )
        #  re-prompt for the correct value.
        validation_result = validate_data(age, investment_amount, intent_request)
        if not validation_result["isValid"]:
            slots[validation_result["violatedSlot"]] = None
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )

        # Fetch current session attributes for the session
        output_session_attributes = intent_request["sessionAttributes"]

        return delegate(output_session_attributes, get_slots(intent_request))

    # Get the initial investment recommendation
    risk_level = get_slots(intent_request)["risk_level"]
    investment_recommendation = get_investment_recommendation(risk_level)

    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": "Hi {}, thank you for your information; your recommended portfolio is {}".format(
                first_name, investment_recommendation
            ),
        },
    )




### YOUR CODE STARTS HERE ###
# Validate that the user is over the age of 18.
    if age < 18:
    # If the user is under the age of 18, ask them to update their
    # profile.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": "You are not old enough to use this service. "
            + "Please update your profile.",
        },
    )
# Use the elicitSlot dialog action to re-prompt for the first violation detected.

    return delegate(session_attributes, get_slots(intent_request))
    slots = get_slots(intent_request)
    return close(
                   # Get the risk level of the user.

 
    
    """
    Performs dialog management and fulfillment for recommending a portfolio.

    """

    first_name = get_slots(intent_request)["firstName"]
    age = get_slots(intent_request)["age"]
    investment_amount = get_slots(intent_request)["investmentAmount"]
    risk_level = get_slots(intent_request)["riskLevel"]
    source = intent_request["invocationSource"]

    # YOUR CODE GOES HERE!

    if source == "age": # age validation
        if age is not None:
            age = parse_int(age)
            if age < 0 or age > 65:
                return build_validation_result(
                    False,
                    "age",
                    "I'm sorry, {} is not between 0 and 65. Please provide an age between 0 and 65.".format(age),
                )
        else:
            return build_validation_result(
                False, "age", "I'm sorry, I did not hear an age for you. Please provide an age between 0 and 65."
            )
    if source == "investmentAmount": # investment amount validation
        if investment_amount is not None:
            investment_amount = parse_int(investment_amount)
            if investment_amount < 5000:
                return build_validation_result(
                    False,
                    "investmentAmount",
                    "I'm sorry, {} is not greater than 5000. Please provide an investment amount greater than 5000.".format(investment_amount),
                )
        else:
            return build_validation_result(
                False, "investmentAmount", "I'm sorry, I did not hear an investment amount for you. Please provide an investment amount greater than 5000."
            )

    # If age or investment amount are missing, ask for them and return None.
    if age is None or investment_amount is None:
        return None

    if risk_level is not None:
        return delegate(
            intent_request["sessionAttributes"],
            get_slots(intent_request),
            "recommendPortfolio",
        )

    # If age or investment amount are valid, call the recommend_portfolio() function to provide the recommendation.
    recommendation = recommend_portfolio(age, investment_amount)

    # Return the result to the user.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": "Here is your {} portfolio recommendation: {}".format(
                risk_level, recommendation
            ),
        },
    )

    if risk_level is None:
        return elicit_slot(
            intent_request["sessionAttributes"],
            "recommendPortfolio",
            get_slots(intent_request),
            "riskLevel",
            {
                "contentType": "PlainText",
                "content": "Please provide the level of risk you want associated with your portfolio.",
            },
        )

    if risk_level == "none":
        return close(
            intent_request["sessionAttributes"],
            "Fulfilled",
            {
                "contentType": "PlainText",
                "content": "Here is your Low Risk portfolio recommendation: 100% bonds (AGG), 0% equities (SPY)".format(
                    risk_level, recommendation
                ),
            },
        )
    
    if risk_level == "low":
        return close(
            intent_request["sessionAttributes"],
            "Fulfilled",
            {
                "contentType": "PlainText",
                "content": "Here is your Low portfolio recommendation: 60% bonds (AGG), 40% equities (SPY)".format(
                    risk_level, recommendation
                ),
            },
        )

    if risk_level == "medium":
        return close(
            intent_request["sessionAttributes"],
            "Fulfilled",
            {
                "contentType": "PlainText",
                "content": "Here is your Medium portfolio recommendation: 40% bonds (AGG), 60% equities (SPY)".format(
                    risk_level, recommendation
                ),
            },
        )

    if risk_level == "high":
        return close(
            intent_request["sessionAttributes"],
            "Fulfilled",
            {
                "contentType": "PlainText",
                "content": "Here is your High portfolio recommendation: 20% bonds (AGG), 80% equities (SPY)".format(
                    risk_level, recommendation
                ),
            },
        )
    
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": "I'm sorry, I could not find an appropriate portfolio for you.",
        },
    )


    return recommend_portfolio(age, investment_amount, risk_level)  # None




### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "recommendPortfolio":
        return recommend_portfolio(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
