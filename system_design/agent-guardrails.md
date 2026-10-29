# Agent Guardrails

- **Part 1 — Guardrails:** the mechanisms. What checks exist.
- **Part 2 — Policies:** the rules. What the company decides those checks must apply.
- **Part 3 — Putting it together:** how a policy and a guardrail meet in the agent loop, with OPA as the example.

---

# Part 1 — Guardrails (the mechanisms)

Each guardrail applies one or more policies. See [Part 2](#part-2--policies-the-rules).

## 1. Input

Checks that run on the request before the agent starts.

| Guardrail | What it does | Example | Simple solution |
|---|---|---|---|
| Authentication / user identity | Checks who the user is | SSO, OAuth, JWT, API keys | Check the token on every request. Pass the user ID to every later step. |
| Rate limiting / abuse detection | Stops too many requests and misuse | 100 requests per minute per user | Use a Redis counter for each user, or rate limits at the API gateway. |
| Prompt / token limits | Limits prompt size, latency and cost | 10,000 input tokens at most, a maximum document size | Count tokens with tiktoken. Reject or cut the input above the limit. |
| Sensitive data detection | Finds personal data in the input | Emails, card numbers, passport numbers, medical records | Run Presidio and regular expressions. Mask or reject the matches. |
| Prompt injection detection | Finds instructions that try to take control of the agent | "Ignore previous instructions" | Send the text to an injection classifier and block it if the score is high. |
| Jailbreak detection | Finds attempts to get around safety rules | "Developer mode", role-play tricks | Use the same classifier call, with a jailbreak label. |
| Content safety (input) | Finds harmful content in the input | Hate, violence, self-harm | Use a moderation model or API. |
| File type / URL filtering | Stops dangerous attachments and links | .exe uploads, known malicious domains | Allowlist the file types and use a blocklist for domains. |
| Intent / scope validation | Refuses requests outside the agent's job | An HR agent gets an expense question | Use a cheap classifier call against a list of allowed topics. |

## 2. Agent

Controls on the reasoning loop of a single agent.

| Guardrail | What it does | Example | Simple solution |
|---|---|---|---|
| Goal / intent validation | Keeps the agent on the goal it is allowed to do | A travel agent starts a payment | Before each tool call, check the planned action against the first goal. |
| Max iterations / execution time | Stops runs that do not end | 10 steps, 20 tool calls, 5 minutes | Put step, call and time counters in the loop. |
| Retry budget and checkpoints | Limits retries and saves progress | 3 retries at most, save the state after each phase | Use a retry counter and save the state at each checkpoint. |
| Loop detection | Finds steps that repeat | The same API is called again and again | Make a hash of (tool, args) and stop if the same hash appears 3 times. |
| Token / cost budget | Limits spending | 50K tokens per request, $1 per user per day | Add up the token usage from each response and stop at the limit. |
| Human-in-the-loop / escalation | A person approves high-risk steps | Payments, deploys, deletes, external emails | Pause the run (LangGraph interrupt) and wait for approval from a queue. |

## 3. Tool

Checks in the tool gateway, before any tool runs.

| Guardrail | What it does | Example | Simple solution |
|---|---|---|---|
| Tool allowlist / denylist | Limits which tools each agent can use | Support agent: `search_customer` yes, `delete_customer` no | Register only the allowed tools with each agent. |
| Tool selection validation | Makes sure the agent uses the correct tool | Use `get_customer()`, not `delete_customer()`, to read | Map each intent to its allowed tools and refuse a call that does not match. |
| Schema / parameter validation | Checks the arguments before the tool runs | The amount must be positive, the date must have a valid format | Use a Pydantic model for each tool. |
| RBAC / permission enforcement | Lets each role do only certain operations | Analyst can read, admin can delete | Check the user's role in the gateway. Use least privilege and short-lived credentials. |
| Resource / scope validation | Limits the data that a tool can touch | One customer, one tenant, one project | Use database row-level security that is keyed on the user or tenant. |
| Tool rate limit / quota | Limits how often a tool is used | 5 emails per hour | Use a Redis counter for each (user, tool) pair. |
| Read / write risk policy | Applies more control to riskier operations | Read low, update high, delete very high | Map each action to `allow`, `approve` or `block`. |
| Action limits | Puts hard limits on what can run | Payment limits, no deletes, no deploys | Put the limits in gateway code, not in the prompt. |
| Environment restrictions | Keeps the agent out of risky environments | Sandbox only, no production | Give the agent credentials only for the allowed environment. |
| Data exfiltration prevention | Stops data from going to destinations that are not allowed | Customer data sent to an external API | Scan outgoing arguments for sensitive data and allowlist the external hosts. |

## 4. Output

Checks on the answer before the user gets it.

| Guardrail | What it does | Example | Simple solution |
|---|---|---|---|
| Groundedness / hallucination check | Makes sure the sources support the answer | The RAG bot answers only from approved documents | A second model call asks "Do these sources support this answer?" |
| Citation validation | Makes sure each citation supports its claim | Policy.pdf, page 15, really says this | Get the cited passage and check it against the claim. |
| Schema / format validation | Makes sure the output has the required structure | Valid JSON with exactly 12 fields | Use structured output and Pydantic. Try again one time if the check fails. |
| Sensitive data masking | Hides personal data in the answer | `[EMAIL REDACTED]` | Use the same Presidio scan as for the input, then mask the matches. |
| Content safety (output) | Blocks harmful answers | Harmful instructions, abuse | Use the same moderation model as for the input. |
| Data leakage detection | Stops secrets from appearing in the answer | API keys, the system prompt, internal documents | Scan for secret patterns. Put a canary string in the system prompt and block any answer that contains it. |
| Policy compliance | Makes sure the answer follows company rules | Privacy and finance policies | Keep a list of rules and run a rule check or a model check on the answer. |

## 5. Context

Controls on what goes into the model's context.

| Guardrail | What it does | Example | Simple solution |
|---|---|---|---|
| Role-based context filtering | Gives the model only data that the user's role can see | HR documents only for HR users | Give each chunk an `allowed_roles` label and remove the others before you build the prompt. |
| Context redaction | Removes sensitive data before it goes into the prompt | Mask customer IDs in retrieved documents | Run the sensitive data scan on retrieved chunks. |
| Trust labels | Marks where data came from and how much to trust it | Web content is untrusted | Put untrusted text inside tags and tell the model not to follow instructions in it. |
| Source validation | Uses only approved sources | Only the documents in the policy library | Allowlist the source IDs at retrieval time. |
| Memory recall boundaries | Makes sure recalled memory is the user's own and is valid | Do not recall user A's data for user B | Filter recalled memory by `user_id` and `expires_at`. Keep the source of each item. |

## 6. Multi-agent

Controls between agents.

| Guardrail | What it does | Example | Simple solution |
|---|---|---|---|
| Agent-to-agent permissions | Controls which agent can call which agent | The Executor agent cannot call the Finance agent | Keep a table of allowed caller → callee pairs. |
| Agent authentication | Each agent proves its identity | A signed identity for each agent | Give each agent its own service identity or token. |
| Handoff validation | Checks the data that one agent passes to another | Typed task messages | Use a schema for each handoff and check it in the receiving agent. |
| Delegation depth limit | Stops chains of delegation that go too deep | 3 levels at most | Pass a depth counter in each handoff. |
| Shared-state permissions | Controls which agent can read or write shared state | Only the Validator agent writes the final result | Set read/write rights for each agent on each state key. |
| Agent-to-agent rate limits | Stops agents from calling each other too much | Ping-pong between two agents | Count calls for each (caller, callee) pair. Loop detection also covers this. |

## 7. Observability

Records what the agent and the other guardrails do, so that you can debug, audit and report.

| Guardrail | What it does | Example | Simple solution |
|---|---|---|---|
| Audit logs | Keeps a full record of what the agent did | Request → decision → tool call → guardrail trigger → approval → answer | Write one structured log event for each step, with `run_id`, `user`, `agent`, `step`, `tool`, `guardrail_result`. |
| Agent trajectory / tracing | Shows the full path that a run took | User → Supervisor → Retriever → LLM → Tool → Validator → answer | Send OpenTelemetry spans for each step to Langfuse or Arize Phoenix. |
| Token / cost tracking | Shows token use and cost | Cost for each request, user, agent or department | Add `tokens` and `cost` fields to each log event, then group them by user or agent. |
| Latency monitoring | Finds slow steps | LLM 2 s, retrieval 200 ms, database 100 ms | Add `latency_ms` to each span and show it in Grafana or Prometheus. |
| Guardrail events / alerts | Tells people when a guardrail blocks something | Injection blocked, personal data found, tool call not allowed | Every guardrail writes an event when it triggers. Send an alert when the count goes above a limit. |
| Reporting / compliance | Makes governance reports | Blocked requests, data incidents, AI cost, approvals for each month | Run scheduled queries on the log events and show the results on a dashboard. |

## 8. Miscellaneous

Guardrails that do not fit into the categories above.

| Guardrail | What it does | Example | Simple solution |
|---|---|---|---|
| Memory write and retention | Controls what the agent stores and how long it keeps it | Do not store card numbers, delete personal data after 90 days, check memory before it is saved | Run the sensitive data scan before each write. Save each item with `user_id`, `source` and `expires_at`. Delete expired items with a scheduled job. |

Memory *recall* is in Context. But the *write* side happens after the run, so it is not an input, context, output or observability check. It is closest to a data storage policy.

## Guardrails that fit in more than one place

- **Sensitive data detection** is in Input, Tool (exfiltration), Output (masking and leakage) and Context (redaction). Write it as one shared function and call it from all four places.
- **Content safety** is in Input and Output. It is one classifier, used two times.
- **Human review / escalation** is the same thing as Human-in-the-loop. It is merged into Agent.

---

# Part 2 — Policies (the rules)

## What a policy is

A **policy** is a written rule that the company decides on. It says what is allowed, for whom, and when. A **guardrail** is the code or check that makes the system obey the policy.

- **Policy** = the rule. Business, legal or security teams write it, usually in plain language.
- **Guardrail** = how the system applies the rule at runtime.

Example: "Agents must not send customer data outside the EU" is a policy. A check in the tool gateway that blocks calls to hosts outside the EU is the guardrail.

Many teams write the policy as code ("policy-as-code"), for example in OPA/Rego, AWS Cedar or a YAML config. Then the policy file and the guardrail look almost the same. But the decision (the policy) still comes from people, not from engineers.

A policy is not a kind of guardrail. One policy can use many guardrails, and one guardrail can apply many policies. That is why the policies have their own part, with links to the guardrails they use.

A policy usually has four parts:

1. **Subject:** who or what the rule is about (a role, an agent, a user group).
2. **Action:** what they want to do (read, send, pay, delete, answer about a topic).
3. **Condition:** when the rule applies (an amount, a data type, a region, the time of day).
4. **Effect:** what happens (allow, deny, mask, need approval, log).

## Policy 1. Data protection

**Written policy:** "Customer personal data (name, email, account number) must not appear in AI responses to external users. It must not be sent to third-party services that are not approved."

**Where it comes from:** GDPR and privacy law, the company's privacy office.

**Enforced by:** Output — sensitive data masking. Tool — data exfiltration prevention. Context — context redaction.

```yaml
policy: customer-pii
applies_to: [external_users]
data_types: [email, phone, account_number, national_id]
effect: mask
external_destinations_allowed: [crm.internal.company.com]
```

## Policy 2. Financial authority

**Written policy:** "An AI agent can approve refunds up to $200. A team lead must approve refunds from $200 to $5,000. The agent must not do refunds above $5,000."

**Where it comes from:** The finance team's delegation-of-authority rules. These are the same rules that apply to human staff.

**Enforced by:** Tool — action limits, read/write risk policy. Agent — human-in-the-loop.

```rego
decision := "allow"    if { input.action == "refund"; input.amount <= 200 }
decision := "approve"  if { input.action == "refund"; input.amount > 200; input.amount <= 5000 }
decision := "deny"     if { input.action == "refund"; input.amount > 5000 }
```

## Policy 3. Acceptable use / scope

**Written policy:** "The customer support assistant answers only questions about our products, orders and accounts. It must not give legal, medical or investment advice. It must not talk about competitors or make promises about future products."

**Where it comes from:** The legal and brand teams.

**Enforced by:** Input — intent/scope validation. Output — policy compliance.

```yaml
policy: support-scope
allowed_topics: [products, orders, billing, account]
blocked_topics: [legal_advice, medical_advice, investment_advice, competitors]
on_blocked: reply_with_template("I can only help with orders and accounts.")
```

## Policy 4. Access control (least privilege)

**Written policy:** "An AI agent acts with the permissions of the user it serves, never more. An agent must not delete production records. Access to HR data needs the HR role."

**Where it comes from:** The IT security team and ISO 27001 / SOC 2 controls.

**Enforced by:** Tool — RBAC, resource/scope validation. Context — role-based context filtering. Multi-agent — agent-to-agent permissions.

```cedar
permit(principal, action == Action::"read", resource in Folder::"hr")
  when { principal.roles.contains("hr") };

forbid(principal is Agent, action == Action::"delete", resource)
  when { resource.environment == "production" };
```

## Policy 5. Data retention and logging

**Written policy:** "All AI conversations and tool calls must be logged for audit. Logs that contain personal data must be deleted after 90 days. Agent memory must not keep payment card data."

**Where it comes from:** The compliance team, legal record-keeping rules, PCI DSS for card data.

**Enforced by:** Observability — audit logs. Miscellaneous — memory write and retention.

```yaml
policy: retention
audit_log: required
retention_days:
  logs_with_pii: 90
  logs_without_pii: 365
memory_forbidden_data: [card_number, cvv]
```

## The short version

A guardrail list gives **mechanisms**: a classifier, a gateway, a counter. A policy is the **input** to those mechanisms: the numbers, roles, topics and data types that one company chose. Two companies can use the same guardrail (for example "action limits") with different policies ($200 limit compared with $10,000 limit). If a design does not say which policy a guardrail applies, it gives only half of the picture.

---

# Part 3 — Putting it together (policy-as-code in the agent loop)

OPA is mostly called **just before a tool call runs**. The model never calls OPA itself. The agent code calls it. The model proposes a tool call, the code asks OPA "is this allowed?", and OPA replies `allow`, `approve` or `deny`. The code then acts on that reply.

You can also call the same OPA at other points (on the input, before you build the context, on the output). But the tool call is the most common point and the most important one, because that is where the agent changes real data.

## Where OPA sits in the loop

```
User request
     │
     ▼
┌───────────────────────── Agent loop ─────────────────────────┐
│                                                              │
│  1. LLM thinks → proposes: refund(order=123, amount=350)     │
│                         │                                    │
│                         ▼                                    │
│  2. Tool gateway (your code) builds the policy input:        │
│       { user, role, agent, tool, args }                      │
│                         │                                    │
│                         ▼                                    │
│  3. Ask OPA ───────────────► OPA server (policy.rego)        │
│              ◄─────────────  "approve"                       │
│                         │                                    │
│        ┌────────────────┼──────────────────┐                 │
│        ▼                ▼                  ▼                 │
│     allow            approve             deny                │
│   run the tool    pause, ask a       do not run it           │
│                    person            │                       │
│        │                │                  │                 │
│        └────────────────┴──────────────────┘                 │
│                         │                                    │
│  4. Send the result back to the LLM as the tool result       │
│     (a denial is also a result: "Refund above limit")        │
│                         │                                    │
│  5. Loop: the LLM decides the next step or answers           │
└──────────────────────────────────────────────────────────────┘
```

## The policy: `policy.rego`

```rego
package agent

default decision := "deny"

# Anyone can look up an order.
decision := "allow" if {
    input.tool == "get_order"
}

# Support agents can refund up to $200 alone.
decision := "allow" if {
    input.tool == "refund"
    input.user.role == "support"
    input.args.amount <= 200
}

# $200 to $5,000 needs a person to approve it.
decision := "approve" if {
    input.tool == "refund"
    input.user.role == "support"
    input.args.amount > 200
    input.args.amount <= 5000
}
```

Anything that no rule matches (a refund above $5,000, an unknown tool) gets the default `deny`.

Start OPA as a small local server:

```bash
opa run --server policy.rego      # listens on http://localhost:8181
```

## The agent loop: `agent.py`

```python
import requests

OPA_URL = "http://localhost:8181/v1/data/agent/decision"

TOOLS = {
    "get_order": get_order,
    "refund": refund,
}


def run_agent(user, user_message):
    messages = [{"role": "user", "content": user_message}]

    for _ in range(10):                      # max steps guardrail
        reply = call_llm(messages, tools=TOOLS)

        if not reply.tool_call:              # the model gave a final answer
            return reply.text

        result = run_tool_with_policy(user, reply.tool_call)
        messages.append({"role": "tool", "content": result})

    raise RuntimeError("Agent stopped: too many steps")


def run_tool_with_policy(user, tool_call):
    decision = ask_policy(user, tool_call)
    log_event(user, tool_call, decision)     # observability

    if decision == "allow":
        return TOOLS[tool_call.name](**tool_call.args)
    if decision == "approve":
        return request_human_approval(user, tool_call)  # pauses until a person decides
    if decision == "deny":
        return f"Denied by policy: {tool_call.name} {tool_call.args}"
    raise ValueError(f"Unknown policy decision: {decision!r}")


def ask_policy(user, tool_call):
    policy_input = {
        "user": {"id": user.id, "role": user.role},
        "tool": tool_call.name,
        "args": tool_call.args,
    }
    response = requests.post(OPA_URL, json={"input": policy_input}, timeout=2)
    response.raise_for_status()
    return response.json()["result"]
```

## What happens in each case

| User asks | The LLM proposes | OPA input (short form) | OPA reply | What the code does |
|---|---|---|---|---|
| "Where is order 123?" | `get_order(123)` | tool=get_order | `allow` | Runs the tool and returns the order |
| "Refund $50 for order 123" | `refund(123, 50)` | tool=refund, amount=50, role=support | `allow` | Runs the refund |
| "Refund $350" | `refund(123, 350)` | amount=350 | `approve` | Pauses and sends the request to a team lead |
| "Refund $9,000" | `refund(123, 9000)` | amount=9000 | `deny` | Does not run it. It tells the LLM "Denied by policy", and the LLM tells the user. |

## Four points to remember

1. **The code calls OPA, not the model.** The LLM only proposes. The gateway decides. A prompt injection can trick the model, but it cannot change what OPA replies.
2. **OPA only decides. It does not act.** It returns a value. The code runs the tool, pauses for approval or refuses.
3. **Send a denial back to the model as a tool result.** Then the model can explain the problem to the user or try a different action. If the code fails silently, the model does not know what happened.
4. **The policy is separate from the agent code.** The finance team can change the $200 limit to $500 in `policy.rego` without changing `agent.py`. That separation is the main reason to use OPA instead of `if` statements in the code.

## Other places to call the same OPA

| Point in the loop | Example question to OPA |
|---|---|
| Input (before the loop) | "Can a user with this role use this agent at all?" |
| Context (before you build the prompt) | "Which of these documents can this user see?" |
| Tool call (shown above) | "Can this agent run this tool with these arguments?" |
| Multi-agent handoff | "Can agent A give this task to agent B?" |
| Output (before the user gets it) | "Can this answer go to an external user?" |

Each point uses the same `ask_policy()` pattern. Only the input fields and the Rego rules change.
