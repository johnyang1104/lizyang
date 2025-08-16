import streamlit as st
import json
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Kidney Tumor Pathology Reporting Checklist",
    page_icon="🫘",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .section-header {
        background-color: #e8f4fd;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        border-left: 4px solid #1f77b4;
        margin: 1.5rem 0 1rem 0;
    }
    .stSelectbox label, .stRadio label, .stCheckbox label {
        font-weight: 500;
    }
    .subsection {
        background-color: #f8f9fa;
        padding: 0.5rem 1rem;
        border-radius: 3px;
        margin: 1rem 0;
        border-left: 2px solid #6c757d;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("🫘 Kidney Tumor Pathology Reporting Checklist")
    st.markdown("**AJCC 8th Edition Standard** | Protocol Posting Date: June 2025")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Initialize session state for form data
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    
    # ========== CASE SUMMARY SECTION ==========
    st.markdown('<div class="section-header"><h2>📋 CASE SUMMARY</h2></div>', unsafe_allow_html=True)
    st.markdown("**(KIDNEY: Nephrectomy)**")
    
    col1, col2 = st.columns(2)
    with col1:
        case_id = st.text_input("Case ID:", key="case_id")
        patient_name = st.text_input("Patient Name:", key="patient_name")
        age = st.number_input("Age:", min_value=0, max_value=120, key="age")
    with col2:
        gender = st.selectbox("Gender:", ["", "Male", "Female"], key="gender")
        date_of_procedure = st.date_input("Date of Procedure:", key="date_of_procedure")
        pathologist = st.text_input("Pathologist:", key="pathologist")
    
    clinical_diagnosis = st.text_input("Clinical Diagnosis:", key="clinical_diagnosis")
    
    # ========== SPECIMEN SECTION ==========
    st.markdown('<div class="section-header"><h2>🧪 SPECIMEN</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><h4>Procedure</h4></div>', unsafe_allow_html=True)
    procedure_options = [
        "Partial nephrectomy",
        "Total (simple) nephrectomy", 
        "Radical nephrectomy",
        "Other",
        "Not specified"
    ]
    procedure = st.selectbox("Select procedure:", [""] + procedure_options, key="procedure")
    if procedure == "Other":
        procedure_other = st.text_input("Specify other procedure:", key="procedure_other")
    
    st.markdown('<div class="subsection"><h4>Specimen Laterality</h4></div>', unsafe_allow_html=True)
    laterality_options = [
        "Right",
        "Left",
        "Other",
        "Not specified"
    ]
    laterality = st.selectbox("Specimen laterality:", [""] + laterality_options, key="laterality")
    if laterality == "Other":
        laterality_other = st.text_input("Specify other laterality:", key="laterality_other")
    
    st.markdown('<div class="subsection"><h4>Specimen Weight & Dimensions</h4></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        kidney_weight = st.number_input("Kidney Weight (g):", min_value=0.0, step=1.0, key="kidney_weight")
    with col2:
        col2a, col2b, col2c = st.columns(3)
        with col2a:
            kidney_length = st.number_input("Length (cm):", min_value=0.0, step=0.1, key="kidney_length")
        with col2b:
            kidney_width = st.number_input("Width (cm):", min_value=0.0, step=0.1, key="kidney_width")
        with col2c:
            kidney_height = st.number_input("Height (cm):", min_value=0.0, step=0.1, key="kidney_height")
    
    # ========== TUMOR SECTION ==========
    st.markdown('<div class="section-header"><h2>🎯 TUMOR</h2></div>', unsafe_allow_html=True)
    
    # Tumor Focality
    st.markdown('<div class="subsection"><h4>Tumor Focality</h4></div>', unsafe_allow_html=True)
    focality_options = [
        "Unifocal",
        "Multifocal"
    ]
    focality = st.selectbox("Tumor focality:", [""] + focality_options, key="focality")
    if focality == "Multifocal":
        tumor_number = st.number_input("Number of tumors:", min_value=2, key="tumor_number")
    
    # Tumor Site
    st.markdown('<div class="subsection"><h4>Tumor Site (select all that apply)</h4></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        upper_pole = st.checkbox("Upper pole", key="site_upper_pole")
        middle = st.checkbox("Middle", key="site_middle")
    with col2:
        lower_pole = st.checkbox("Lower pole", key="site_lower_pole")
        other_site = st.checkbox("Other", key="site_other")
    
    if other_site:
        other_site_detail = st.text_input("Specify other site:", key="other_site_detail")
    
    not_specified_site = st.checkbox("Not specified", key="site_not_specified")
    
    # Tumor Size
    st.markdown('<div class="subsection"><h4>Tumor Size</h4></div>', unsafe_allow_html=True)
    st.info("If multiple tumors are present, document the size of the largest tumor.")
    
    size_method = st.radio(
        "Size measurement:",
        ["Greatest dimension in Centimeters (cm)", "Cannot be determined"],
        key="size_method"
    )
    
    if size_method == "Greatest dimension in Centimeters (cm)":
        greatest_dimension = st.number_input("Greatest dimension (cm):", min_value=0.0, step=0.1, key="greatest_dimension")
        
        additional_dims = st.checkbox("Additional dimensions", key="additional_dims")
        if additional_dims:
            col1, col2 = st.columns(2)
            with col1:
                size_x = st.number_input("Width (cm):", min_value=0.0, step=0.1, key="size_x")
            with col2:
                size_y = st.number_input("Height (cm):", min_value=0.0, step=0.1, key="size_y")
        
        # Other tumor sizes
        other_tumors = st.checkbox("Other tumor dimensions", key="other_tumors")
        if other_tumors:
            other_tumor_sizes = st.text_area("Greatest Dimension of Other Tumor(s) (cm):", key="other_tumor_sizes")
    else:
        size_explain = st.text_input("Explain why size cannot be determined:", key="size_explain")
    
    # Histologic Type
    st.markdown('<div class="subsection"><h4>Histologic Type</h4></div>', unsafe_allow_html=True)
    
    st.write("**Clear cell tumors:**")
    clear_cell_rcc = st.checkbox("Clear cell renal cell carcinoma", key="clear_cell_rcc")
    multilocular_cystic = st.checkbox("Multilocular cystic renal neoplasm of low malignant potential", key="multilocular_cystic")
    
    st.write("**Papillary renal tumors:**")
    papillary_rcc = st.checkbox("Papillary renal cell carcinoma", key="papillary_rcc")
    
    st.write("**Oncocytic and chromophobe renal tumors:**")
    chromophobe_rcc = st.checkbox("Chromophobe renal cell carcinoma", key="chromophobe_rcc")
    other_oncocytic = st.checkbox("Other oncocytic tumors of the kidney", key="other_oncocytic")
    if other_oncocytic:
        oncocytic_detail = st.text_input("Specify oncocytic tumor type:", key="oncocytic_detail")
    
    st.write("**Collecting duct tumors:**")
    collecting_duct = st.checkbox("Collecting duct carcinoma", key="collecting_duct")
    
    st.write("**Other renal tumors:**")
    clear_cell_papillary = st.checkbox("Clear cell papillary renal cell tumor", key="clear_cell_papillary")
    mucinous_tubular = st.checkbox("Mucinous tubular and spindle renal cell carcinoma", key="mucinous_tubular")
    tubulocystic = st.checkbox("Tubulocystic renal cell carcinoma", key="tubulocystic")
    acquired_cystic = st.checkbox("Acquired cystic disease-associated renal cell carcinoma", key="acquired_cystic")
    eosinophilic_solid = st.checkbox("Eosinophilic solid and cystic renal cell carcinoma", key="eosinophilic_solid")
    rcc_nos = st.checkbox("Renal cell carcinoma, NOS (unclassified)", key="rcc_nos")
    
    st.write("**Molecularly defined renal carcinomas:**")
    tfe3_rearranged = st.checkbox("TFE3-rearranged renal cell carcinoma", key="tfe3_rearranged")
    tfeb_altered = st.checkbox("TFEB-altered renal cell carcinoma", key="tfeb_altered")
    eloc_mutated = st.checkbox("ELOC (formerly TCEB1)-mutated renal cell carcinoma", key="eloc_mutated")
    fh_deficient = st.checkbox("Fumarate hydratase-deficient renal cell carcinoma", key="fh_deficient")
    sdh_deficient = st.checkbox("Succinate dehydrogenase-deficient (SDH) renal cell carcinoma", key="sdh_deficient")
    alk_rearranged = st.checkbox("ALK-rearranged renal cell carcinoma", key="alk_rearranged")
    smarcb1_deficient = st.checkbox("SMARCB1-deficient renal medullary carcinoma", key="smarcb1_deficient")
    
    st.write("**Other:**")
    subtype_pending = st.checkbox("Renal cell carcinoma, subtype pending additional studies", key="subtype_pending")
    other_histologic = st.checkbox("Other histologic type not listed", key="other_histologic")
    if other_histologic:
        other_histologic_detail = st.text_input("Specify other histologic type:", key="other_histologic_detail")
    
    histologic_comment = st.text_area("Histologic Type Comment:", key="histologic_comment")
    
    # Histologic Grade
    st.markdown('<div class="subsection"><h4>Histologic Grade (WHO / ISUP)</h4></div>', unsafe_allow_html=True)
    st.info("See table for renal carcinoma subtype grading requirements")
    
    grade_options = [
        "G1, nucleoli absent or inconspicuous at 400x magnification",
        "G2, nucleoli conspicuous and visible at 400x magnification, not prominent at 100x magnification",
        "G3, nucleoli conspicuous at 100x magnification",
        "G4, extreme nuclear pleomorphism and / or multinucleated giant cells and / or rhabdoid and / or sarcomatoid differentiation",
        "GX, cannot be assessed",
        "Not applicable"
    ]
    grade = st.selectbox("Histologic grade:", [""] + grade_options, key="grade")
    
    if grade and "G4" in grade:
        g4_specify = st.text_input("Specify G4 features:", key="g4_specify")
    elif grade and "Not applicable" in grade:
        grade_na_reason = st.text_input("Reason for not applicable:", key="grade_na_reason")
    
    grade_comment = st.text_area("Histologic Grade Comment:", key="grade_comment")
    
    # Tumor Extent
    st.markdown('<div class="subsection"><h4>Tumor Extent (select all that apply)</h4></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        limited_kidney = st.checkbox("Limited to kidney", key="extent_limited_kidney")
        perinephric_tissue = st.checkbox("Extends into perinephric tissue (beyond renal capsule)", key="extent_perinephric")
        renal_sinus = st.checkbox("Extends into renal sinus", key="extent_renal_sinus")
        pelvicalyceal = st.checkbox("Extends into pelvicalyceal system", key="extent_pelvicalyceal")
        renal_vein = st.checkbox("Extends into renal vein or its segmental branches", key="extent_renal_vein")
    
    with col2:
        ivc = st.checkbox("Extends into inferior vena cava", key="extent_ivc")
        gerota_fascia = st.checkbox("Extends beyond renal Gerota's fascia (renal fascia)", key="extent_gerota")
        adrenal_direct = st.checkbox("Directly invades adrenal gland (T4)", key="extent_adrenal_direct")
        adrenal_noncontiguous = st.checkbox("Involves adrenal gland non-contiguously (M1)", key="extent_adrenal_noncontiguous")
        other_organs = st.checkbox("Extends into other organ(s) / structure(s)", key="extent_other_organs")
    
    if other_organs:
        other_organs_detail = st.text_input("Specify other organs/structures:", key="other_organs_detail")
    
    cannot_determine_extent = st.checkbox("Cannot be determined", key="extent_cannot_determine")
    if cannot_determine_extent:
        extent_explain = st.text_input("Explain why cannot be determined:", key="extent_explain")
    
    # Histologic Features
    st.markdown('<div class="subsection"><h4>Histologic Features (select all that apply)</h4></div>', unsafe_allow_html=True)
    
    no_sarcomatoid_rhabdoid = st.checkbox("Sarcomatoid or rhabdoid features not identified", key="no_sarcomatoid_rhabdoid")
    
    sarcomatoid_present = st.checkbox("Sarcomatoid features present", key="sarcomatoid_present")
    if sarcomatoid_present:
        sarcomatoid_percentage = st.number_input("Percentage of Sarcomatoid Element (%):", min_value=0.0, max_value=100.0, step=1.0, key="sarcomatoid_percentage")
    
    rhabdoid_present = st.checkbox("Rhabdoid features present", key="rhabdoid_present")
    if rhabdoid_present:
        rhabdoid_percentage = st.number_input("Percentage of Rhabdoid Element (%):", min_value=0.0, max_value=100.0, step=1.0, key="rhabdoid_percentage")
    
    other_features = st.checkbox("Other", key="other_features")
    if other_features:
        other_features_detail = st.text_input("Specify other features:", key="other_features_detail")
    
    cannot_determine_features = st.checkbox("Cannot be determined", key="features_cannot_determine")
    if cannot_determine_features:
        features_explain = st.text_input("Explain:", key="features_explain")
    
    # Tumor Necrosis
    st.markdown('<div class="subsection"><h4>Tumor Necrosis</h4></div>', unsafe_allow_html=True)
    
    necrosis_options = [
        "Not identified",
        "Present",
        "Cannot be determined"
    ]
    necrosis = st.selectbox("Tumor necrosis:", [""] + necrosis_options, key="necrosis")
    
    if necrosis == "Present":
        necrosis_percentage = st.number_input("Percentage of Tumor Necrosis (%):", min_value=0.0, max_value=100.0, step=1.0, key="necrosis_percentage")
    elif necrosis == "Cannot be determined":
        necrosis_explain = st.text_input("Explain:", key="necrosis_explain")
    
    # Vascular Invasion
    st.markdown('<div class="subsection"><h4>Lymphatic and/or Small Vessel Vascular Invasion</h4></div>', unsafe_allow_html=True)
    st.info("(excluding renal vein and its segmental branches and inferior vena cava)")
    
    vascular_invasion_options = [
        "Not identified",
        "Present",
        "Cannot be determined"
    ]
    vascular_invasion = st.selectbox("Vascular invasion:", [""] + vascular_invasion_options, key="vascular_invasion")
    
    if vascular_invasion == "Cannot be determined":
        vascular_explain = st.text_input("Explain:", key="vascular_explain")
    
    # Tumor Comment
    tumor_comment = st.text_area("Tumor Comment:", key="tumor_comment")
    
    # ========== MARGINS SECTION ==========
    st.markdown('<div class="section-header"><h2>📏 MARGINS</h2></div>', unsafe_allow_html=True)
    
    # Margin Status
    st.markdown('<div class="subsection"><h4>Margin Status</h4></div>', unsafe_allow_html=True)
    
    margin_status_options = [
        "All margins negative for invasive carcinoma",
        "Invasive carcinoma present at margin"
    ]
    margin_status = st.selectbox("Margin status:", [""] + margin_status_options, key="margin_status")
    
    if margin_status == "Invasive carcinoma present at margin":
        st.write("**Margin(s) Involved by Invasive Carcinoma (select all that apply):**")
        st.info("For partial nephrectomy only")
        
        col1, col2 = st.columns(2)
        with col1:
            renal_parenchymal_margin = st.checkbox("Renal parenchymal", key="margin_renal_parenchymal")
            if renal_parenchymal_margin:
                renal_parenchymal_detail = st.text_input("Distance (mm):", key="renal_parenchymal_detail")
            
            renal_capsular_margin = st.checkbox("Renal capsular", key="margin_renal_capsular")
            if renal_capsular_margin:
                renal_capsular_detail = st.text_input("Distance (mm):", key="renal_capsular_detail")
            
            renal_sinus_margin = st.checkbox("Renal sinus soft tissue", key="margin_renal_sinus")
            if renal_sinus_margin:
                renal_sinus_detail = st.text_input("Distance (mm):", key="renal_sinus_detail")
            
            renal_hilar_margin = st.checkbox("Renal hilar soft tissue", key="margin_renal_hilar")
            if renal_hilar_margin:
                renal_hilar_detail = st.text_input("Distance (mm):", key="renal_hilar_detail")
        
        with col2:
            renal_vein_margin = st.checkbox("Renal vein (tumor invades or is adherent to vein wall at margin)", key="margin_renal_vein")
            if renal_vein_margin:
                renal_vein_detail = st.text_input("Details:", key="renal_vein_detail")
            
            ureteral_margin = st.checkbox("Ureteral", key="margin_ureteral")
            if ureteral_margin:
                ureteral_detail = st.text_input("Distance (mm):", key="ureteral_detail")
            
            perinephric_fat_margin = st.checkbox("Perinephric fat", key="margin_perinephric_fat")
            if perinephric_fat_margin:
                perinephric_fat_detail = st.text_input("Distance (mm):", key="perinephric_fat_detail")
            
            gerota_fascia_margin = st.checkbox("Gerota's fascia", key="margin_gerota_fascia")
            if gerota_fascia_margin:
                gerota_fascia_detail = st.text_input("Distance (mm):", key="gerota_fascia_detail")
    
    margin_other = st.checkbox("Other", key="margin_other")
    if margin_other:
        margin_other_detail = st.text_input("Specify other margin:", key="margin_other_detail")
    
    margin_cannot_determine = st.checkbox("Cannot be determined", key="margin_cannot_determine")
    if margin_cannot_determine:
        margin_explain = st.text_input("Explain:", key="margin_explain")
    
    margin_not_applicable = st.checkbox("Not applicable", key="margin_not_applicable")
    
    margin_comment = st.text_area("Margin Comment:", key="margin_comment")
    
    # ========== REGIONAL LYMPH NODES SECTION ==========
    st.markdown('<div class="section-header"><h2>🔗 REGIONAL LYMPH NODES</h2></div>', unsafe_allow_html=True)
    
    # Regional Lymph Node Status
    st.markdown('<div class="subsection"><h4>Regional Lymph Node Status</h4></div>', unsafe_allow_html=True)
    
    ln_status_options = [
        "Not applicable (no regional lymph nodes submitted or found)",
        "Regional lymph nodes present"
    ]
    ln_status = st.selectbox("Regional lymph node status:", [""] + ln_status_options, key="ln_status")
    
    if ln_status == "Regional lymph nodes present":
        ln_tumor_status_options = [
            "All regional lymph nodes negative for tumor",
            "Tumor present in regional lymph node(s)"
        ]
        ln_tumor_status = st.selectbox("Tumor in lymph nodes:", [""] + ln_tumor_status_options, key="ln_tumor_status")
        
        if ln_tumor_status == "Tumor present in regional lymph node(s)":
            st.write("**Number of Lymph Nodes with Tumor:**")
            
            ln_positive_method = st.radio(
                "Number of positive nodes:",
                ["Exact number", "At least", "Other", "Cannot be determined"],
                key="ln_positive_method"
            )
            
            if ln_positive_method == "Exact number":
                ln_positive_exact = st.number_input("Exact number of positive nodes:", min_value=0, key="ln_positive_exact")
            elif ln_positive_method == "At least":
                ln_positive_atleast = st.number_input("At least number of positive nodes:", min_value=0, key="ln_positive_atleast")
            elif ln_positive_method == "Other":
                ln_positive_other = st.text_input("Specify other:", key="ln_positive_other")
            elif ln_positive_method == "Cannot be determined":
                ln_positive_explain = st.text_input("Explain:", key="ln_positive_explain")
            
            # Nodal Site(s) with Tumor
            st.write("**Nodal Site(s) with Tumor (select all that apply):**")
            col1, col2 = st.columns(2)
            
            with col1:
                hilar_nodes = st.checkbox("Hilar", key="node_hilar")
                if hilar_nodes:
                    hilar_detail = st.text_input("Hilar node details:", key="hilar_detail")
                
                precaval_nodes = st.checkbox("Precaval", key="node_precaval")
                if precaval_nodes:
                    precaval_detail = st.text_input("Precaval node details:", key="precaval_detail")
                
                interaortocaval_nodes = st.checkbox("Interaortocaval", key="node_interaortocaval")
                if interaortocaval_nodes:
                    interaortocaval_detail = st.text_input("Interaortocaval node details:", key="interaortocaval_detail")
                
                paracaval_nodes = st.checkbox("Paracaval", key="node_paracaval")
                if paracaval_nodes:
                    paracaval_detail = st.text_input("Paracaval node details:", key="paracaval_detail")
            
            with col2:
                retrocaval_nodes = st.checkbox("Retrocaval", key="node_retrocaval")
                if retrocaval_nodes:
                    retrocaval_detail = st.text_input("Retrocaval node details:", key="retrocaval_detail")
                
                preaortic_nodes = st.checkbox("Preaortic", key="node_preaortic")
                if preaortic_nodes:
                    preaortic_detail = st.text_input("Preaortic node details:", key="preaortic_detail")
                
                paraaortic_nodes = st.checkbox("Paraaortic", key="node_paraaortic")
                if paraaortic_nodes:
                    paraaortic_detail = st.text_input("Paraaortic node details:", key="paraaortic_detail")
                
                retroaortic_nodes = st.checkbox("Retroaortic", key="node_retroaortic")
                if retroaortic_nodes:
                    retroaortic_detail = st.text_input("Retroaortic node details:", key="retroaortic_detail")
            
            other_nodal_site = st.checkbox("Other", key="node_other")
            if other_nodal_site:
                other_nodal_detail = st.text_input("Specify other nodal site:", key="other_nodal_detail")
            
            # Size of Largest Nodal Metastatic Deposit
            st.write("**Size of Largest Nodal Metastatic Deposit:**")
            
            largest_met_method = st.radio(
                "Size of largest metastatic deposit (cm):",
                ["Exact size", "At least", "Greater than", "Less than", "Other", "Cannot be determined"],
                key="largest_met_method"
            )
            
            if largest_met_method == "Exact size":
                largest_met_exact = st.number_input("Exact size (cm):", min_value=0.0, step=0.1, key="largest_met_exact")
            elif largest_met_method == "At least":
                largest_met_atleast = st.number_input("At least (cm):", min_value=0.0, step=0.1, key="largest_met_atleast")
            elif largest_met_method == "Greater than":
                largest_met_greater = st.number_input("Greater than (cm):", min_value=0.0, step=0.1, key="largest_met_greater")
            elif largest_met_method == "Less than":
                largest_met_less = st.number_input("Less than (cm):", min_value=0.0, step=0.1, key="largest_met_less")
            elif largest_met_method == "Other":
                largest_met_other = st.text_input("Specify other:", key="largest_met_other")
            elif largest_met_method == "Cannot be determined":
                largest_met_explain = st.text_input("Explain:", key="largest_met_explain")
            
            largest_met_site = st.text_input("Specify Nodal Site with Largest Metastatic Deposit:", key="largest_met_site")
            
            # Extranodal Extension
            st.write("**Extranodal Extension (ENE):**")
            ene_options = ["Not identified", "Present", "Cannot be determined"]
            ene = st.selectbox("Extranodal Extension:", [""] + ene_options, key="ene")
            
            if ene == "Present":
                ene_location = st.text_input("Specify Location of Involved Lymph Node(s):", key="ene_location")
            elif ene == "Cannot be determined":
                ene_explain = st.text_input("Explain:", key="ene_explain")
        
        # Number of Lymph Nodes Examined
        st.write("**Number of Lymph Nodes Examined:**")
        
        ln_examined_method = st.radio(
            "Number of examined nodes:",
            ["Exact number", "At least", "Other", "Cannot be determined"],
            key="ln_examined_method"
        )
        
        if ln_examined_method == "Exact number":
            ln_examined_exact = st.number_input("Exact number of examined nodes:", min_value=0, key="ln_examined_exact")
        elif ln_examined_method == "At least":
            ln_examined_atleast = st.number_input("At least number of examined nodes:", min_value=0, key="ln_examined_atleast")
        elif ln_examined_method == "Other":
            ln_examined_other = st.text_input("Specify other:", key="ln_examined_other")
        elif ln_examined_method == "Cannot be determined":
            ln_examined_explain = st.text_input("Explain:", key="ln_examined_explain")
    
    ln_comment = st.text_area("Regional Lymph Node Comment:", key="ln_comment")
    
    # ========== DISTANT METASTASIS SECTION ==========
    st.markdown('<div class="section-header"><h2>🎯 DISTANT METASTASIS</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><h4>Distant Site(s) Involved, if applicable</h4></div>', unsafe_allow_html=True)
    
    dm_not_applicable = st.checkbox("Not applicable", key="dm_not_applicable")
    
    dm_specify = st.checkbox("Specify site(s)", key="dm_specify")
    if dm_specify:
        dm_sites = st.text_area("Specify distant metastasis sites:", key="dm_sites")
    
    dm_cannot_determine = st.checkbox("Cannot be determined", key="dm_cannot_determine")
    if dm_cannot_determine:
        dm_explain = st.text_input("Explain:", key="dm_explain")
    
    # ========== pTNM CLASSIFICATION SECTION ==========
    st.markdown('<div class="section-header"><h2>📊 pTNM CLASSIFICATION (AJCC 8th Edition)</h2></div>', unsafe_allow_html=True)
    
    st.info("Reporting of pT, pN, and (when applicable) pM categories is based on information available to the pathologist at the time the report is issued. As per the AJCC (Chapter 1, 8th Ed.) it is the managing physician's responsibility to establish the final pathologic stage based upon all pertinent information, including but potentially not limited to this pathology report.")
    
    # Modified Classification
    st.markdown('<div class="subsection"><h4>Modified Classification (required only if applicable)</h4></div>', unsafe_allow_html=True)
    
    modified_not_applicable = st.checkbox("Not applicable", key="modified_not_applicable")
    modified_y = st.checkbox("y (post-neoadjuvant therapy)", key="modified_y")
    modified_r = st.checkbox("r (recurrence)", key="modified_r")
    
    # pT Category
    st.markdown('<div class="subsection"><h4>pT Category</h4></div>', unsafe_allow_html=True)
    
    pt_options = [
        "pT not assigned (cannot be determined based on available pathological information)",
        "pT0: No evidence of primary tumor",
        "pT1a: Tumor less than or equal to 4 cm in greatest dimension, limited to the kidney",
        "pT1b: Tumor greater than 4 cm but less than or equal to 7 cm in greatest dimension limited to the kidney",
        "pT1 (subcategory cannot be determined)",
        "pT2a: Tumor greater than 7 cm but less than or equal to 10 cm in greatest dimension, limited to the kidney",
        "pT2b: Tumor greater than 10 cm, limited to the kidney",
        "pT2 (subcategory cannot be determined)",
        "pT3a: Tumor extends into the renal vein or its segmental branches, or invades the pelvicalyceal system, or invades perirenal and / or renal sinus fat but not beyond Gerota's fascia",
        "pT3b: Tumor extends into the vena cava below the diaphragm",
        "pT3c: Tumor extends into the vena cava above the diaphragm or invades the wall of the vena cava",
        "pT3 (subcategory cannot be determined)",
        "pT4: Tumor invades beyond Gerota's fascia (including contiguous extension into the ipsilateral adrenal gland)"
    ]
    
    pt_category = st.selectbox("pT Category:", [""] + pt_options, key="pt_category")
    
    # T Suffix
    st.markdown('<div class="subsection"><h4>T Suffix (required only if applicable)</h4></div>', unsafe_allow_html=True)
    
    t_suffix_applicable = st.radio(
        "T suffix:",
        ["Not applicable", "(m) multiple primary synchronous tumors in a single organ"],
        key="t_suffix_applicable"
    )
    
    # pN Category
    st.markdown('<div class="subsection"><h4>pN Category</h4></div>', unsafe_allow_html=True)
    
    pn_options = [
        "pN not assigned (no nodes submitted or found)",
        "pN not assigned (cannot be determined based on available pathological information)",
        "pN0: No regional lymph node metastasis",
        "pN1: Metastasis in regional lymph node(s)"
    ]
    
    pn_category = st.selectbox("pN Category:", [""] + pn_options, key="pn_category")
    
    # pM Category
    st.markdown('<div class="subsection"><h4>pM Category (required only if confirmed pathologically)</h4></div>', unsafe_allow_html=True)
    
    pm_options = [
        "Not applicable - pM cannot be determined from the submitted specimen(s)",
        "pM1: Distant metastasis (including non-contiguous adrenal gland involvement)"
    ]
    
    pm_category = st.selectbox("pM Category:", [""] + pm_options, key="pm_category")
    
    # ========== ADDITIONAL FINDINGS SECTION ==========
    st.markdown('<div class="section-header"><h2>🔍 ADDITIONAL FINDINGS</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><h4>Additional Findings in Kidney (select all that apply)</h4></div>', unsafe_allow_html=True)
    
    additional_insufficient = st.checkbox("Insufficient tissue", key="additional_insufficient")
    additional_no_change = st.checkbox("No significant pathologic change identified", key="additional_no_change")
    
    additional_glomerular = st.checkbox("Glomerular disease", key="additional_glomerular")
    if additional_glomerular:
        glomerular_type = st.text_input("Specify type of glomerular disease:", key="glomerular_type")
    
    additional_tubulointerstitial = st.checkbox("Tubulointerstitial disease", key="additional_tubulointerstitial")
    if additional_tubulointerstitial:
        tubulointerstitial_type = st.text_input("Specify type of tubulointerstitial disease:", key="tubulointerstitial_type")
    
    additional_vascular = st.checkbox("Vascular disease", key="additional_vascular")
    if additional_vascular:
        vascular_type = st.text_input("Specify type of vascular disease:", key="vascular_type")
    
    additional_cysts = st.checkbox("Cyst(s)", key="additional_cysts")
    if additional_cysts:
        cysts_type = st.text_input("Specify type of cyst(s):", key="cysts_type")
    
    additional_adenomas = st.checkbox("Papillary adenoma(s)", key="additional_adenomas")
    if additional_adenomas:
        adenomas_detail = st.text_input("Papillary adenoma details:", key="adenomas_detail")
    
    additional_other = st.checkbox("Other", key="additional_other")
    if additional_other:
        additional_other_detail = st.text_input("Specify other findings:", key="additional_other_detail")
    
    # ========== IMMUNOHISTOCHEMISTRY SECTION ==========
    st.markdown('<div class="section-header"><h2>🧬 IMMUNOHISTOCHEMISTRY</h2></div>', unsafe_allow_html=True)
    st.info("If applicable - Optional section for recording immunohistochemistry results")
    
    ihc_performed = st.checkbox("Immunohistochemistry performed", key="ihc_performed")
    
    if ihc_performed:
        st.markdown('<div class="subsection"><h4>Immunohistochemistry Results</h4></div>', unsafe_allow_html=True)
        
        # Common kidney tumor markers
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.write("**Antibody**")
            cd10_antibody = st.checkbox("CD10", key="cd10_antibody")
            ck7_antibody = st.checkbox("CK7", key="ck7_antibody")
            vimentin_antibody = st.checkbox("Vimentin", key="vimentin_antibody")
            pax8_antibody = st.checkbox("PAX8", key="pax8_antibody")
            rcc_antibody = st.checkbox("RCC Marker", key="rcc_antibody")
        
        with col2:
            st.write("**Result**")
            if cd10_antibody:
                cd10_result = st.selectbox("CD10 Result:", ["", "Positive", "Negative"], key="cd10_result")
            if ck7_antibody:
                ck7_result = st.selectbox("CK7 Result:", ["", "Positive", "Negative"], key="ck7_result")
            if vimentin_antibody:
                vimentin_result = st.selectbox("Vimentin Result:", ["", "Positive", "Negative"], key="vimentin_result")
            if pax8_antibody:
                pax8_result = st.selectbox("PAX8 Result:", ["", "Positive", "Negative"], key="pax8_result")
            if rcc_antibody:
                rcc_result = st.selectbox("RCC Result:", ["", "Positive", "Negative"], key="rcc_result")
        
        with col3:
            st.write("**Intensity**")
            if cd10_antibody and st.session_state.get("cd10_result") == "Positive":
                cd10_intensity = st.selectbox("CD10 Intensity:", ["", "Weak", "Moderate", "Strong"], key="cd10_intensity")
            if ck7_antibody and st.session_state.get("ck7_result") == "Positive":
                ck7_intensity = st.selectbox("CK7 Intensity:", ["", "Weak", "Moderate", "Strong"], key="ck7_intensity")
            if vimentin_antibody and st.session_state.get("vimentin_result") == "Positive":
                vimentin_intensity = st.selectbox("Vimentin Intensity:", ["", "Weak", "Moderate", "Strong"], key="vimentin_intensity")
            if pax8_antibody and st.session_state.get("pax8_result") == "Positive":
                pax8_intensity = st.selectbox("PAX8 Intensity:", ["", "Weak", "Moderate", "Strong"], key="pax8_intensity")
            if rcc_antibody and st.session_state.get("rcc_result") == "Positive":
                rcc_intensity = st.selectbox("RCC Intensity:", ["", "Weak", "Moderate", "Strong"], key="rcc_intensity")
        
        with col4:
            st.write("**Percentage (%)**")
            if cd10_antibody and st.session_state.get("cd10_result") == "Positive":
                cd10_percentage = st.number_input("CD10 %:", min_value=0.0, max_value=100.0, step=1.0, key="cd10_percentage")
            if ck7_antibody and st.session_state.get("ck7_result") == "Positive":
                ck7_percentage = st.number_input("CK7 %:", min_value=0.0, max_value=100.0, step=1.0, key="ck7_percentage")
            if vimentin_antibody and st.session_state.get("vimentin_result") == "Positive":
                vimentin_percentage = st.number_input("Vimentin %:", min_value=0.0, max_value=100.0, step=1.0, key="vimentin_percentage")
            if pax8_antibody and st.session_state.get("pax8_result") == "Positive":
                pax8_percentage = st.number_input("PAX8 %:", min_value=0.0, max_value=100.0, step=1.0, key="pax8_percentage")
            if rcc_antibody and st.session_state.get("rcc_result") == "Positive":
                rcc_percentage = st.number_input("RCC %:", min_value=0.0, max_value=100.0, step=1.0, key="rcc_percentage")
        
        other_ihc = st.text_area("Other Immunohistochemistry Results:", key="other_ihc")
    
    # ========== MOLECULAR TESTING SECTION ==========
    st.markdown('<div class="section-header"><h2>🧪 MOLECULAR TESTING</h2></div>', unsafe_allow_html=True)
    st.info("If applicable - Optional section for recording molecular testing results")
    
    molecular_performed = st.checkbox("Molecular testing performed", key="molecular_performed")
    
    if molecular_performed:
        st.markdown('<div class="subsection"><h4>Molecular Testing Results</h4></div>', unsafe_allow_html=True)
        
        vhl_testing = st.checkbox("VHL gene mutation testing", key="vhl_testing")
        if vhl_testing:
            vhl_result = st.text_input("VHL testing result:", key="vhl_result")
        
        other_molecular = st.text_area("Other Molecular Markers:", key="other_molecular")
    else:
        st.write("No molecular testing performed")
    
    # ========== PROGNOSTIC ASSESSMENT SECTION ==========
    st.markdown('<div class="section-header"><h2>📈 PROGNOSTIC ASSESSMENT</h2></div>', unsafe_allow_html=True)
    st.info("Optional section for risk stratification")
    
    prognostic_assessment = st.checkbox("Perform prognostic assessment", key="prognostic_assessment")
    
    if prognostic_assessment:
        st.markdown('<div class="subsection"><h4>Prognostic Factors</h4></div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            tumor_size_score = st.number_input("Tumor Size Score:", min_value=0, max_value=10, key="tumor_size_score")
            grade_score = st.number_input("Grade Score:", min_value=0, max_value=10, key="grade_score")
        
        with col2:
            stage_score = st.number_input("Stage Score:", min_value=0, max_value=10, key="stage_score")
            overall_score = st.number_input("Overall Prognostic Score:", min_value=0, max_value=30, key="overall_score")
        
        risk_stratification_options = [
            "Low risk",
            "Intermediate risk", 
            "High risk"
        ]
        risk_stratification = st.selectbox("Risk Stratification:", [""] + risk_stratification_options, key="risk_stratification")
    
    # ========== COMMENTS SECTION ==========
    st.markdown('<div class="section-header"><h2>💬 COMMENTS</h2></div>', unsafe_allow_html=True)
    
    comments = st.text_area(
        "Comment(s):",
        height=150,
        placeholder="Enter any additional comments, pending studies, or other relevant information...",
        key="comments"
    )
    
    # ========== FINAL DIAGNOSIS SECTION ==========
    st.markdown('<div class="section-header"><h2>🎯 FINAL DIAGNOSIS</h2></div>', unsafe_allow_html=True)
    
    final_diagnosis = st.text_area(
        "Final Diagnosis:",
        height=100,
        placeholder="Enter the final pathological diagnosis...",
        key="final_diagnosis"
    )
    
    recommendations = st.text_area(
        "Clinical Recommendations:",
        height=100,
        placeholder="Enter clinical recommendations (follow-up, genetic testing, etc.)...",
        key="recommendations"
    )
    
    # ========== GENERATE REPORT SECTION ==========
    st.markdown("---")
    st.markdown("### 📋 Generate Final Report")
    
    # Large Generate Report Button
    if st.button("🫘 GENERATE COMPLETE KIDNEY PATHOLOGY REPORT", type="primary", use_container_width=True):
        st.success("✅ Complete kidney pathology report generated successfully!")
        
        # Large Report Display Area
        st.markdown("### 📄 KIDNEY TUMOR PATHOLOGY REPORT")
        
        # Create comprehensive report content
        report_content = f"""KIDNEY TUMOR PATHOLOGY REPORT
Date: {datetime.now().strftime('%Y-%m-%d')}
Standard: AJCC 8th Edition
Protocol Posting Date: June 2025

CASE SUMMARY (KIDNEY: Nephrectomy)
"""
        
        # Add Case Summary
        if st.session_state.get('case_id'):
            report_content += f"Case ID: {st.session_state.case_id}\n"
        if st.session_state.get('patient_name'):
            report_content += f"Patient Name: {st.session_state.patient_name}\n"
        if st.session_state.get('age'):
            report_content += f"Age: {st.session_state.age}\n"
        if st.session_state.get('gender'):
            report_content += f"Gender: {st.session_state.gender}\n"
        if st.session_state.get('date_of_procedure'):
            report_content += f"Date of Procedure: {st.session_state.date_of_procedure}\n"
        if st.session_state.get('pathologist'):
            report_content += f"Pathologist: {st.session_state.pathologist}\n"
        if st.session_state.get('clinical_diagnosis'):
            report_content += f"Clinical Diagnosis: {st.session_state.clinical_diagnosis}\n"
        
        # Add Specimen Section
        report_content += f"\nSPECIMEN\n"
        
        if st.session_state.get('procedure'):
            report_content += f"Procedure: {st.session_state.procedure}\n"
            if st.session_state.get('procedure_other') and st.session_state.procedure == "Other":
                report_content += f"  Details: {st.session_state.procedure_other}\n"
        
        if st.session_state.get('laterality'):
            report_content += f"Specimen Laterality: {st.session_state.laterality}\n"
            if st.session_state.get('laterality_other') and st.session_state.laterality == "Other":
                report_content += f"  Details: {st.session_state.laterality_other}\n"
        
        # Specimen dimensions
        if st.session_state.get('kidney_weight'):
            report_content += f"Kidney Weight: {st.session_state.kidney_weight} g\n"
        
        dimensions = []
        if st.session_state.get('kidney_length'):
            dimensions.append(f"{st.session_state.kidney_length}")
        if st.session_state.get('kidney_width'):
            dimensions.append(f"{st.session_state.kidney_width}")
        if st.session_state.get('kidney_height'):
            dimensions.append(f"{st.session_state.kidney_height}")
        
        if dimensions:
            report_content += f"Kidney Dimensions: {' x '.join(dimensions)} cm\n"
        
        # Add Tumor Section
        report_content += f"\nTUMOR\n"
        
        if st.session_state.get('focality'):
            report_content += f"Tumor Focality: {st.session_state.focality}\n"
            if st.session_state.get('tumor_number') and st.session_state.focality == "Multifocal":
                report_content += f"  Number of tumors: {st.session_state.tumor_number}\n"
        
        # Tumor Sites
        tumor_sites = []
        if st.session_state.get('site_upper_pole'):
            tumor_sites.append("Upper pole")
        if st.session_state.get('site_middle'):
            tumor_sites.append("Middle")
        if st.session_state.get('site_lower_pole'):
            tumor_sites.append("Lower pole")
        if st.session_state.get('site_other'):
            detail = st.session_state.get('other_site_detail', '')
            tumor_sites.append(f"Other ({detail})" if detail else "Other")
        if st.session_state.get('site_not_specified'):
            tumor_sites.append("Not specified")
        
        if tumor_sites:
            report_content += f"Tumor Site: {', '.join(tumor_sites)}\n"
        
        # Tumor Size
        if st.session_state.get('size_method') == "Greatest dimension in Centimeters (cm)":
            if st.session_state.get('greatest_dimension'):
                size_text = f"{st.session_state.greatest_dimension} cm"
                if st.session_state.get('additional_dims') and st.session_state.get('size_x') and st.session_state.get('size_y'):
                    size_text += f" x {st.session_state.size_x} cm x {st.session_state.size_y} cm"
                report_content += f"Tumor Size: {size_text}\n"
        elif st.session_state.get('size_method') == "Cannot be determined":
            report_content += "Tumor Size: Cannot be determined"
            if st.session_state.get('size_explain'):
                report_content += f" ({st.session_state.size_explain})"
            report_content += "\n"
        
        # Histologic Type
        histologic_types = []
        histologic_keys = [
            ('clear_cell_rcc', 'Clear cell renal cell carcinoma'),
            ('multilocular_cystic', 'Multilocular cystic renal neoplasm of low malignant potential'),
            ('papillary_rcc', 'Papillary renal cell carcinoma'),
            ('chromophobe_rcc', 'Chromophobe renal cell carcinoma'),
            ('other_oncocytic', 'Other oncocytic tumors'),
            ('collecting_duct', 'Collecting duct carcinoma'),
            ('clear_cell_papillary', 'Clear cell papillary renal cell tumor'),
            ('mucinous_tubular', 'Mucinous tubular and spindle renal cell carcinoma'),
            ('tubulocystic', 'Tubulocystic renal cell carcinoma'),
            ('acquired_cystic', 'Acquired cystic disease-associated renal cell carcinoma'),
            ('eosinophilic_solid', 'Eosinophilic solid and cystic renal cell carcinoma'),
            ('rcc_nos', 'Renal cell carcinoma, NOS'),
            ('tfe3_rearranged', 'TFE3-rearranged renal cell carcinoma'),
            ('tfeb_altered', 'TFEB-altered renal cell carcinoma'),
            ('eloc_mutated', 'ELOC-mutated renal cell carcinoma'),
            ('fh_deficient', 'Fumarate hydratase-deficient renal cell carcinoma'),
            ('sdh_deficient', 'SDH-deficient renal cell carcinoma'),
            ('alk_rearranged', 'ALK-rearranged renal cell carcinoma'),
            ('smarcb1_deficient', 'SMARCB1-deficient renal medullary carcinoma'),
            ('subtype_pending', 'Renal cell carcinoma, subtype pending additional studies'),
            ('other_histologic', 'Other histologic type')
        ]
        
        for key, name in histologic_keys:
            if st.session_state.get(key):
                histologic_types.append(name)
        
        if histologic_types:
            report_content += f"Histologic Type: {', '.join(histologic_types)}\n"
        
        if st.session_state.get('histologic_comment'):
            report_content += f"Histologic Type Comment: {st.session_state.histologic_comment}\n"
        
        if st.session_state.get('grade'):
            report_content += f"Histologic Grade: {st.session_state.grade}\n"
            if st.session_state.get('g4_specify') and "G4" in str(st.session_state.grade):
                report_content += f"  G4 Features: {st.session_state.g4_specify}\n"
        
        if st.session_state.get('grade_comment'):
            report_content += f"Histologic Grade Comment: {st.session_state.grade_comment}\n"
        
        # Tumor Extent
        extent_findings = []
        extent_keys = [
            ('extent_limited_kidney', 'Limited to kidney'),
            ('extent_perinephric', 'Extends into perinephric tissue'),
            ('extent_renal_sinus', 'Extends into renal sinus'),
            ('extent_pelvicalyceal', 'Extends into pelvicalyceal system'),
            ('extent_renal_vein', 'Extends into renal vein'),
            ('extent_ivc', 'Extends into inferior vena cava'),
            ('extent_gerota', 'Extends beyond Gerota\'s fascia'),
            ('extent_adrenal_direct', 'Directly invades adrenal gland (T4)'),
            ('extent_adrenal_noncontiguous', 'Involves adrenal gland non-contiguously (M1)'),
            ('extent_other_organs', 'Extends into other organs/structures')
        ]
        
        for key, name in extent_keys:
            if st.session_state.get(key):
                extent_findings.append(name)
        
        if extent_findings:
            report_content += f"Tumor Extent: {', '.join(extent_findings)}\n"
        
        # Histologic Features
        if st.session_state.get('sarcomatoid_present'):
            report_content += f"Sarcomatoid Features: Present"
            if st.session_state.get('sarcomatoid_percentage'):
                report_content += f" ({st.session_state.sarcomatoid_percentage}%)"
            report_content += "\n"
        
        if st.session_state.get('rhabdoid_present'):
            report_content += f"Rhabdoid Features: Present"
            if st.session_state.get('rhabdoid_percentage'):
                report_content += f" ({st.session_state.rhabdoid_percentage}%)"
            report_content += "\n"
        
        if st.session_state.get('no_sarcomatoid_rhabdoid'):
            report_content += "Sarcomatoid or rhabdoid features: Not identified\n"
        
        # Tumor Necrosis
        if st.session_state.get('necrosis'):
            report_content += f"Tumor Necrosis: {st.session_state.necrosis}"
            if st.session_state.get('necrosis_percentage') and st.session_state.necrosis == "Present":
                report_content += f" ({st.session_state.necrosis_percentage}%)"
            report_content += "\n"
        
        if st.session_state.get('vascular_invasion'):
            report_content += f"Lymphatic and/or Vascular Invasion: {st.session_state.vascular_invasion}\n"
        
        if st.session_state.get('tumor_comment'):
            report_content += f"Tumor Comment: {st.session_state.tumor_comment}\n"
        
        # Add Margins Section
        report_content += f"\nMARGINS\n"
        
        if st.session_state.get('margin_status'):
            report_content += f"Margin Status: {st.session_state.margin_status}\n"
        
        if st.session_state.get('margin_comment'):
            report_content += f"Margin Comment: {st.session_state.margin_comment}\n"
        
        # Add Regional Lymph Nodes Section
        report_content += f"\nREGIONAL LYMPH NODES\n"
        
        if st.session_state.get('ln_status'):
            report_content += f"Regional Lymph Node Status: {st.session_state.ln_status}\n"
            
            if st.session_state.get('ln_tumor_status'):
                report_content += f"  Tumor Status: {st.session_state.ln_tumor_status}\n"
            
            if st.session_state.get('ln_positive_exact'):
                report_content += f"  Number of positive nodes: {st.session_state.ln_positive_exact}\n"
            if st.session_state.get('ln_examined_exact'):
                report_content += f"  Number of nodes examined: {st.session_state.ln_examined_exact}\n"
        
        if st.session_state.get('ln_comment'):
            report_content += f"Regional Lymph Node Comment: {st.session_state.ln_comment}\n"
        
        # Add Distant Metastasis Section
        report_content += f"\nDISTANT METASTASIS\n"
        
        if st.session_state.get('dm_not_applicable'):
            report_content += "Distant Site(s) Involved: Not applicable\n"
        elif st.session_state.get('dm_specify') and st.session_state.get('dm_sites'):
            report_content += f"Distant Site(s) Involved: {st.session_state.dm_sites}\n"
        
        # Add pTNM Classification Section
        report_content += f"\npTNM CLASSIFICATION (AJCC 8th Edition)\n"
        
        report_content += "Reporting of pT, pN, and (when applicable) pM categories is based on information\navailable to the pathologist at the time the report is issued.\n\n"
        
        # Modified classification
        modifiers = []
        if st.session_state.get('modified_y'):
            modifiers.append("y (post-neoadjuvant therapy)")
        if st.session_state.get('modified_r'):
            modifiers.append("r (recurrence)")
        
        if modifiers:
            report_content += f"Modified Classification: {', '.join(modifiers)}\n"
        
        if st.session_state.get('pt_category'):
            report_content += f"pT: {st.session_state.pt_category}\n"
        if st.session_state.get('pn_category'):
            report_content += f"pN: {st.session_state.pn_category}\n"
        if st.session_state.get('pm_category'):
            report_content += f"pM: {st.session_state.pm_category}\n"
        
        # Add Additional Findings Section
        report_content += f"\nADDITIONAL FINDINGS\n"
        
        additional_findings = []
        if st.session_state.get('additional_insufficient'):
            additional_findings.append("Insufficient tissue")
        if st.session_state.get('additional_no_change'):
            additional_findings.append("No significant pathologic change identified")
        if st.session_state.get('additional_glomerular'):
            detail = st.session_state.get('glomerular_type', '')
            if detail:
                additional_findings.append(f"Glomerular disease ({detail})")
            else:
                additional_findings.append("Glomerular disease")
        if st.session_state.get('additional_tubulointerstitial'):
            detail = st.session_state.get('tubulointerstitial_type', '')
            if detail:
                additional_findings.append(f"Tubulointerstitial disease ({detail})")
            else:
                additional_findings.append("Tubulointerstitial disease")
        if st.session_state.get('additional_vascular'):
            detail = st.session_state.get('vascular_type', '')
            if detail:
                additional_findings.append(f"Vascular disease ({detail})")
            else:
                additional_findings.append("Vascular disease")
        if st.session_state.get('additional_cysts'):
            detail = st.session_state.get('cysts_type', '')
            if detail:
                additional_findings.append(f"Cyst(s) ({detail})")
            else:
                additional_findings.append("Cyst(s)")
        if st.session_state.get('additional_adenomas'):
            additional_findings.append("Papillary adenoma(s)")
        if st.session_state.get('additional_other'):
            detail = st.session_state.get('additional_other_detail', '')
            if detail:
                additional_findings.append(f"Other ({detail})")
            else:
                additional_findings.append("Other")
        
        if additional_findings:
            report_content += f"Additional Findings in Kidney: {', '.join(additional_findings)}\n"
        
        # Add Immunohistochemistry Section
        if st.session_state.get('ihc_performed'):
            report_content += f"\nIMMUNOHISTOCHEMISTRY\n"
            
            ihc_results = []
            if st.session_state.get('cd10_antibody') and st.session_state.get('cd10_result'):
                intensity = st.session_state.get('cd10_intensity', '')
                percentage = st.session_state.get('cd10_percentage', '')
                result_text = f"CD10: {st.session_state.cd10_result}"
                if intensity:
                    result_text += f" ({intensity})"
                if percentage:
                    result_text += f" {percentage}%"
                ihc_results.append(result_text)
            
            if st.session_state.get('ck7_antibody') and st.session_state.get('ck7_result'):
                intensity = st.session_state.get('ck7_intensity', '')
                percentage = st.session_state.get('ck7_percentage', '')
                result_text = f"CK7: {st.session_state.ck7_result}"
                if intensity:
                    result_text += f" ({intensity})"
                if percentage:
                    result_text += f" {percentage}%"
                ihc_results.append(result_text)
            
            if st.session_state.get('vimentin_antibody') and st.session_state.get('vimentin_result'):
                intensity = st.session_state.get('vimentin_intensity', '')
                percentage = st.session_state.get('vimentin_percentage', '')
                result_text = f"Vimentin: {st.session_state.vimentin_result}"
                if intensity:
                    result_text += f" ({intensity})"
                if percentage:
                    result_text += f" {percentage}%"
                ihc_results.append(result_text)
            
            if st.session_state.get('pax8_antibody') and st.session_state.get('pax8_result'):
                intensity = st.session_state.get('pax8_intensity', '')
                percentage = st.session_state.get('pax8_percentage', '')
                result_text = f"PAX8: {st.session_state.pax8_result}"
                if intensity:
                    result_text += f" ({intensity})"
                if percentage:
                    result_text += f" {percentage}%"
                ihc_results.append(result_text)
            
            if st.session_state.get('rcc_antibody') and st.session_state.get('rcc_result'):
                intensity = st.session_state.get('rcc_intensity', '')
                percentage = st.session_state.get('rcc_percentage', '')
                result_text = f"RCC Marker: {st.session_state.rcc_result}"
                if intensity:
                    result_text += f" ({intensity})"
                if percentage:
                    result_text += f" {percentage}%"
                ihc_results.append(result_text)
            
            if ihc_results:
                for result in ihc_results:
                    report_content += f"  {result}\n"
            
            if st.session_state.get('other_ihc'):
                report_content += f"Other IHC: {st.session_state.other_ihc}\n"
        
        # Add Molecular Testing Section
        if st.session_state.get('molecular_performed'):
            report_content += f"\nMOLECULAR TESTING\n"
            
            if st.session_state.get('vhl_testing') and st.session_state.get('vhl_result'):
                report_content += f"VHL gene mutation testing: {st.session_state.vhl_result}\n"
            
            if st.session_state.get('other_molecular'):
                report_content += f"Other Molecular Markers: {st.session_state.other_molecular}\n"
        
        # Add Prognostic Assessment Section
        if st.session_state.get('prognostic_assessment'):
            report_content += f"\nPROGNOSTIC ASSESSMENT\n"
            
            if st.session_state.get('tumor_size_score'):
                report_content += f"Tumor Size Score: {st.session_state.tumor_size_score}\n"
            if st.session_state.get('grade_score'):
                report_content += f"Grade Score: {st.session_state.grade_score}\n"
            if st.session_state.get('stage_score'):
                report_content += f"Stage Score: {st.session_state.stage_score}\n"
            if st.session_state.get('overall_score'):
                report_content += f"Overall Prognostic Score: {st.session_state.overall_score}\n"
            if st.session_state.get('risk_stratification'):
                report_content += f"Risk Stratification: {st.session_state.risk_stratification}\n"
        
        # Add Final Diagnosis Section
        if st.session_state.get('final_diagnosis'):
            report_content += f"\nFINAL DIAGNOSIS\n"
            report_content += str(st.session_state.final_diagnosis) + "\n"
        
        # Add Clinical Recommendations Section
        if st.session_state.get('recommendations'):
            report_content += f"\nCLINICAL RECOMMENDATIONS\n"
            report_content += str(st.session_state.recommendations) + "\n"
        
        # Add Comments Section
        if st.session_state.get('comments'):
            report_content += f"\nCOMMENTS\n"
            report_content += str(st.session_state.comments) + "\n"
        
        report_content += f"\nEnd of Report\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        
        # Display the report
        st.text_area(
            "Complete Kidney Pathology Report:",
            value=report_content,
            height=600,
            key="final_report"
        )
        
        # Download button
        st.download_button(
            label="📥 Download Report as Text File",
            data=report_content,
            file_name=f"kidney_pathology_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )

if __name__ == "__main__":
    main()