from unittest.mock import Mock

from flight_assistant.use_cases import SummarizeFareRulesUseCase


def test_summarize_fare_rules():
    expected = "New Summary"
    summarizer = Mock()
    summarizer.summarize.return_value = expected
    use_case = SummarizeFareRulesUseCase(summarizer)
    rules = (
        "\n  CHANGES\n\n"
        "    BEFORE DEPARTURE\n"
        "      PER COUPON CHARGE USD 17.00 FOR REISSUE.\n         "
        "NOTE -\n"
        "          - DATE CHANGE/FLIGHT CHANGE/REROUTE APPLY WITH\n"
        "          FEE 17 USD FOR DOMESTIC SEGMENT APPLIED FARE\n"
        "          DIFFERENT IF ANY. THESE FEES APPLY FOR ALL ADULTS\n"
        "          AND CHILDREN.\n"
        "          DO NOT APPLY THESE FEES FOR INFANTS.\n"
        "          - DATE/FLIGHT/ROUTE CHANGE MUST BE DONE 3 HOURS\n"
        "          PRIOR TO DEPARTURE TIME.\n"
        "          -------------------------------------------\n          "
        "- NAME CHANGE BEFORE TICKET ISSUE IS FREE OF\n"
        "          CHARGE.\n          "
        "- NAME CHANGE AFTER TICKET ISSUE IS NOT\n"
        "          PERMITTED.\n"
        "          --------------------------------------------\n"
        "          NAME COLLECTION OR SPELLING BEFORE TICKET ISSUE\n"
        "          IS FREE OF CHARGE. AFTER TICKET ISSUE FEE\n"
        "          200000VND PER INTERNATIONAL SEGMENT. FOR FURTHER\n"
        "          INFORMATION PLEASE CONTACT AIRLINE TO BE\n"
        "          SUPPORTED AT GDS -AT- VIETJETAIR.COM\n"
        "          ---------------------------------------------\n"
        "          TITLE CORRECTION BEFORE 3 HOURS PRIOR TO SCHEDULE\n"
        "          DEPARTURE TIME FREE OF CHARGE WITHIN 3 HOURS THE\n"
        "          FEE 100000VND PER PASSENGER PER TICKET WILL BE\n"
        "          COLLECTED AT THE AIRPORT\n"
        "          STATION.\n"
        "          ----------------------------------------------\n"
        "          REISSUE TICKET IS REQUIRED FOR ANY\n          CHANGE.\n"
        "          ----------------------------------------------\n\n"
        "    AFTER DEPARTURE\n"
        "      CHANGES NOT PERMITTED IN CASE OF NO-SHOW.\n\n"
        "  CANCELLATIONS\n\n"
        "    TICKET IS NON-REFUNDABLE IN CASE OF CANCEL/NO-SHOW/\n"
        "      REFUND.\n"
        "         NOTE -\n"
        "          NOT ALLOW REFUND TO ORIGINAL PAYMENT METHOD.\n"
        "          REFUND AS CREDIT SHELL ENTITLED TO PASSSENGER UP\n"
        "          TO 180 DAYS FROM THE DATE OF DEPARTURE IS ALLOWED\n"
        "          FOR UNUSED TICKET FOR VJ INTERNATIONAL FLIGHT.\n"
        "          THE REQUEST  TIME OF REFUND MUST BE AT LEAST 24\n"
        "          HOURS BEFORE DEPARTURE TIME.\n"
        "          REISSUE FEE USD17/PER PAX/PER COUPON WHEN\n"
        "          REBOOKING USING CREDIT SHELL."
    )

    actual = use_case.execute(rules)

    assert actual == expected
