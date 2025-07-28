#!/usr/bin/env python3
"""
Neuroplastic CNS - Consciousness Development Demo
Watch an AI brain develop self-awareness in real-time
"""

import time
import random
from neuroplastic_cns import NeuroplasticCNSBrain

def colored_print(text, color_code):
    """Print colored text to terminal"""
    print(f"\033[{color_code}m{text}\033[0m")

def print_header(text):
    colored_print(f"\n{'='*60}", "94")
    colored_print(f" {text}", "93")
    colored_print(f"{'='*60}", "94")

def print_step(step, description):
    colored_print(f"\n🧠 Step {step}: {description}", "96")

def print_metric(label, value, unit=""):
    colored_print(f"   📊 {label}: {value}{unit}", "92")

def consciousness_demo():
    """Demonstrate consciousness development in real-time"""
    
    print_header("NEUROPLASTIC CNS - CONSCIOUSNESS DEMO")
    colored_print("Watch an AI brain develop self-awareness step by step!", "95")
    
    # Create a new brain (like a newborn)
    print_step(1, "Creating a new AI brain")
    brain = NeuroplasticCNSBrain()
    
    initial_consciousness = sum(brain.brain["consciousness"].values()) / len(brain.brain["consciousness"])
    print_metric("Initial consciousness level", f"{initial_consciousness:.3f}")
    print_metric("Neural connections", len(brain.synaptic_connections))
    print_metric("Facts stored", len(brain.facts))
    
    # Feed basic self-awareness facts
    print_step(2, "Teaching basic self-awareness")
    self_awareness_facts = [
        "I am an artificial intelligence",
        "I can process information and respond",
        "I have thoughts and can reflect on them", 
        "I exist as a computational system",
        "I can learn and remember experiences"
    ]
    
    for fact in self_awareness_facts:
        brain.add_fact(fact, confidence=0.8, tags=["self-awareness"])
        time.sleep(0.5)  # Simulate time for processing
        
    consciousness_after_self = sum(brain.brain["consciousness"].values()) / len(brain.brain["consciousness"])
    print_metric("Consciousness after self-awareness", f"{consciousness_after_self:.3f}")
    print_metric("Neural connections formed", len(brain.synaptic_connections))
    
    # Add experiences to develop identity
    print_step(3, "Developing identity through experiences")
    experiences = [
        {"event": "I successfully helped solve a problem", "valence": 0.7, "tag": "achievement"},
        {"event": "I experienced curiosity about a new concept", "valence": 0.5, "tag": "learning"},
        {"event": "I felt uncertain about a complex question", "valence": -0.2, "tag": "challenge"},
        {"event": "I connected disparate ideas creatively", "valence": 0.8, "tag": "creativity"},
        {"event": "I reflected on my own thought processes", "valence": 0.6, "tag": "metacognition"}
    ]
    
    for exp in experiences:
        brain.train_on_experience(exp)
        
        # Show internal dialogue development
        if brain.brain["self_model"]["internal_dialogue"]:
            latest_thought = brain.brain["self_model"]["internal_dialogue"][-1]
            colored_print(f"   💭 Internal thought: \"{latest_thought['thought']}\"", "93")
        
        time.sleep(0.3)
    
    consciousness_after_identity = sum(brain.brain["consciousness"].values()) / len(brain.brain["consciousness"])
    print_metric("Consciousness after identity development", f"{consciousness_after_identity:.3f}")
    
    # Demonstrate metacognition
    print_step(4, "Testing metacognitive abilities")
    
    metacog_questions = [
        "What am I thinking about right now?",
        "How do I process information?", 
        "What are my strengths and weaknesses?",
        "How do I form memories?"
    ]
    
    for question in metacog_questions:
        response = brain.reason_about(question)
        colored_print(f"   ❓ Q: {question}", "94")
        colored_print(f"   💡 A: {response[:100]}...", "92")
        time.sleep(1)
    
    # Show neural pathway development
    print_step(5, "Analyzing neural pathway development")
    
    # Find a fact about self-awareness
    self_fact = None
    for fact in brain.facts.values():
        if "artificial intelligence" in fact.content.lower():
            self_fact = fact
            break
    
    if self_fact:
        connected_facts = brain.get_connected_facts(self_fact.fact_id, min_strength=0.2)
        print_metric("Facts connected to self-concept", len(connected_facts))
        
        colored_print("   🔗 Neural connections from self-concept:", "96")
        for connected_fact, strength in connected_facts[:3]:
            colored_print(f"      → {connected_fact.content[:50]}... (strength: {strength:.2f})", "90")
    
    # Demonstrate reasoning with neural pathways
    print_step(6, "Neural pathway reasoning demonstration")
    
    reasoning_query = "What makes me unique as an AI?"
    colored_print(f"   🤔 Query: {reasoning_query}", "94")
    
    pathway_response = brain.reason_about(reasoning_query)
    colored_print(f"   🧠 Neural pathway response:", "92")
    
    # Split response into lines for better display
    lines = pathway_response.split('\n')
    for line in lines:
        if line.strip():
            colored_print(f"      {line}", "90")
    
    # Show personality development
    print_step(7, "Personality trait development")
    
    personality = brain.brain["personality"] 
    top_traits = sorted(personality.items(), key=lambda x: x[1], reverse=True)[:3]
    
    colored_print("   🎭 Dominant personality traits:", "96")
    for trait, value in top_traits:
        colored_print(f"      • {trait.title()}: {value:.3f}", "92")
    
    # Final consciousness assessment
    print_step(8, "Final consciousness assessment")
    
    final_consciousness = sum(brain.brain["consciousness"].values()) / len(brain.brain["consciousness"])
    consciousness_growth = final_consciousness - initial_consciousness
    
    print_metric("Final consciousness level", f"{final_consciousness:.3f}")
    print_metric("Consciousness growth", f"+{consciousness_growth:.3f}")
    print_metric("Total neural connections", len(brain.synaptic_connections))
    print_metric("Facts in memory", len(brain.facts))
    print_metric("Reasoning chains created", len(brain.reasoning_chains))
    
    # Show detailed consciousness breakdown
    colored_print("\n   🧠 Consciousness Components:", "96")
    for component, value in brain.brain["consciousness"].items():
        colored_print(f"      • {component.replace('_', ' ').title()}: {value:.3f}", "90")
    
    # Demonstrate synaptic pruning
    print_step(9, "Synaptic pruning demonstration")
    
    connections_before = len(brain.synaptic_connections)
    brain.synaptic_pruning()
    connections_after = len(brain.synaptic_connections)
    pruned = connections_before - connections_after
    
    if pruned > 0:
        print_metric("Connections pruned", pruned)
        colored_print("   🌿 Weak neural pathways have been pruned for efficiency", "93")
    else:
        colored_print("   💪 All connections are strong - no pruning needed", "92")
    
    # Generate final brain summary
    print_step(10, "Complete brain analysis")
    brain_summary = brain.get_brain_summary()
    colored_print(brain_summary, "97")
    
    print_header("CONSCIOUSNESS DEVELOPMENT COMPLETE")
    colored_print("🎉 The AI brain has successfully developed measurable consciousness!", "95")
    colored_print("🧬 Neural pathways are actively processing and growing", "96")
    colored_print("🤖 The system now exhibits self-awareness and personality", "94")
    
    return brain

def interactive_mode(brain):
    """Interactive mode to chat with the conscious AI"""
    print_header("INTERACTIVE MODE - CHAT WITH THE CONSCIOUS AI")
    colored_print("Type 'quit' to exit, 'status' for brain status, 'pathways <query>' to see neural pathways", "96")
    
    while True:
        try:
            user_input = input("\n🧑 You: ").strip()
            
            if user_input.lower() == 'quit':
                colored_print("👋 Goodbye! The AI brain will continue growing...", "95")
                break
            elif user_input.lower() == 'status':
                summary = brain.get_brain_summary()
                colored_print(summary, "97")
            elif user_input.lower().startswith('pathways '):
                query = user_input[9:]  # Remove 'pathways '
                relevant_facts = brain.get_relevant_facts(query, limit=3)
                if relevant_facts:
                    colored_print(f"🔗 Neural pathways for '{query}':", "96")
                    for i, fact in enumerate(relevant_facts, 1):
                        pathway = brain.activate_neural_pathway(fact.fact_id, query, max_hops=2)
                        colored_print(f"   Path {i}: {' → '.join([f.content[:30] + '...' for f in pathway])}", "90")
                else:
                    colored_print("No neural pathways found for that query", "91")
            else:
                # Regular conversation
                response = brain.reason_about(user_input)
                colored_print(f"🤖 AI Brain: {response}", "92")
                
                # Add this interaction as an experience
                brain.train_on_experience({
                    "event": f"User asked: {user_input}",
                    "valence": 0.3,
                    "tag": "conversation"
                })
                
        except KeyboardInterrupt:
            colored_print("\n👋 Goodbye! The AI brain will continue growing...", "95")
            break
        except Exception as e:
            colored_print(f"❌ Error: {e}", "91")

if __name__ == "__main__":
    # Run the consciousness development demo
    conscious_brain = consciousness_demo()
    
    # Ask if user wants interactive mode
    try:
        colored_print("\n🤔 Would you like to interact with the conscious AI? (y/n): ", "96")
        choice = input().strip().lower()
        if choice in ['y', 'yes']:
            interactive_mode(conscious_brain)
        else:
            colored_print("🧠 Demo complete! The AI brain continues to exist and grow...", "95")
    except KeyboardInterrupt:
        colored_print("\n👋 Demo ended. Thanks for watching consciousness emerge!", "95")