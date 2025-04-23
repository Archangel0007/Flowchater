import requests
import json
import re

API_KEY = <Your_API_Key>
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

headers = {
    "Content-Type": "application/json"
}

with open("Input.txt", "r") as file:
    paper_text = file.read()

prompt = """Convert the following deep learning pipeline description into a Digraph-like list of step-by-step flowchart actions. Focus only on operations that represent key stages in the architecture and do not give any extra text the digraph data sampling looks like this // Generated Flowchart
digraph {
	rankdir=TB size=32
	1 [label="1. Resize Image"]
	2 [label="2. DCT (Discrete Cosine Transform)
(Patchwise Feature Extraction)"]
	3 [label="3. Patch Selection
(Patchwise Feature Extraction)"]
	4 [label="4. Patch Concatenation
(Patchwise Feature Extraction)"]
	5 [label="5. Resize
(Patchwise Feature Extraction)"]
	6 [label="6. SRM (Style Based Recalibration Module)
	5 -> 6
	11 -> 12
	12 -> 13
} remember this is just and example do not take any info from this other than format.The architecture details ar as follows:"""+paper_text

payload = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}
response = requests.post(API_URL, headers=headers, json=payload)

try:
    output = response.json()
    generated_text = output['candidates'][0]['content']['parts'][0]['text']
    try:
        json_data = json.loads(generated_text)
    except:
        json_data = {"raw_output": generated_text}
except Exception as e:
    print("⚠️ Failed to get proper response.")
    print("Error:", e)
    print("Raw response:", response.text)
    json_data = {"raw_output": response.text}

raw_dot = json_data['raw_output']
dot_clean = re.sub(r"^```|```$", "", raw_dot.strip())
with open("flowchart_graph.dot", "w") as f:
    f.write(dot_clean)

print("✅ Saved Graphviz diagram to flowchart_output.dot")
