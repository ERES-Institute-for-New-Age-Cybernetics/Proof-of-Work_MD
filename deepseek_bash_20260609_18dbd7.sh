# Run BERA alone (rating only)
python3 bera_rate.py

# Integrate with EAAP gate (uncomment bridge code)
python3 -c "
import eaap_proof as gate
from bera_rate import BERAGateBridge

bridge = BERAGateBridge(gate_module=gate)
# ... submit physiological data
"