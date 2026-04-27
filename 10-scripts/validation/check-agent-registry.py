from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

try:
    import yaml
except ImportError as exc:
    print("ERROR: PyYAML is required. Install dependencies with: pip install -r requirements.txt")
    raise SystemExit(1) from exc


ROOT = Path(__file__).resolve().parents[2]

AGENTS_FILE = ROOT / "02-agent-registry" / "agents.yaml"
TEAMS_FILE = ROOT / "02-agent-registry" / "teams.yaml"
MODEL_ROUTING_FILE = ROOT / "02-agent-registry" / "model-routing.yaml"
TOKEN_POLICY_FILE = ROOT / "02-agent-registry" / "token-policy.yaml"


def load_yaml(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Missing required file: {path.relative_to(ROOT)}")

    if path.stat().st_size == 0:
        raise ValueError(f"Required file is empty: {path.relative_to(ROOT)}")

    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_agents(data: Any) -> int:
    if not isinstance(data, dict):
        raise ValueError("agents.yaml must contain a top-level mapping.")

    agents = data.get("agents")
    if not isinstance(agents, list):
        raise ValueError("agents.yaml must contain an 'agents' list.")

    seen_ids: set[str] = set()

    for index, agent in enumerate(agents, start=1):
        if not isinstance(agent, dict):
            raise ValueError(f"Agent entry #{index} must be a mapping.")

        agent_id = agent.get("id")
        name = agent.get("name")

        if not agent_id or not isinstance(agent_id, str):
            raise ValueError(f"Agent entry #{index} is missing a valid 'id'.")

        if not name or not isinstance(name, str):
            raise ValueError(f"Agent '{agent_id}' is missing a valid 'name'.")

        if agent_id in seen_ids:
            raise ValueError(f"Duplicate agent id found: {agent_id}")

        seen_ids.add(agent_id)

    return len(agents)


def validate_yaml_mapping(path: Path, label: str) -> None:
    data = load_yaml(path)

    if not isinstance(data, dict):
        raise ValueError(f"{label} must contain a top-level mapping.")


def main() -> int:
    try:
        agents_data = load_yaml(AGENTS_FILE)
        total_agents = validate_agents(agents_data)

        validate_yaml_mapping(TEAMS_FILE, "teams.yaml")
        validate_yaml_mapping(MODEL_ROUTING_FILE, "model-routing.yaml")
        validate_yaml_mapping(TOKEN_POLICY_FILE, "token-policy.yaml")

    except Exception as exc:
        print(f"Agent registry validation failed: {exc}")
        return 1

    print(f"Agent registry validation passed successfully.")
    print(f"Total agents found: {total_agents}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
