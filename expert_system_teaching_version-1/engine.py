from dataclasses import dataclass
from typing import List, Set, Dict, Any


@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""
    cf: float = 1.0


class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """TODO: Return True if all antecedents are true and consequent not yet known."""
        # antecedents in the facts?
        for a in rule.antecedents:
            if a not in self.facts:
                return False
        # consequent already known?
        if rule.consequent in self.facts:
            return False

        # all antecedents satisfied?
        return True

    def run(self) -> None:
        """TODO: Implement the forward chaining loop."""
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        while True:
            rules_fire = [r for r in self.rules if self.can_fire(r)]
            if not rules_fire:
                print("no more rules can fire")
                break
            rules_fire.sort(key=lambda r: (-r.priority, r.name))
            rule = rules_fire[0]
            self.facts.add(rule.consequent)
            self.trace.append({
                "rule": rule.name or "Unnamed rule",
                "antecedents": rule.antecedents,
                "derived": rule.consequent,
                "priority": rule.priority,
                "cf": getattr(rule, "cf", 1.0)
            })

    def conclusions(self) -> Dict[str, List[str]]:
        """TODO: Return separated results (recommendations, specs, other facts)."""
        recommendations, specs, other_facts = [], [], []
        for t in self.trace:
            cons = t.get("derived", "")
            if cons.startswith("recommend:"):
                recommendations.append(cons[len("recommend:"):].strip())
            elif cons.startswith("spec:"):
                specs.append(cons[len("spec:"):].strip())
            else:
                other_facts.append(cons.strip())

        return {
            "recommendations": recommendations,
            "specs": specs,
            "facts": sorted(self.facts),
            "other_facts": other_facts,
            "fired_rules": [t.get("rule", "") for t in self.trace]
        }
