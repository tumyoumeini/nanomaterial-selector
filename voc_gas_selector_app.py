
import streamlit as st
import requests
import openai

# --- SETUP YOUR API KEYS ---
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
CSE_ID = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
OPENAI_API_KEY = "YOUR_OPENAI_KEY"

openai.api_key = OPENAI_API_KEY

# --- FULL LIST OF 100 ANALYTES ---
common_gases = [
    "Ammonia (NH₃)", "Hydrogen Sulfide (H₂S)", "Nitrogen Dioxide (NO₂)", "Nitric Oxide (NO)", "Sulfur Dioxide (SO₂)",
    "Carbon Monoxide (CO)", "Carbon Dioxide (CO₂)", "Methane (CH₄)", "Hydrogen (H₂)", "Oxygen (O₂)", "Ozone (O₃)",
    "Chlorine (Cl₂)", "Bromine (Br₂)", "Fluorine (F₂)", "Iodine (I₂)", "Hydrogen Fluoride (HF)", "Hydrogen Chloride (HCl)",
    "Hydrogen Cyanide (HCN)", "Arsine (AsH₃)", "Phosphine (PH₃)", "Silane (SiH₄)", "Diborane (B₂H₆)", "Nitrous Oxide (N₂O)",
    "Ethylene (C₂H₄)", "Acetylene (C₂H₂)", "Radon (Rn)", "Helium (He)", "Neon (Ne)", "Argon (Ar)", "Krypton (Kr)",
    "Xenon (Xe)", "Isobutylene", "Ethane (C₂H₆)", "Propane (C₃H₈)", "Butane (C₄H₁₀)", "Dimethyl Ether (DME)",
    "Hydrogen Peroxide (H₂O₂ vapor)", "Sulfur Hexafluoride (SF₆)", "Amine vapors", "Nitrosyl Chloride (NOCl)"
]

common_vocs = [
    "Acetone", "Ethanol", "Methanol", "Toluene", "Benzene", "Xylene", "Formaldehyde", "Acetic Acid", "Isopropanol",
    "Chloroform", "Styrene", "Phenol", "Hexane", "Heptane", "Octane", "Nonane", "Decane", "Cyclohexane",
    "2-Butanone (MEK)", "2-Propanol", "1-Propanol", "Ethyl Acetate", "Butyl Acetate", "Methyl Acetate",
    "Diethyl Ether", "Dimethylformamide (DMF)", "Dimethyl Sulfoxide (DMSO)", "Vinyl Acetate", "Vinyl Chloride",
    "Carbon Disulfide", "1,2-Dichlorobenzene", "1,4-Dioxane", "Limonene", "α-Pinene", "β-Pinene", "Terpineol",
    "Tetrahydrofuran (THF)", "Furfural", "Cresol", "Aniline", "Pyridine", "Thiophene", "Acetonitrile", "Naphthalene",
    "Isobutanol", "Butanol", "Ethylene Glycol", "Propylene Glycol", "Allyl Alcohol", "Butyraldehyde",
    "Isovaleraldehyde", "Benzaldehyde", "Methyl Isobutyl Ketone (MIBK)", "Acrolein", "Diisocyanates (e.g., TDI)",
    "Tetrachloroethylene (PCE)", "Trichloroethylene (TCE)", "Methyl Tertiary Butyl Ether (MTBE)", "Nitromethane",
    "1,2-Dichloroethane"
]

analytes = common_gases + common_vocs

# --- STREAMLIT UI ---
st.set_page_config(page_title="Nanomaterial Selector AI", layout="centered")
st.title("🔬 AI-Powered Nanomaterial Recommender for Gas/VOC Sensing")

target = st.selectbox("Select a gas or VOC:", analytes)

if st.button("🔍 Search & Get Nanomaterial Suggestion"):
    st.info("Searching Google for scholarly results...")

    query = f"{target} gas sensor selective nanomaterial site:researchgate.net OR site:nature.com OR site:sciencedirect.com"

    google_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": CSE_ID,
        "q": query,
        "num": 10
    }

    response = requests.get(google_url, params=params)
    results = response.json().get("items", [])

    combined_text = ""
    for i, item in enumerate(results):
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        combined_text += f"{i+1}. {title}\n{snippet}\n{link}\n\n"

    if not combined_text:
        st.warning("No search results found.")
    else:
        st.info("Analyzing results using AI...")

        prompt = f"""
You are an expert in nanomaterial-based gas sensors. Based on the following search results, suggest the best nanomaterial for selectively detecting {target}. Be specific, and mention any promising material if supported by evidence.

Results:
{combined_text}
        """

        gpt_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=350
        )

        suggestion = gpt_response["choices"][0]["message"]["content"]

        st.success(f"📌 AI Suggestion for {target}:")
        st.markdown(suggestion)
