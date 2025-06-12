
import streamlit as st

st.set_page_config(page_title="VOC/Gas Nanomaterial Selector", layout="centered")
st.title("🔬 AI Tool: Find Suitable Nanomaterials for Target Gases & VOCs")

st.markdown("Select your target analyte and detection range to discover nanomaterials with high selectivity and proven research references.")

category = st.radio("Select Type of Target:", ["Inorganic Gases", "Volatile Organic Compounds (VOCs)"])

gases = [
    "Ammonia (NH3)", "Hydrogen Sulfide (H2S)", "Nitrogen Dioxide (NO2)", "Carbon Monoxide (CO)", "Ozone (O3)",
    "Hydrogen (H2)", "Sulfur Dioxide (SO2)", "Methane (CH4)", "Carbon Dioxide (CO2)", "Chlorine (Cl2)",
    "Nitric Oxide (NO)", "Nitrous Oxide (N2O)", "Hydrogen Chloride (HCl)", "Hydrogen Fluoride (HF)", "Phosphine (PH3)",
    "Arsine (AsH3)", "Hydrogen Cyanide (HCN)", "Bromine (Br2)", "Fluorine (F2)", "Radon (Rn)",
    "Diborane (B2H6)", "Silane (SiH4)", "Dichlorosilane (SiH2Cl2)", "Hydrazine (N2H4)", "Iodine (I2)",
] + [f"Gas {i+1}" for i in range(75)]

vocs = [
    "Acetone", "Ethanol", "Methanol", "Benzene", "Toluene", "Formaldehyde", "Xylene", "Hexane",
    "Acetic Acid", "Isopropanol", "Chloroform", "Vinyl Chloride", "Methyl Ethyl Ketone (MEK)", "Styrene", "Limonene",
    "Phenol", "Tetrachloroethylene", "Trichloroethylene", "Carbon Disulfide", "Butyl Acetate",
] + [f"VOC {i+1}" for i in range(80)]

selected_analyte = st.selectbox("Choose your target analyte:", gases if category == "Inorganic Gases" else vocs)
sensitivity_range = st.radio("Select Sensitivity Range:", ["ppb (parts per billion)", "ppm (parts per million)"])

material_database = {
    ("Ammonia (NH3)", "ppb (parts per billion)"): ("WO3 Nanowires", "https://doi.org/10.1016/j.snb.2019.127026"),
    ("Hydrogen Sulfide (H2S)", "ppm (parts per million)"): ("SnO2 Quantum Dots", "https://doi.org/10.1016/j.snb.2020.128245"),
    ("Nitrogen Dioxide (NO2)", "ppb (parts per billion)"): ("Graphene Oxide", "https://doi.org/10.1016/j.snb.2018.12.075"),
    ("Methanol", "ppm (parts per million)"): ("TiO2 Nanotubes", "https://doi.org/10.1016/j.snb.2015.11.093"),
    ("Ethanol", "ppm (parts per million)"): ("ZnO Nanorods", "https://doi.org/10.1016/j.snb.2019.127009"),
    ("Acetone", "ppb (parts per billion)"): ("In2O3 Nanoparticles", "https://doi.org/10.1016/j.snb.2014.04.068"),
    ("Formaldehyde", "ppb (parts per billion)"): ("TiO2 Nanotubes", "https://doi.org/10.1016/j.snb.2013.11.020"),
}

material, ref = material_database.get((selected_analyte, sensitivity_range), ("Material data not available", "https://scholar.google.com"))

if st.button("🔍 Find Nanomaterial"):
    st.success(f"Recommended Nanomaterial: **{material}**")
    st.markdown(f"📄 [View Research Reference]({ref})")

st.markdown("---")
st.markdown("📬 Need help selecting or ordering this material? Contact us at [support@schnaiffer.com](mailto:support@schnaiffer.com)")
