from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is not installed.")
    print("Install it with: pip install pyyaml")
    sys.exit(1)


REGISTRY_PATH = Path("02-agent-registry/agents.yaml")

REQUIRED_FIELDS = [
    "id",
    "number",
    "team",
    "title",
    "purpose",
    "phase",
    "active",
    "model_profile",
    "token_budget",
    "tools",
    "inputs",
    "outputs",
    "reviewer",
]


def main():
    if not REGISTRY_PATH.exists():
        print(f"ERROR: Agent registry file not found: {REGISTRY_PATH}")
        sys.exit(1)

    with REGISTRY_PATH.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not data or "agents" not in data:
        print("ERROR: agents.yaml must contain a top-level 'agents' key.")
        sys.exit(1)

    agents = data["agents"]

    if not isinstance(agents, list):
        print("ERROR: 'agents' must be a list.")
        sys.exit(1)

    errors = []
    seen_ids = set()
    seen_numbers = set()

    for index, agent in enumerate(agents, start=1):
        agent_id = agent.get("id", f"unknown-agent-at-index-{index}")

        for field in REQUIRED_FIELDS:
            if field not in agent:
                errors.append(f"{agent_id}: missing required field '{field}'")

        if "id" in agent:
            if agent["id"] in seen_ids:
                errors.append(f"{agent_id}: duplicate agent id")
            seen_ids.add(agent["id"])

        if "number" in agent:
            if agent["number"] in seen_numbers:
                errors.append(f"{agent_id}: duplicate agent number {agent['number']}")
            seen_numbers.add(agent["number"])

        if "tools" in agent and not isinstance(agent["tools"], list):
            errors.append(f"{agent_id}: 'tools' must be a list")

        if "inputs" in agent and not isinstance(agent["inputs"], list):
            errors.append(f"{agent_id}: 'inputs' must be a list")

        if "outputs" in agent and not isinstance(agent["outputs"], list):
            errors.append(f"{agent_id}: 'outputs' must be a list")

    print(f"Total agents found: {len(agents)}")

    if len(agents) != 44:
        errors.append(f"Expected 44 agents, but found {len(agents)}")

    if errors:
        print("\nAgent registry validation failed:\n")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("Agent registry validation passed successfully.")


if __name__ == "__main__":
    main()