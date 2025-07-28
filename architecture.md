# CNS Architecture Overview

## 🧠 Modular CNS Inspired by Evolution

The CNS is built from independently evolving modules, not monolithic computation.

### Core Components:

- **Memory Core**  
  - Uses reinforcement and decay algorithms to adjust memory weights over time.
  - Implements bounded memory volume to simulate energy-efficiency and prioritization.

- **Contradiction Loop**  
  - Detects conflicting beliefs or facts and tags them for re-evaluation.
  - May trigger overwrite, reinforcement, or branching based on synthetic salience.

- **Attention + Task Routing**  
  - Uses relevance scoring to route tasks through cortex (LLM) or local recall.
  - Temporal and task-based priors shape query formation.

- **LLM Cortex Interface**  
  - Stateless transformer queried with shaped, context-aware prompts.
  - CNS memory preconditions inputs; LLM does not own memory.

---

Architecture intentionally modular and interpretable. 
