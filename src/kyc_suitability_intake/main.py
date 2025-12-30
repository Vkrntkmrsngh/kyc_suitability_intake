from kyc_suitability_intake.crew import KycSuitabilityIntakeCrew

def run():
    sample_intake = """
    Client met advisor for initial discovery. Primary goal: retirement in ~12 years.
    Prefers stability, uncomfortable with large drawdowns. Needs emergency fund liquidity.
    Has existing 401(k) and brokerage account. Mentions upcoming home purchase in 2 years.
    No mention of tax constraints. No explicit constraints on industries. Time horizon mixed.
    """

    result = KycSuitabilityIntakeCrew().crew().kickoff(
        inputs={
            "client_name": "Nancy Peterson",
            "intake_text": sample_intake
        }
    )

    print(result)

if __name__ == "__main__":
    run()