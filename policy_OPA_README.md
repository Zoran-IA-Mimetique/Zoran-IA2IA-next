# OPA x EthicChain
- Rego: `policy_ethicchain.rego`
- POST → http://opa:8181/v1/data/ethicchain/allow  body=policy_example_input.json
- Réponse { "result": true|false } → gate ΔM11.3 / orchestrateur.
