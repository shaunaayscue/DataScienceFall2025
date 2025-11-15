import engine
from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"


def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    if input("Is your budget medium? (y/n): ").lower().startswith("y"):
        facts.append("budget_medium")
    if input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")
    if input("Do you primarily do gaming? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    if input("Do you primarily do creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Is your work mostly office only? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    if input("Do you prefer Windows? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_windows")
    if input("Do you prefer macOS? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")
    if input("Do you prefer Linux? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")
    if input("Do you need AI acceleration? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    if input("Do you prefer a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    return facts


def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)
    facts = collect_initial_facts()
    engine.assert_facts(facts)
    engine.run()
    results = engine.conclusions()

    # results and explanations
    for r in results["recommendations"]:
        print(f"\n> Recommendation: {r}")
    for step in engine.trace:
        confidence = step.get("cf", 1.0)
        print(
            f"> Explanation: derived from rule '{step['rule']}' "
            f"(confidence {confidence:.2f}) "
            f"\n> Why: Facts [{', '.join(step['antecedents'])}] were satisfied"
            f"\n> How: This led to [{step['derived']}]"
        )
    print("> Fired rules:", ", ".join(results["fired_rules"]))


if __name__ == "__main__":
    main()
