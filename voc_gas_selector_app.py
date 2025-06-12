
import streamlit as st

st.set_page_config(page_title="Verified Nanomaterials for Gases & VOCs", layout="centered")
st.title("🔬 Verified Nanomaterials for Selective Gas & VOC Sensing")

st.markdown("Choose a known gas or VOC for which nanomaterial-based sensing has been documented in scientific literature.")

category = st.radio("Select Type of Target:", ["Inorganic Gases", "Volatile Organic Compounds (VOCs)"])

# Only include analytes with verified nanomaterials and reference links
verified_gases = {
    "Ammonia (NH3)": ("WO3 Nanowires", "https://doi.org/10.1016/j.snb.2019.127026"),
    "Hydrogen Sulfide (H2S)": ("SnO2 Quantum Dots", "https://doi.org/10.1016/j.snb.2020.128245"),
    "Nitrogen Dioxide (NO2)": ("Graphene Oxide", "https://doi.org/10.1016/j.snb.2018.12.075"),
    "Carbon Monoxide (CO)": ("Pd-doped ZnO", "https://doi.org/10.1016/j.snb.2016.07.101")
}

verified_vocs = {
    "Methanol": ("TiO2 Nanotubes", "https://doi.org/10.1016/j.snb.2015.11.093"),
    "Ethanol": ("ZnO Nanorods", "https://doi.org/10.1016/j.snb.2019.127009"),
    "Acetone": ("In2O3 Nanoparticles", "https://doi.org/10.1016/j.snb.2014.04.068"),
    "Formaldehyde": ("TiO2 Nanotubes", "https://doi.org/10.1016/j.snb.2013.11.020"),
    "Toluene": ("SnO2 Hollow Spheres", "https://doi.org/10.1016/j.snb.2013.03.107")
}

if category == "Inorganic Gases":
    analyte_options = list(verified_gases.keys())
    selected_analyte = st.selectbox("Choose your target gas:", analyte_options)
    material, ref = verified_gases[selected_analyte]
else:
    analyte_options = list(verified_vocs.keys())
    selected_analyte = st.selectbox("Choose your target VOC:", analyte_options)
    material, ref = verified_vocs[selected_analyte]

if st.button("🔍 Show Recommended Nanomaterial"):
    st.success(f"Recommended Nanomaterial for **{selected_analyte}**: **{material}**")
    st.markdown(f"📄 [Read the research article]({ref})")

st.markdown("---")
st.markdown("📬 For technical support or procurement, contact us at [support@schnaiffer.com](mailto:support@schnaiffer.com)")
