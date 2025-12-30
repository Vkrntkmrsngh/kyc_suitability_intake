from typing import Type, Dict, Any, List
from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class KycCompletenessInput(BaseModel):
    extracted_profile: Dict[str, Any] = Field(..., description="The extracted KYC/suitability profile JSON.")

class KycCompletenessTool(BaseTool):
    name: str = "KYC Completeness Checker"
    description: str = (
        "Checks whether mandatory KYC/suitability fields are present in the extracted profile "
        "and returns missing fields as a list."
    )
    args_schema: Type[BaseModel] = KycCompletenessInput

    def _run(self, extracted_profile: Dict[str, Any]) -> str:
        profile = extracted_profile.get("client_profile", {}) if isinstance(extracted_profile, dict) else {}
        required = {
            "goals": "goals",
            "time_horizon": "time_horizon",
            "liquidity_needs": "liquidity_needs",
            "constraints": "constraints",
            "preferences": "preferences",
        }

        missing: List[str] = []
        for k, label in required.items():
            v = profile.get(k)
            if v is None:
                missing.append(label)
            elif isinstance(v, str) and not v.strip():
                missing.append(label)
            elif isinstance(v, list) and len(v) == 0:
                missing.append(label)

        # Keep it simple: return as a string so agents can paste it into outputs
        return f"Missing required fields: {missing}" if missing else "All required fields present."