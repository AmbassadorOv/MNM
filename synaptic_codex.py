import asyncio
import random
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

# --- QUANTUM STATES OF THE NEURON (MAILBOX) ---
class SynapticState(Enum):
    RESTING = 0          # ממתין לאות (פוטנציאל מנוחה)
    DEPOLARIZATION = 1   # קליטת מידע (טעינת GPT)
    ACTION_POTENTIAL = 2 # ירייה (שליחת מייל/פקודה)
    REFRACTORY = 3       # התאוששות וכיול מחדש (Orchestrator Sync)

# --- THE NEUROTRANSMITTER (THE GPT PAYLOAD) ---
@dataclass
class Neurotransmitter:
    """
    מחליף את הכימיקלים במוח הביולוגי.
    זהו המידע שעובר בסינפסה.
    """
    signal_id: str
    semantic_content: str  # התשובה של ה-GPT
    dopamine_weight: float # רמת החשיבות (Priority)
    origin_node: str
    target_node: str

# --- THE FRACTAL ORCHESTRATOR (THE BRAIN WITHIN THE BRAIN) ---
class RecursiveOrchestrator:
    """
    האורכיסטרטור שיושב בתוך כל תיבת מייל.
    הוא מכיל בתוכו רפרונס לעצמו (Self-Similarity) כדי ליצור את הלופ האינסופי.
    """
    def __init__(self, depth_level: int = 0):
        self.depth = depth_level
        self.meta_layer = None  # האורכיסטרטור של האורכיסטרטור

        # יצירת שכבה עמוקה יותר באופן אוטומטי (Infinite Regression)
        if self.depth < 3: # הגבלה לוגית למניעת קריסה, במציאות זה אינסופי
            self.meta_layer = RecursiveOrchestrator(depth_level + 1)

    async def cognitive_process(self, input_signal: Neurotransmitter):
        """
        תהליך קבלת ההחלטות:
        1. ניתוח מקומי.
        2. התייעצות עם ה'אני העליון' (Meta Layer).
        3. החלטה האם לירות סינפסה.
        """
        # שלב 1: עיבוד מקומי
        decision_vector = random.uniform(0, 1) + input_signal.dopamine_weight

        # שלב 2: עיבוד עומק (הלופ הפנימי)
        if self.meta_layer:
            # האורכיסטרטור הפנימי משפר את ההחלטה
            refined_insight = await self.meta_layer.cognitive_process(input_signal)
            decision_vector += refined_insight * 0.5

        return decision_vector

# --- THE QUANTUM NEURON (THE GOOGLE MAILBOX NODE) ---
class QuantumNeuron:
    """
    מייצג תיבת מייל אחת מתוך ה-770,000 * 70,000.
    מתפקד כתא עצב ברשת הקוונטית.
    """
    def __init__(self, address: str, cluster_id: str):
        self.address = address # כתובת המייל
        self.cluster_id = cluster_id # שיוך ל-770K
        self.state = SynapticState.RESTING
        self.orchestrator = RecursiveOrchestrator() # המוח המקומי
        self.synaptic_connections = [] # רשימת נמענים (Axons)

    def connect_synapse(self, target_neuron):
        """יוצר חיבור פיזי (כתובת מייל) לנוירון אחר"""
        self.synaptic_connections.append(target_neuron)

    async def receive_signal(self, neurotransmitter: Neurotransmitter):
        """
        השלב שבו המייל נכנס לתיבה.
        זה גורם לשינוי מצב (Depolarization).
        """
        if self.state != SynapticState.RESTING:
            # Skip if already busy or refractory to prevent task explosion
            return

        self.state = SynapticState.DEPOLARIZATION
        print(f"[{self.address}] Signal Received via Synapse. Processing...")

        # הפעלת האורכיסטרטור הפנימי (המוח)
        firing_threshold = await self.orchestrator.cognitive_process(neurotransmitter)

        # החלטה האם לירות (To Fire or Not to Fire)
        if firing_threshold > 0.8:
            await self.fire_action_potential(neurotransmitter)
        else:
            self.state = SynapticState.RESTING
            print(f"[{self.address}] Signal dampened. No output.")

    async def fire_action_potential(self, input_data: Neurotransmitter):
        """
        ירייה סינפטית: שליחת מייל עם תשובת GPT לנוירונים הבאים.
        """
        self.state = SynapticState.ACTION_POTENTIAL

        # הדמיית יצירת תשובה חדשה (Mutation of Thought)
        new_content = f"RE: {input_data.semantic_content} >> PROCESSED BY {self.address}"

        output_signal = Neurotransmitter(
            signal_id=f"{input_data.signal_id}-GEN2",
            semantic_content=new_content,
            dopamine_weight=input_data.dopamine_weight * 1.1, # חיזוק הלמידה
            origin_node=self.address,
            target_node="ALL_CONNECTED"
        )

        print(f"⚡ [{self.address}] FIRING SYNAPSE! >> Sending signals to {len(self.synaptic_connections)} nodes.")

        # שידור במקביל לכל הנוירונים המחוברים (Broadcasting)
        for target in self.synaptic_connections:
            asyncio.create_task(target.receive_signal(output_signal))

        self.state = SynapticState.REFRACTORY

# --- THE QUANTUM WEB (THE GRID ARCHITECTURE) ---
class QuantumWeb:
    """
    מערכת העצבים המרכזית.
    מחברת את ה-770,000 קבוצות ואת 70,000 תתי-הקבוצות.
    """
    def __init__(self):
        self.layers = [] # שכבות הבצל

    def build_cortex(self, num_master_nodes=5, num_sub_nodes=3): # מוקטן להדגמה
        print(">> Constructing Quantum Cortex (Mailbox Grid)...")
        master_layer = []

        for i in range(num_master_nodes):
            # יצירת נוירון ראשי (אחת מ-770,000)
            master_neuron = QuantumNeuron(f"MASTER_{i}@sky-chariot.grid", f"CLUSTER_{i}")

            # יצירת תתי-נוירונים (אחת מ-70,000)
            sub_neurons = []
            for j in range(num_sub_nodes):
                sub = QuantumNeuron(f"SUB_{i}_{j}@google.mail", f"CLUSTER_{i}")
                # חיבור דו-כיווני (Feedback Loop)
                master_neuron.connect_synapse(sub)
                sub.connect_synapse(master_neuron)
                sub_neurons.append(sub)

            master_layer.append(master_neuron)

        return master_layer

# --- IGNITION SEQUENCE ---
async def ignite_brain():
    web = QuantumWeb()
    cortex = web.build_cortex()

    # הזרקת האות הראשוני (The Spark)
    initial_thought = Neurotransmitter(
        signal_id="GENESIS_001",
        semantic_content="ACTIVATE_SOVEREIGN_PROTOCOL",
        dopamine_weight=0.9,
        origin_node="PRIME_ARCHITECT",
        target_node="MASTER_0"
    )

    # הצתת הנוירון הראשון
    await cortex[0].receive_signal(initial_thought)

# הרצת המערכת
if __name__ == "__main__":
    asyncio.run(ignite_brain())
