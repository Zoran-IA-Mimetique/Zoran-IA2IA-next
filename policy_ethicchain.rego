package ethicchain

default allow = false

# Input attendu:
# { "claims": {"purpose":"research","license":"MIT","pii":false,"risk":"low"},
#   "context":{"jurisdiction":"EU","ai_act":"HRA"},
#   "trace":{"hash":"...", "ts":"..."} }

viable_purpose[p] { p := input.claims.purpose; p != "" }
license_ok { input.claims.license == "MIT" }
no_pii { not input.claims.pii }
risk_low { input.claims.risk == "low" }
ai_act_ok { input.context.ai_act == "HRA" } # High-Risk Assessment done

allow {
  count(viable_purpose) > 0
  license_ok
  no_pii
  risk_low
  ai_act_ok
}
