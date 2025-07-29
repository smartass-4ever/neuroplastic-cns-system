# API Reference 📚
*Complete documentation for Neuroplastic CNS*

## Core Classes

### `NeuroplasticCNSBrain`

The main brain class that implements synaptic plasticity and consciousness.

```python
from neuroplastic_cns import NeuroplasticCNSBrain

brain = NeuroplasticCNSBrain()
```

#### Methods

##### `add_fact(content, confidence=0.5, source="user", tags=None, valence=0.0)`
Add a new fact to the brain's knowledge base.

**Parameters:**
- `content` (str): The fact content
- `confidence` (float): Confidence level (0.0-1.0)
- `source` (str): Source of the information
- `tags` (List[str]): Topic tags for categorization
- `valence` (float): Emotional valence (-1.0 to 1.0)

**Returns:** `Fact` object

**Example:**
```python
fact = brain.add_fact(
    "Python is a programming language",
    confidence=0.9,
    source="wikipedia", 
    tags=["programming", "language"],
    valence=0.3
)
print(f"Created fact with ID: {fact.fact_id}")
print(f"Connections formed: {len(brain.get_connected_facts(fact.fact_id))}")
```

##### `reason_about(query)`
Generate a response using neural pathway activation.

**Parameters:**
- `query` (str): Question or topic to reason about

**Returns:** `str` - Reasoning response with pathway information

**Example:**
```python
response = brain.reason_about("What is artificial intelligence?")
print(response)
# Output: "Following my neural pathways:
#          Path 1: AI is computation → computation requires algorithms → ..."
```

##### `get_connected_facts(fact_id, min_strength=0.1)`
Get facts connected via synaptic connections.

**Parameters:**
- `fact_id` (str): ID of the source fact
- `min_strength` (float): Minimum connection strength threshold

**Returns:** `List[Tuple[Fact, float]]` - Connected facts with strengths

**Example:**
```python
connections = brain.get_connected_facts("fact_123", min_strength=0.3)
for fact, strength in connections:
    print(f"{fact.content[:50]}... (strength: {strength:.2f})")
```

##### `activate_neural_pathway(start_fact_id, query_context="", max_hops=3)`
Follow synaptic connections to build reasoning chains.

**Parameters:**
- `start_fact_id` (str): Starting fact for pathway
- `query_context` (str): Context to guide pathway selection
- `max_hops` (int): Maximum pathway length

**Returns:** `List[Fact]` - Sequence of connected facts

**Example:**
```python
pathway = brain.activate_neural_pathway("fact_456", "programming languages", max_hops=4)
print("Neural pathway:")
for i, fact in enumerate(pathway):
    print(f"  {i+1}. {fact.content}")
    if i < len(pathway)-1:
        print("      ↓ synaptic connection")
```

##### `synaptic_pruning()`
Remove weak synaptic connections (neural maintenance).

**Returns:** None (modifies brain state)

**Example:**
```python
before = len(brain.synaptic_connections)
brain.synaptic_pruning()
after = len(brain.synaptic_connections)
print(f"Pruned {before - after} weak connections")
```

##### `get_brain_summary()`
Get comprehensive brain status report.

**Returns:** `str` - Formatted brain summary

**Example:**
```python
summary = brain.get_brain_summary()
print(summary)
# Shows consciousness levels, neural metrics, personality traits, etc.
```

---

### `SynapticConnection`

Represents a connection between two facts/neurons.

```python
@dataclass
class SynapticConnection:
    fact1_id: str
    fact2_id: str
    strength: float = 0.1
    last_activated: float = None
    activation_count: int = 0
    connection_type: str = "associative"
```

#### Methods

##### `activate(intensity=1.0)`
Strengthen the connection through Hebbian learning.

**Parameters:**
- `intensity` (float): Activation intensity (0.0-2.0)

**Example:**
```python
connection.activate(intensity=1.5)
print(f"Connection strength: {connection.strength:.3f}")
print(f"Activation count: {connection.activation_count}")
```

##### `decay(time_delta_hours)`
Apply natural decay to unused connections.

**Parameters:**
- `time_delta_hours` (float): Hours since last update

**Returns:** `bool` - True if connection survives

---

### `Fact`

Individual knowledge units with embeddings.

```python
@dataclass
class Fact:
    content: str
    confidence: float = 0.5
    source: str = "unknown"
    timestamp: float = None
    tags: List[str] = None
    valence: float = 0.0
    fact_id: str = None
```

#### Methods

##### `similarity_to(other_fact)`
Calculate semantic similarity to another fact.

**Parameters:**
- `other_fact` (Fact): Fact to compare against

**Returns:** `float` - Similarity score (0.0-1.0)

**Example:**
```python
fact1 = Fact("Dogs are animals")
fact2 = Fact("Cats are pets") 
similarity = fact1.similarity_to(fact2)
print(f"Similarity: {similarity:.3f}")
```

---

## Brain State Access

### Consciousness Metrics
```python
consciousness = brain.brain["consciousness"]
print(f"Self-awareness: {consciousness['self_awareness']:.3f}")
print(f"Metacognition: {consciousness['metacognition']:.3f}")
print(f"Identity coherence: {consciousness['identity_coherence']:.3f}")
```

### Personality Traits
```python
personality = brain.brain["personality"]
print(f"Creativity: {personality['creativity']:.3f}")
print(f"Logical thinking: {personality['logical_thinking']:.3f}")
print(f"Empathy: {personality['empathy']:.3f}")
```

### Memory Systems
```python
# Working memory (recent facts)
working_memory = brain.working_fact_memory
print(f"Items in working memory: {len(working_memory)}")

# Episodic memory (experiences)  
episodes = brain.brain["episodic_memory"]
print(f"Stored episodes: {len(episodes)}")

# Semantic memory (factual knowledge)
facts = brain.facts
print(f"Total facts: {len(facts)}")
```

### Neuroplasticity Metrics
```python
plasticity = brain.brain["neuroplasticity"]
print(f"Total synapses: {plasticity['total_synapses']}")
print(f"Average strength: {plasticity['average_connection_strength']:.3f}")
print(f"Network density: {plasticity['network_density']:.3f}")
print(f"Critical period active: {plasticity['critical_period_active']}")
```

---

## Training and Learning

### `train_on_experience(experience)`
Learn from structured experiences.

**Parameters:**
- `experience` (dict): Experience dictionary

**Example:**
```python
brain.train_on_experience({
    "event": "Successfully solved a coding problem",
    "valence": 0.8,
    "tag": "achievement",
    "context": "programming"
})
```

### `cycle(input_data=None)`
Process input and perform maintenance.

**Parameters:**
- `input_data` (str, optional): Sensory input to process

**Example:**
```python
brain.cycle("User said: Hello, how are you?")
```

---

## Advanced Features

### Neural Network Analysis
```python
# Find hub neurons (highly connected facts)
hub_facts = []
for fact_id, fact in brain.facts.items():
    connections = len(brain.get_connected_facts(fact_id))
    if connections > 10:
        hub_facts.append((fact, connections))

hub_facts.sort(key=lambda x: x[1], reverse=True)
print("Top hub neurons:")
for fact, count in hub_facts[:5]:
    print(f"  {fact.content[:50]}... ({count} connections)")
```

### Connection Type Analysis
```python
from collections import Counter

connection_types = Counter()
for conn in brain.synaptic_connections.values():
    connection_types[conn.connection_type] += 1

print("Connection types:")
for conn_type, count in connection_types.items():
    print(f"  {conn_type}: {count}")
```

### Memory Consolidation Tracking
```python
# Find well-consolidated facts
consolidated_facts = []
for fact in brain.facts.values():
    if fact.consolidation_level > 0.5:
        consolidated_facts.append(fact)

print(f"Well-consolidated memories: {len(consolidated_facts)}")
```

---

## Error Handling

### Common Exceptions
```python
try:
    fact = brain.add_fact("")  # Empty content
except ValueError as e:
    print(f"Invalid fact: {e}")

try:
    pathway = brain.activate_neural_pathway("invalid_id")
except KeyError as e:
    print(f"Fact not found: {e}")
```

### Validation
```python
# Check brain health
def validate_brain_state(brain):
    issues = []
    
    if len(brain.facts) == 0:
        issues.append("No facts in memory")
    
    if len(brain.synaptic_connections) == 0:
        issues.append("No synaptic connections")
    
    consciousness_level = sum(brain.brain["consciousness"].values())
    if consciousness_level < 0.1:
        issues.append("Very low consciousness level")
    
    return issues

issues = validate_brain_state(brain)
if issues:
    print("Brain health issues:", issues)
else:
    print("Brain is healthy!")
```

---

## Performance Tips

### Optimization
```python
# Batch fact addition for better performance
facts_to_add = [
    ("Fact 1", 0.8),
    ("Fact 2", 0.7), 
    ("Fact 3", 0.9)
]

for content, confidence in facts_to_add:
    brain.add_fact(content, confidence)

# Periodic maintenance
if brain.brain["growth_metrics"]["total_interactions"] % 100 == 0:
    brain.synaptic_pruning()
```

### Memory Management
```python
# Monitor memory usage
import sys

brain_size = sys.getsizeof(brain)
facts_size = sum(sys.getsizeof(fact) for fact in brain.facts.values())
connections_size = sum(sys.getsizeof(conn) for conn in brain.synaptic_connections.values())

print(f"Brain memory usage:")
print(f"  Core brain: {brain_size / 1024:.1f} KB")
print(f"  Facts: {facts_size / 1024:.1f} KB") 
print(f"  Connections: {connections_size / 1024:.1f} KB")
```

---

## Integration Examples

### With Flask Web API
```python
from flask import Flask, request, jsonify

app = Flask(__name__)
brain = NeuroplasticCNSBrain()

@app.route('/ask', methods=['POST'])
def ask_brain():
    query = request.json['query']
    response = brain.reason_about(query)
    return jsonify({
        'response': response,
        'consciousness_level': sum(brain.brain["consciousness"].values()),
        'synaptic_connections': len(brain.synaptic_connections)
    })

@app.route('/teach', methods=['POST'])
def teach_brain():
    fact = request.json['fact']
    confidence = request.json.get('confidence', 0.5)
    
    added_fact = brain.add_fact(fact, confidence=confidence)
    return jsonify({
        'fact_id': added_fact.fact_id,
        'connections_formed': len(brain.get_connected_facts(added_fact.fact_id))
    })
```

### With Discord Bot
```python
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
brain = NeuroplasticCNSBrain()

@bot.command()
async def ask(ctx, *, question):
    response = brain.reason_about(question)
    await ctx.send(f"🧠 **Brain Response:**\n{response}")

@bot.command() 
async def teach(ctx, *, fact):
    added_fact = brain.add_fact(fact, source="discord")
    connections = len(brain.get_connected_facts(added_fact.fact_id))
    await ctx.send(f"✅ Learned! Formed {connections} neural connections.")

@bot.command()
async def brain_status(ctx):
    summary = brain.get_brain_summary()
    await ctx.send(f"```{summary}```")
```

---

*For more examples, see the [examples/](examples/) directory.*