import boto3
import json


def generate_ai_summary(
    high_regions,
    surplus_regions,
    lost_revenue,
    holding_cost,
    redistribution_plan
):

    high_regions_list = ", ".join(
        high_regions["region"].tolist()
    ) or "None"

    surplus_regions_list = ", ".join(
        surplus_regions["region"].tolist()
    ) or "None"

    total_transfer_units = sum(
        item["Units to Transfer"]
        for item in redistribution_plan
    ) if redistribution_plan else 0

    prompt = f"""
You are a senior supply chain strategy consultant.

High Demand Regions: {high_regions_list}
Surplus Regions: {surplus_regions_list}
Potential Lost Revenue: ₹{lost_revenue:,}
Estimated Holding Cost: ₹{holding_cost:,}
Proposed Redistribution Units: {total_transfer_units:,}

Write a concise executive-level strategic summary explaining:
- Current operational risk
- Financial exposure
- Recommended redistribution strategy
- Expected business impact

Keep it professional and board-ready.
"""

    try:

        bedrock = boto3.client(
            service_name="bedrock-runtime",
            region_name="ap-south-1"
        )

        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 500,
            "temperature": 0.6,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })

        response = bedrock.invoke_model(
            body=body,
            modelId="arn:aws:bedrock:ap-south-1:752995910188:inference-profile/apac.anthropic.claude-3-haiku-20240307-v1:0",
            accept="application/json",
            contentType="application/json"
        )

        response_body = json.loads(
            response["body"].read()
        )

        return response_body["content"][0]["text"]

    except Exception as e:

        return f"Bedrock Error: {str(e)}"