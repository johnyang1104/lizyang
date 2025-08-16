import streamlit as st
import json
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Hepatocellular Carcinoma Pathology Reporting Checklist",
    page_icon="🔬",
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
    .tumor-section {
        background-color: #fff3cd;
        padding: 0.5rem 1rem;
        border-radius: 3px;
        margin: 1rem 0;
        border-left: 3px solid #ffc107;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("🔬 Hepatocellular Carcinoma Pathology Reporting Checklist")
    st.markdown("**AJCC-UICC 8th Edition Standard** | Protocol Posting Date: June 2022")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Initialize session state for form data
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    
    # ========== CASE SUMMARY SECTION ==========
    st.markdown('<div class="section-header"><h2>📋 CASE SUMMARY</h2></div>', unsafe_allow_html=True)
    st.markdown("**(HEPATOCELLULAR CARCINOMA)**")
    st.markdown("**Standard(s): AJCC-UICC 8**")
    
    col1, col2 = st.columns(2)
    with col1:
        case_id = st.text_input("Case ID:", key="case_id")
        patient_name = st.text_input("Patient Name:", key="patient_name")
        liver_location = st.selectbox("Liver Location:", ["", "Liver"], key="liver_location")
    with col2:
        date_of_procedure = st.date_input("Date of Procedure:", key="date_of_procedure")
        pathologist = st.text_input("Pathologist:", key="pathologist")
    
    # ========== SPECIMEN SECTION ==========
    st.markdown('<div class="section-header"><h2>🧪 SPECIMEN</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><h4>Procedure (select all that apply)</h4></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        wedge_resection = st.checkbox("Wedge resection", key="wedge_resection")
        partial_major = st.checkbox("Partial hepatectomy, major (3 segments or more)", key="partial_major")
        partial_minor = st.checkbox("Partial hepatectomy, minor (less than 3 segments)", key="partial_minor")
        partial_nos = st.checkbox("Partial hepatectomy (not otherwise specified)", key="partial_nos")
    
    with col2:
        total_hepatectomy = st.checkbox("Total hepatectomy", key="total_hepatectomy")
        procedure_other = st.checkbox("Other (specify)", key="procedure_other")
        if procedure_other:
            procedure_other_specify = st.text_input("Specify other procedure:", key="procedure_other_specify")
        procedure_not_specified = st.checkbox("Not specified", key="procedure_not_specified")
    
    # ========== TUMOR SECTION ==========
    st.markdown('<div class="section-header"><h2>🎯 TUMOR</h2></div>', unsafe_allow_html=True)
    
    # Histologic Type
    st.markdown('<div class="subsection"><h4>Histologic Type</h4></div>', unsafe_allow_html=True)
    histologic_options = [
        "Hepatocellular carcinoma",
        "Hepatocellular carcinoma, fibrolamellar",
        "Hepatocellular carcinoma, scirrhous",
        "Hepatocellular carcinoma, clear cell type",
        "Other histologic type not listed",
        "Carcinoma, type cannot be determined"
    ]
    histologic_type = st.selectbox("Histologic Type:", [""] + histologic_options, key="histologic_type")
    
    if histologic_type == "Other histologic type not listed":
        histologic_other = st.text_input("Specify other type:", key="histologic_other")
    elif histologic_type == "Carcinoma, type cannot be determined":
        histologic_cannot = st.text_input("Explain:", key="histologic_cannot")
    
    histologic_comment = st.text_area("Histologic Type Comment:", key="histologic_comment")
    
    # Histologic Grade
    st.markdown('<div class="subsection"><h4>Histologic Grade</h4></div>', unsafe_allow_html=True)
    st.info("For multiple tumors, select the worst grade.")
    
    grade_options = [
        "G1, well differentiated",
        "G2, moderately differentiated",
        "G3, poorly differentiated",
        "G4, undifferentiated",
        "Other",
        "GX, cannot be assessed",
        "Not applicable"
    ]
    grade = st.selectbox("Histologic Grade:", [""] + grade_options, key="grade")
    
    if grade == "Other":
        grade_other = st.text_input("Specify other grade:", key="grade_other")
    elif grade == "GX, cannot be assessed":
        grade_cannot = st.text_input("Explain:", key="grade_cannot")
    elif grade == "Not applicable":
        grade_not_applicable = st.text_input("Explain:", key="grade_not_applicable")
    
    # Tumor Focality
    st.markdown('<div class="subsection"><h4>Tumor Focality</h4></div>', unsafe_allow_html=True)
    focality_options = ["Solitary", "Multiple", "Cannot be determined"]
    focality = st.selectbox("Tumor Focality:", [""] + focality_options, key="focality")
    
    if focality == "Multiple":
        focality_multiple = st.text_input("Describe multiple tumors:", key="focality_multiple")
    elif focality == "Cannot be determined":
        focality_cannot = st.text_input("Explain:", key="focality_cannot")
    
    # ========== TUMOR CHARACTERISTICS SECTION ==========
    st.markdown('<div class="section-header"><h2>📊 TUMOR CHARACTERISTICS</h2></div>', unsafe_allow_html=True)
    st.info("For multiple tumors, repeat this section for up to 5 largest tumor nodules.")
    
    # Number of tumor nodules to document
    num_tumors = st.number_input("Number of tumor nodules to document (max 5):", min_value=1, max_value=5, value=1, key="num_tumors")
    
    # Create tabs for each tumor
    if num_tumors > 1:
        tumor_tabs = st.tabs([f"Tumor {i+1}" for i in range(num_tumors)])
    else:
        tumor_tabs = [st.container()]
    
    for i, tab in enumerate(tumor_tabs):
        with tab:
            st.markdown(f'<div class="tumor-section"><h4>Tumor {i+1} Characteristics</h4></div>', unsafe_allow_html=True)
            
            # Tumor Identification
            tumor_id = st.text_input(f"Tumor {i+1} Identification:", key=f"tumor_id_{i}")
            
            # Tumor Site
            st.write("**Tumor Site:**")
            col1, col2 = st.columns(2)
            
            with col1:
                right_lobe = st.checkbox(f"Right lobe", key=f"right_lobe_{i}")
                if right_lobe:
                    right_lobe_detail = st.text_input(f"Right lobe details:", key=f"right_lobe_detail_{i}")
                
                left_lobe = st.checkbox(f"Left lobe", key=f"left_lobe_{i}")
                if left_lobe:
                    left_lobe_detail = st.text_input(f"Left lobe details:", key=f"left_lobe_detail_{i}")
                
                caudate_lobe = st.checkbox(f"Caudate lobe", key=f"caudate_lobe_{i}")
                if caudate_lobe:
                    caudate_lobe_detail = st.text_input(f"Caudate lobe details:", key=f"caudate_lobe_detail_{i}")
            
            with col2:
                quadrate_lobe = st.checkbox(f"Quadrate lobe", key=f"quadrate_lobe_{i}")
                if quadrate_lobe:
                    quadrate_lobe_detail = st.text_input(f"Quadrate lobe details:", key=f"quadrate_lobe_detail_{i}")
                
                segmental_location = st.checkbox(f"Segmental location (specify)", key=f"segmental_location_{i}")
                if segmental_location:
                    segmental_detail = st.text_input(f"Segmental location details:", key=f"segmental_detail_{i}")
                
                site_other = st.checkbox(f"Other (specify)", key=f"site_other_{i}")
                if site_other:
                    site_other_detail = st.text_input(f"Other site details:", key=f"site_other_detail_{i}")
            
            # Tumor Size
            st.write("**Tumor Size:**")
            size_method = st.radio(
                f"Size measurement method for Tumor {i+1}:",
                ["Greatest dimension of viable tumor in cm", "Cannot be determined"],
                key=f"size_method_{i}"
            )
            
            if size_method == "Greatest dimension of viable tumor in cm":
                size_cm = st.number_input(f"Greatest dimension (cm):", min_value=0.0, step=0.1, key=f"size_cm_{i}")
                
                # Additional dimensions
                additional_dims = st.checkbox(f"Additional dimensions", key=f"additional_dims_{i}")
                if additional_dims:
                    col1, col2 = st.columns(2)
                    with col1:
                        size_x = st.number_input(f"Width (cm):", min_value=0.0, step=0.1, key=f"size_x_{i}")
                    with col2:
                        size_y = st.number_input(f"Height (cm):", min_value=0.0, step=0.1, key=f"size_y_{i}")
                
                # Greatest dimension on gross exam
                gross_size = st.number_input(f"Greatest dimension on gross exam (cm):", min_value=0.0, step=0.1, key=f"gross_size_{i}")
            else:
                size_explain = st.text_input(f"Explain why size cannot be determined:", key=f"size_explain_{i}")
            
            # Treatment Effect
            st.write("**Treatment Effect:**")
            treatment_options = [
                "No known presurgical therapy",
                "Complete necrosis (no viable tumor)",
                "Incomplete necrosis (viable tumor present)",
                "No necrosis",
                "Cannot be determined"
            ]
            treatment_effect = st.selectbox(f"Treatment Effect for Tumor {i+1}:", [""] + treatment_options, key=f"treatment_effect_{i}")
            
            if treatment_effect == "Incomplete necrosis (viable tumor present)":
                st.write("**Extent of Tumor Necrosis:**")
                necrosis_method = st.radio(
                    f"Necrosis extent method:",
                    ["Specify percentage", "Other", "Cannot be determined"],
                    key=f"necrosis_method_{i}"
                )
                
                if necrosis_method == "Specify percentage":
                    necrosis_percent = st.number_input(f"Necrosis percentage:", min_value=0, max_value=100, key=f"necrosis_percent_{i}")
                elif necrosis_method == "Other":
                    necrosis_other = st.text_input(f"Specify other:", key=f"necrosis_other_{i}")
                elif necrosis_method == "Cannot be determined":
                    necrosis_cannot = st.text_input(f"Explain:", key=f"necrosis_cannot_{i}")
            
            elif treatment_effect == "Cannot be determined":
                treatment_explain = st.text_input(f"Explain:", key=f"treatment_explain_{i}")
            
            # Satellitosis
            st.write("**Satellitosis:**")
            satellitosis_options = ["Not identified", "Present", "Cannot be determined"]
            satellitosis = st.selectbox(f"Satellitosis for Tumor {i+1}:", [""] + satellitosis_options, key=f"satellitosis_{i}")
            
            # Tumor Extent
            st.write("**Tumor Extent (select all that apply):**")
            
            col1, col2 = st.columns(2)
            with col1:
                confined_liver = st.checkbox(f"Confined to liver", key=f"confined_liver_{i}")
                major_portal = st.checkbox(f"Involves a major branch of the portal vein", key=f"major_portal_{i}")
                hepatic_vein = st.checkbox(f"Involves hepatic vein(s)", key=f"hepatic_vein_{i}")
                visceral_peritoneum = st.checkbox(f"Perforates visceral peritoneum", key=f"visceral_peritoneum_{i}")
            
            with col2:
                gallbladder = st.checkbox(f"Directly invades gallbladder", key=f"gallbladder_{i}")
                diaphragm = st.checkbox(f"Directly invades diaphragm", key=f"diaphragm_{i}")
                adjacent_organs = st.checkbox(f"Directly invades other adjacent organ(s)", key=f"adjacent_organs_{i}")
                if adjacent_organs:
                    adjacent_specify = st.text_input(f"Specify adjacent organs:", key=f"adjacent_specify_{i}")
                
                extent_cannot = st.checkbox(f"Cannot be determined", key=f"extent_cannot_{i}")
                if extent_cannot:
                    extent_explain = st.text_input(f"Explain:", key=f"extent_explain_{i}")
                
                no_primary = st.checkbox(f"No evidence of primary tumor", key=f"no_primary_{i}")
            
            # Vascular Invasion
            st.write("**Vascular Invasion (select all that apply):**")
            
            vascular_not_identified = st.checkbox(f"Not identified", key=f"vascular_not_identified_{i}")
            
            vascular_small = st.checkbox(f"Small vessel", key=f"vascular_small_{i}")
            if vascular_small:
                vascular_small_detail = st.text_input(f"Small vessel details:", key=f"vascular_small_detail_{i}")
            
            vascular_large = st.checkbox(f"Large vessel (major branch of hepatic vein or portal vein)", key=f"vascular_large_{i}")
            if vascular_large:
                vascular_large_detail = st.text_input(f"Large vessel details:", key=f"vascular_large_detail_{i}")
            
            vascular_present_nos = st.checkbox(f"Present (not otherwise specified)", key=f"vascular_present_nos_{i}")
            if vascular_present_nos:
                vascular_nos_detail = st.text_input(f"Present NOS details:", key=f"vascular_nos_detail_{i}")
            
            vascular_cannot = st.checkbox(f"Cannot be determined", key=f"vascular_cannot_{i}")
            if vascular_cannot:
                vascular_cannot_detail = st.text_input(f"Vascular invasion cannot be determined - explain:", key=f"vascular_cannot_detail_{i}")
            
            # Perineural Invasion
            st.write("**Perineural Invasion:**")
            pni_options = ["Not identified", "Present", "Cannot be determined"]
            pni = st.selectbox(f"Perineural Invasion for Tumor {i+1}:", [""] + pni_options, key=f"pni_{i}")
            if pni == "Present":
                pni_detail = st.text_input(f"Perineural invasion details:", key=f"pni_detail_{i}")
            elif pni == "Cannot be determined":
                pni_explain = st.text_input(f"Explain:", key=f"pni_explain_{i}")
            
            # Tumor Comment for this nodule
            tumor_comment = st.text_area(f"Tumor {i+1} Comment:", key=f"tumor_comment_{i}")
    
    # ========== MARGINS SECTION ==========
    st.markdown('<div class="section-header"><h2>📏 MARGINS</h2></div>', unsafe_allow_html=True)
    
    # Margin Status
    st.markdown('<div class="subsection"><h4>Margin Status</h4></div>', unsafe_allow_html=True)
    
    margin_status = st.radio(
        "Margin status:",
        [
            "All margins negative for invasive carcinoma",
            "Invasive carcinoma present at margin",
            "Other",
            "Cannot be determined",
            "Not applicable"
        ],
        key="margin_status"
    )
    
    if margin_status == "All margins negative for invasive carcinoma":
        st.write("**Closest Margin(s) to Invasive Carcinoma (select all that apply):**")
        
        parenchymal_closest = st.checkbox("Parenchymal", key="parenchymal_closest")
        if parenchymal_closest:
            parenchymal_detail = st.text_input("Parenchymal details:", key="parenchymal_detail")
        
        margin_other_closest = st.checkbox("Other (specify)", key="margin_other_closest")
        if margin_other_closest:
            margin_other_detail = st.text_input("Other margin details:", key="margin_other_detail")
        
        margin_closest_cannot = st.checkbox("Cannot be determined", key="margin_closest_cannot")
        if margin_closest_cannot:
            margin_closest_explain = st.text_input("Explain:", key="margin_closest_explain")
        
        # Distance from Invasive Carcinoma to Closest Margin
        st.write("**Distance from Invasive Carcinoma to Closest Margin:**")
        
        distance_method = st.radio(
            "Distance measurement:",
            [
                "Exact distance in cm",
                "Greater than 1 cm",
                "Exact distance in mm",
                "Greater than 10 mm",
                "Other",
                "Cannot be determined"
            ],
            key="distance_method"
        )
        
        if distance_method == "Exact distance in cm":
            distance_cm = st.number_input("Distance (cm):", min_value=0.0, step=0.1, key="distance_cm")
        elif distance_method == "Exact distance in mm":
            distance_mm = st.number_input("Distance (mm):", min_value=0.0, step=0.1, key="distance_mm")
        elif distance_method == "Other":
            distance_other = st.text_input("Specify other:", key="distance_other")
        elif distance_method == "Cannot be determined":
            distance_explain = st.text_input("Explain:", key="distance_explain")
    
    elif margin_status == "Invasive carcinoma present at margin":
        st.write("**Margin(s) Involved by Invasive Carcinoma (select all that apply):**")
        
        parenchymal_involved = st.checkbox("Parenchymal", key="parenchymal_involved")
        if parenchymal_involved:
            parenchymal_involved_detail = st.text_input("Parenchymal involved details:", key="parenchymal_involved_detail")
        
        margin_involved_other = st.checkbox("Other (specify)", key="margin_involved_other")
        if margin_involved_other:
            margin_involved_other_detail = st.text_input("Other involved margin details:", key="margin_involved_other_detail")
        
        margin_involved_cannot = st.checkbox("Cannot be determined", key="margin_involved_cannot")
        if margin_involved_cannot:
            margin_involved_explain = st.text_input("Explain:", key="margin_involved_explain")
    
    elif margin_status == "Other":
        margin_other_specify = st.text_input("Specify other:", key="margin_other_specify")
    elif margin_status == "Cannot be determined":
        margin_cannot_explain = st.text_input("Explain:", key="margin_cannot_explain")
    
    # Margin Comment
    margin_comment = st.text_area("Margin Comment:", key="margin_comment")
    
    # ========== REGIONAL LYMPH NODES SECTION ==========
    st.markdown('<div class="section-header"><h2>🔗 REGIONAL LYMPH NODES</h2></div>', unsafe_allow_html=True)
    
    # Regional Lymph Node Status
    st.markdown('<div class="subsection"><h4>Regional Lymph Node Status</h4></div>', unsafe_allow_html=True)
    
    ln_status = st.radio(
        "Regional lymph node status:",
        [
            "Not applicable (no regional lymph nodes submitted or found)",
            "Regional lymph nodes present",
            "Other",
            "Cannot be determined"
        ],
        key="ln_status"
    )
    
    if ln_status == "Regional lymph nodes present":
        ln_tumor_status = st.radio(
            "Tumor in lymph nodes:",
            [
                "All regional lymph nodes negative for tumor",
                "Tumor present in regional lymph node(s)"
            ],
            key="ln_tumor_status"
        )
        
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
    
    elif ln_status == "Other":
        ln_other_specify = st.text_input("Specify other:", key="ln_other_specify")
    elif ln_status == "Cannot be determined":
        ln_cannot_explain = st.text_input("Explain:", key="ln_cannot_explain")
    
    # Regional Lymph Node Comment
    ln_comment = st.text_area("Regional Lymph Node Comment:", key="ln_comment")
    
    # ========== DISTANT METASTASIS SECTION ==========
    st.markdown('<div class="section-header"><h2>🎯 DISTANT METASTASIS</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><h4>Distant Site(s) Involved, if applicable (select all that apply)</h4></div>', unsafe_allow_html=True)
    
    dm_not_applicable = st.checkbox("Not applicable", key="dm_not_applicable")
    
    dm_non_regional_ln = st.checkbox("Non-regional lymph node(s)", key="dm_non_regional_ln")
    if dm_non_regional_ln:
        dm_non_regional_detail = st.text_input("Non-regional lymph node details:", key="dm_non_regional_detail")
    
    dm_liver = st.checkbox("Liver", key="dm_liver")
    if dm_liver:
        dm_liver_detail = st.text_input("Liver metastasis details:", key="dm_liver_detail")
    
    dm_other = st.checkbox("Other", key="dm_other")
    if dm_other:
        dm_other_detail = st.text_input("Specify other distant sites:", key="dm_other_detail")
    
    dm_cannot_determine = st.checkbox("Cannot be determined", key="dm_cannot_determine")
    if dm_cannot_determine:
        dm_cannot_detail = st.text_input("Cannot be determined details:", key="dm_cannot_detail")
    
    # ========== pTNM CLASSIFICATION SECTION ==========
    st.markdown('<div class="section-header"><h2>📊 PATHOLOGIC STAGE CLASSIFICATION (pTNM, AJCC 8th Edition)</h2></div>', unsafe_allow_html=True)
    
    st.info("Reporting of pT, pN, and (when applicable) pM categories is based on information available to the pathologist at the time the report is issued. As per the AJCC (Chapter 1, 8th Ed.) it is the managing physician's responsibility to establish the final pathologic stage based upon all pertinent information, including but potentially not limited to this pathology report.")
    
    # TNM Descriptors
    st.markdown('<div class="subsection"><h4>TNM Descriptors (select all that apply)</h4></div>', unsafe_allow_html=True)
    
    tnm_not_applicable = st.checkbox("Not applicable", key="tnm_not_applicable")
    if tnm_not_applicable:
        tnm_not_applicable_detail = st.text_input("Not applicable details:", key="tnm_not_applicable_detail")
    
    tnm_m = st.checkbox("m (multiple primary tumors)", key="tnm_m")
    tnm_r = st.checkbox("r (recurrent)", key="tnm_r")
    tnm_y = st.checkbox("y (post-treatment)", key="tnm_y")
    
    # pT Category
    st.markdown('<div class="subsection"><h4>pT Category</h4></div>', unsafe_allow_html=True)
    
    pt_options = [
        "pT not assigned (cannot be determined based on available pathological information)",
        "pT0: No evidence of primary tumor",
        "pT1a: Solitary tumor less than or equal to 2 cm",
        "pT1b: Solitary tumor greater than 2 cm without vascular invasion",
        "pT1 (subcategory cannot be determined)",
        "pT2: Solitary tumor greater than 2 cm with vascular invasion, or multiple tumors, none greater than 5 cm",
        "pT3: Multiple tumors, at least one of which is greater than 5 cm",
        "pT4: Single tumor or multiple tumors of any size involving a major branch of the portal vein or hepatic vein, or tumor(s) with direct invasion of adjacent organs other than the gallbladder or with perforation of visceral peritoneum"
    ]
    
    pt_category = st.selectbox("pT Category:", [""] + pt_options, key="pt_category")
    
    # pN Category
    st.markdown('<div class="subsection"><h4>pN Category</h4></div>', unsafe_allow_html=True)
    
    pn_options = [
        "pN not assigned (no nodes submitted or found)",
        "pN not assigned (cannot be determined based on available pathological information)",
        "pN0: No regional lymph node metastasis",
        "pN1: Regional lymph node metastasis"
    ]
    
    pn_category = st.selectbox("pN Category:", [""] + pn_options, key="pn_category")
    
    # pM Category
    st.markdown('<div class="subsection"><h4>pM Category (required only if confirmed pathologically)</h4></div>', unsafe_allow_html=True)
    
    pm_options = [
        "Not applicable - pM cannot be determined from the submitted specimen(s)",
        "pM1: Distant metastasis"
    ]
    
    pm_category = st.selectbox("pM Category:", [""] + pm_options, key="pm_category")
    
    # ========== ADDITIONAL FINDINGS SECTION ==========
    st.markdown('<div class="section-header"><h2>🔍 ADDITIONAL FINDINGS</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><h4>Additional Findings (select all that apply)</h4></div>', unsafe_allow_html=True)
    
    additional_none = st.checkbox("None identified", key="additional_none")
    
    additional_fibrosis = st.checkbox("Fibrosis", key="additional_fibrosis")
    if additional_fibrosis:
        fibrosis_detail = st.text_input("Specify extent, providing name of the scheme and assessment scale used:", key="fibrosis_detail")
    
    additional_cirrhosis = st.checkbox("Cirrhosis", key="additional_cirrhosis")
    additional_lgd_nodule = st.checkbox("Low-grade dysplastic nodule", key="additional_lgd_nodule")
    additional_hgd_nodule = st.checkbox("High-grade dysplastic nodule", key="additional_hgd_nodule")
    additional_steatosis = st.checkbox("Steatosis", key="additional_steatosis")
    additional_steatohepatitis = st.checkbox("Steatohepatitis", key="additional_steatohepatitis")
    additional_iron = st.checkbox("Iron overload", key="additional_iron")
    
    additional_hepatitis = st.checkbox("Chronic hepatitis", key="additional_hepatitis")
    if additional_hepatitis:
        hepatitis_etiology = st.text_input("Specify etiology:", key="hepatitis_etiology")
    
    additional_other = st.checkbox("Other", key="additional_other")
    if additional_other:
        additional_other_detail = st.text_input("Specify other findings:", key="additional_other_detail")
    
    # ========== SPECIAL STUDIES SECTION ==========
    st.markdown('<div class="section-header"><h2>🔬 SPECIAL STUDIES</h2></div>', unsafe_allow_html=True)
    
    ancillary_studies = st.text_area("Ancillary Studies (specify):", key="ancillary_studies")
    
    # ========== COMMENTS SECTION ==========
    st.markdown('<div class="section-header"><h2>💬 COMMENTS</h2></div>', unsafe_allow_html=True)
    
    comments = st.text_area(
        "Comment(s):",
        height=150,
        placeholder="Enter any additional comments, pending studies, or other relevant information...",
        key="comments"
    )
    
    # ========== GENERATE REPORT SECTION ==========
    st.markdown("---")
    st.markdown("### 📋 Generate Final Report")
    
    # Large Generate Report Button
    if st.button("🔬 GENERATE COMPLETE PATHOLOGY REPORT", type="primary", use_container_width=True):
        st.success("✅ Complete pathology report generated successfully!")
        
        # Large Report Display Area
        st.markdown("### 📄 HEPATOCELLULAR CARCINOMA PATHOLOGY REPORT")
        
        # Create comprehensive report content
        report_content = f"""HEPATOCELLULAR CARCINOMA PATHOLOGY REPORT
Date: {datetime.now().strftime('%Y-%m-%d')}
Standard: AJCC-UICC 8th Edition
Protocol Posting Date: June 2022

CASE SUMMARY (HEPATOCELLULAR CARCINOMA)
"""
        
        # Add Case Summary
        if st.session_state.get('case_id'):
            report_content += f"Case ID: {st.session_state.case_id}\n"
        if st.session_state.get('patient_name'):
            report_content += f"Patient Name: {st.session_state.patient_name}\n"
        if st.session_state.get('date_of_procedure'):
            report_content += f"Date of Procedure: {st.session_state.date_of_procedure}\n"
        if st.session_state.get('pathologist'):
            report_content += f"Pathologist: {st.session_state.pathologist}\n"
        if st.session_state.get('liver_location'):
            report_content += f"Location: {st.session_state.liver_location}\n"
        
        # Add Specimen Section
        report_content += f"\nSPECIMEN\n"
        report_content += f"Procedure(s):\n"
        
        procedures = []
        if st.session_state.get('wedge_resection'):
            procedures.append("Wedge resection")
        if st.session_state.get('partial_major'):
            procedures.append("Partial hepatectomy, major (3 segments or more)")
        if st.session_state.get('partial_minor'):
            procedures.append("Partial hepatectomy, minor (less than 3 segments)")
        if st.session_state.get('partial_nos'):
            procedures.append("Partial hepatectomy (not otherwise specified)")
        if st.session_state.get('total_hepatectomy'):
            procedures.append("Total hepatectomy")
        if st.session_state.get('procedure_other'):
            if st.session_state.get('procedure_other_specify'):
                procedures.append(f"Other: {st.session_state.procedure_other_specify}")
            else:
                procedures.append("Other")
        if st.session_state.get('procedure_not_specified'):
            procedures.append("Not specified")
        
        if procedures:
            for proc in procedures:
                report_content += f"  - {proc}\n"
        
        # Add Tumor Section
        report_content += f"\nTUMOR\n"
        
        if st.session_state.get('histologic_type'):
            report_content += f"Histologic Type: {st.session_state.histologic_type}\n"
            if st.session_state.get('histologic_other') and st.session_state.histologic_type == "Other histologic type not listed":
                report_content += f"  Specified type: {st.session_state.histologic_other}\n"
            elif st.session_state.get('histologic_cannot') and st.session_state.histologic_type == "Carcinoma, type cannot be determined":
                report_content += f"  Explanation: {st.session_state.histologic_cannot}\n"
        
        if st.session_state.get('histologic_comment'):
            report_content += f"Histologic Type Comment: {st.session_state.histologic_comment}\n"
        
        if st.session_state.get('grade'):
            report_content += f"Histologic Grade: {st.session_state.grade}\n"
            if st.session_state.get('grade_other') and st.session_state.grade == "Other":
                report_content += f"  Specified grade: {st.session_state.grade_other}\n"
            elif st.session_state.get('grade_cannot') and st.session_state.grade == "GX, cannot be assessed":
                report_content += f"  Explanation: {st.session_state.grade_cannot}\n"
        
        if st.session_state.get('focality'):
            report_content += f"Tumor Focality: {st.session_state.focality}\n"
            if st.session_state.get('focality_multiple') and st.session_state.focality == "Multiple":
                report_content += f"  Details: {st.session_state.focality_multiple}\n"
            elif st.session_state.get('focality_cannot') and st.session_state.focality == "Cannot be determined":
                report_content += f"  Explanation: {st.session_state.focality_cannot}\n"
        
        # Add Tumor Characteristics for each documented tumor
        num_tumors = st.session_state.get('num_tumors', 1)
        for i in range(num_tumors):
            report_content += f"\nTUMOR {i+1} CHARACTERISTICS\n"
            
            if st.session_state.get(f'tumor_id_{i}'):
                report_content += f"Tumor Identification: {st.session_state[f'tumor_id_{i}']}\n"
            
            # Tumor sites for this tumor
            tumor_sites = []
            if st.session_state.get(f'right_lobe_{i}'):
                detail = st.session_state.get(f'right_lobe_detail_{i}', '')
                if detail:
                    tumor_sites.append(f"Right lobe ({detail})")
                else:
                    tumor_sites.append("Right lobe")
            
            if st.session_state.get(f'left_lobe_{i}'):
                detail = st.session_state.get(f'left_lobe_detail_{i}', '')
                if detail:
                    tumor_sites.append(f"Left lobe ({detail})")
                else:
                    tumor_sites.append("Left lobe")
            
            if st.session_state.get(f'caudate_lobe_{i}'):
                detail = st.session_state.get(f'caudate_lobe_detail_{i}', '')
                if detail:
                    tumor_sites.append(f"Caudate lobe ({detail})")
                else:
                    tumor_sites.append("Caudate lobe")
            
            if st.session_state.get(f'quadrate_lobe_{i}'):
                detail = st.session_state.get(f'quadrate_lobe_detail_{i}', '')
                if detail:
                    tumor_sites.append(f"Quadrate lobe ({detail})")
                else:
                    tumor_sites.append("Quadrate lobe")
            
            if st.session_state.get(f'segmental_location_{i}'):
                detail = st.session_state.get(f'segmental_detail_{i}', '')
                if detail:
                    tumor_sites.append(f"Segmental location: {detail}")
                else:
                    tumor_sites.append("Segmental location")
            
            if st.session_state.get(f'site_other_{i}'):
                detail = st.session_state.get(f'site_other_detail_{i}', '')
                if detail:
                    tumor_sites.append(f"Other: {detail}")
                else:
                    tumor_sites.append("Other")
            
            if tumor_sites:
                report_content += f"Tumor Site: {', '.join(tumor_sites)}\n"
            
            # Tumor Size
            if st.session_state.get(f'size_method_{i}') == "Greatest dimension of viable tumor in cm":
                if st.session_state.get(f'size_cm_{i}'):
                    size_text = f"{st.session_state[f'size_cm_{i}']} cm"
                    if st.session_state.get(f'additional_dims_{i}'):
                        if st.session_state.get(f'size_x_{i}') and st.session_state.get(f'size_y_{i}'):
                            size_text += f" x {st.session_state[f'size_x_{i}']} cm x {st.session_state[f'size_y_{i}']} cm"
                    report_content += f"Tumor Size: {size_text}\n"
                
                if st.session_state.get(f'gross_size_{i}'):
                    report_content += f"Greatest Dimension on Gross Exam: {st.session_state[f'gross_size_{i}']} cm\n"
            
            elif st.session_state.get(f'size_method_{i}') == "Cannot be determined":
                report_content += "Tumor Size: Cannot be determined"
                if st.session_state.get(f'size_explain_{i}'):
                    report_content += f" ({st.session_state[f'size_explain_{i}']})"
                report_content += "\n"
            
            # Treatment Effect
            if st.session_state.get(f'treatment_effect_{i}'):
                report_content += f"Treatment Effect: {st.session_state[f'treatment_effect_{i}']}\n"
                
                if st.session_state[f'treatment_effect_{i}'] == "Incomplete necrosis (viable tumor present)":
                    if st.session_state.get(f'necrosis_method_{i}') == "Specify percentage":
                        if st.session_state.get(f'necrosis_percent_{i}'):
                            report_content += f"  Extent of Tumor Necrosis: {st.session_state[f'necrosis_percent_{i}']}%\n"
                    elif st.session_state.get(f'necrosis_other_{i}'):
                        report_content += f"  Extent of Tumor Necrosis: {st.session_state[f'necrosis_other_{i}']}\n"
            
            # Satellitosis
            if st.session_state.get(f'satellitosis_{i}'):
                report_content += f"Satellitosis: {st.session_state[f'satellitosis_{i}']}\n"
            
            # Tumor Extent
            extent_findings = []
            if st.session_state.get(f'confined_liver_{i}'):
                extent_findings.append("Confined to liver")
            if st.session_state.get(f'major_portal_{i}'):
                extent_findings.append("Involves a major branch of the portal vein")
            if st.session_state.get(f'hepatic_vein_{i}'):
                extent_findings.append("Involves hepatic vein(s)")
            if st.session_state.get(f'visceral_peritoneum_{i}'):
                extent_findings.append("Perforates visceral peritoneum")
            if st.session_state.get(f'gallbladder_{i}'):
                extent_findings.append("Directly invades gallbladder")
            if st.session_state.get(f'diaphragm_{i}'):
                extent_findings.append("Directly invades diaphragm")
            if st.session_state.get(f'adjacent_organs_{i}'):
                if st.session_state.get(f'adjacent_specify_{i}'):
                    extent_findings.append(f"Directly invades other adjacent organ(s): {st.session_state[f'adjacent_specify_{i}']}")
                else:
                    extent_findings.append("Directly invades other adjacent organ(s)")
            if st.session_state.get(f'no_primary_{i}'):
                extent_findings.append("No evidence of primary tumor")
            
            if extent_findings:
                report_content += f"Tumor Extent: {', '.join(extent_findings)}\n"
            
            # Vascular Invasion
            vascular_findings = []
            if st.session_state.get(f'vascular_not_identified_{i}'):
                vascular_findings.append("Not identified")
            if st.session_state.get(f'vascular_small_{i}'):
                detail = st.session_state.get(f'vascular_small_detail_{i}', '')
                if detail:
                    vascular_findings.append(f"Small vessel ({detail})")
                else:
                    vascular_findings.append("Small vessel")
            if st.session_state.get(f'vascular_large_{i}'):
                detail = st.session_state.get(f'vascular_large_detail_{i}', '')
                if detail:
                    vascular_findings.append(f"Large vessel ({detail})")
                else:
                    vascular_findings.append("Large vessel (major branch of hepatic vein or portal vein)")
            if st.session_state.get(f'vascular_present_nos_{i}'):
                vascular_findings.append("Present (not otherwise specified)")
            
            if vascular_findings:
                report_content += f"Vascular Invasion: {', '.join(vascular_findings)}\n"
            
            # Perineural Invasion
            if st.session_state.get(f'pni_{i}'):
                report_content += f"Perineural Invasion: {st.session_state[f'pni_{i}']}\n"
                if st.session_state.get(f'pni_detail_{i}') and st.session_state[f'pni_{i}'] == "Present":
                    report_content += f"  Details: {st.session_state[f'pni_detail_{i}']}\n"
            
            # Tumor Comment
            if st.session_state.get(f'tumor_comment_{i}'):
                report_content += f"Tumor Comment: {st.session_state[f'tumor_comment_{i}']}\n"
        
        # Add Margins Section
        report_content += f"\nMARGINS\n"
        
        if st.session_state.get('margin_status'):
            report_content += f"Margin Status: {st.session_state.margin_status}\n"
            
            if st.session_state.margin_status == "All margins negative for invasive carcinoma":
                closest_margins = []
                if st.session_state.get('parenchymal_closest'):
                    detail = st.session_state.get('parenchymal_detail', '')
                    if detail:
                        closest_margins.append(f"Parenchymal ({detail})")
                    else:
                        closest_margins.append("Parenchymal")
                
                if st.session_state.get('margin_other_closest'):
                    detail = st.session_state.get('margin_other_detail', '')
                    if detail:
                        closest_margins.append(f"Other ({detail})")
                    else:
                        closest_margins.append("Other")
                
                if closest_margins:
                    report_content += f"  Closest Margin(s): {', '.join(closest_margins)}\n"
                
                # Distance information
                if st.session_state.get('distance_method'):
                    if st.session_state.distance_method == "Exact distance in cm" and st.session_state.get('distance_cm'):
                        report_content += f"  Distance to Closest Margin: {st.session_state.distance_cm} cm\n"
                    elif st.session_state.distance_method == "Exact distance in mm" and st.session_state.get('distance_mm'):
                        report_content += f"  Distance to Closest Margin: {st.session_state.distance_mm} mm\n"
                    elif st.session_state.distance_method == "Greater than 1 cm":
                        report_content += f"  Distance to Closest Margin: Greater than 1 cm\n"
                    elif st.session_state.distance_method == "Greater than 10 mm":
                        report_content += f"  Distance to Closest Margin: Greater than 10 mm\n"
            
            elif st.session_state.margin_status == "Invasive carcinoma present at margin":
                involved_margins = []
                if st.session_state.get('parenchymal_involved'):
                    detail = st.session_state.get('parenchymal_involved_detail', '')
                    if detail:
                        involved_margins.append(f"Parenchymal ({detail})")
                    else:
                        involved_margins.append("Parenchymal")
                
                if st.session_state.get('margin_involved_other'):
                    detail = st.session_state.get('margin_involved_other_detail', '')
                    if detail:
                        involved_margins.append(f"Other ({detail})")
                    else:
                        involved_margins.append("Other")
                
                if involved_margins:
                    report_content += f"  Involved Margin(s): {', '.join(involved_margins)}\n"
        
        if st.session_state.get('margin_comment'):
            report_content += f"Margin Comment: {st.session_state.margin_comment}\n"
        
        # Add Regional Lymph Nodes Section
        report_content += f"\nREGIONAL LYMPH NODES\n"
        
        if st.session_state.get('ln_status'):
            report_content += f"Regional Lymph Node Status: {st.session_state.ln_status}\n"
            
            if st.session_state.ln_status == "Regional lymph nodes present":
                if st.session_state.get('ln_tumor_status'):
                    report_content += f"  Tumor Status: {st.session_state.ln_tumor_status}\n"
                    
                    if st.session_state.ln_tumor_status == "Tumor present in regional lymph node(s)":
                        if st.session_state.get('ln_positive_exact'):
                            report_content += f"  Number of positive nodes: {st.session_state.ln_positive_exact}\n"
                        elif st.session_state.get('ln_positive_atleast'):
                            report_content += f"  Number of positive nodes: At least {st.session_state.ln_positive_atleast}\n"
                
                if st.session_state.get('ln_examined_exact'):
                    report_content += f"  Number of nodes examined: {st.session_state.ln_examined_exact}\n"
                elif st.session_state.get('ln_examined_atleast'):
                    report_content += f"  Number of nodes examined: At least {st.session_state.ln_examined_atleast}\n"
        
        if st.session_state.get('ln_comment'):
            report_content += f"Regional Lymph Node Comment: {st.session_state.ln_comment}\n"
        
        # Add Distant Metastasis Section
        report_content += f"\nDISTANT METASTASIS\n"
        
        distant_sites = []
        if st.session_state.get('dm_not_applicable'):
            distant_sites.append("Not applicable")
        if st.session_state.get('dm_non_regional_ln'):
            detail = st.session_state.get('dm_non_regional_detail', '')
            if detail:
                distant_sites.append(f"Non-regional lymph node(s) ({detail})")
            else:
                distant_sites.append("Non-regional lymph node(s)")
        if st.session_state.get('dm_liver'):
            detail = st.session_state.get('dm_liver_detail', '')
            if detail:
                distant_sites.append(f"Liver ({detail})")
            else:
                distant_sites.append("Liver")
        if st.session_state.get('dm_other'):
            detail = st.session_state.get('dm_other_detail', '')
            if detail:
                distant_sites.append(f"Other ({detail})")
            else:
                distant_sites.append("Other")
        
        if distant_sites:
            report_content += f"Distant Site(s) Involved: {', '.join(distant_sites)}\n"
        
        # Add pTNM Classification Section
        report_content += f"\nPATHOLOGIC STAGE CLASSIFICATION (pTNM, AJCC 8th Edition)\n"
        
        report_content += "Reporting of pT, pN, and (when applicable) pM categories is based on information\navailable to the pathologist at the time the report is issued. As per the AJCC\n(Chapter 1, 8th Ed.) it is the managing physician's responsibility to establish\nthe final pathologic stage based upon all pertinent information, including but\npotentially not limited to this pathology report.\n\n"
        
        # TNM Descriptors
        descriptors = []
        if st.session_state.get('tnm_m'):
            descriptors.append("m (multiple primary tumors)")
        if st.session_state.get('tnm_r'):
            descriptors.append("r (recurrent)")
        if st.session_state.get('tnm_y'):
            descriptors.append("y (post-treatment)")
        
        if descriptors:
            report_content += f"TNM Descriptors: {', '.join(descriptors)}\n"
        
        if st.session_state.get('pt_category'):
            report_content += f"pT: {st.session_state.pt_category}\n"
        if st.session_state.get('pn_category'):
            report_content += f"pN: {st.session_state.pn_category}\n"
        if st.session_state.get('pm_category'):
            report_content += f"pM: {st.session_state.pm_category}\n"
        
        # Add Additional Findings Section
        report_content += f"\nADDITIONAL FINDINGS\n"
        
        additional_findings = []
        if st.session_state.get('additional_none'):
            additional_findings.append("None identified")
        if st.session_state.get('additional_fibrosis'):
            detail = st.session_state.get('fibrosis_detail', '')
            if detail:
                additional_findings.append(f"Fibrosis ({detail})")
            else:
                additional_findings.append("Fibrosis")
        if st.session_state.get('additional_cirrhosis'):
            additional_findings.append("Cirrhosis")
        if st.session_state.get('additional_lgd_nodule'):
            additional_findings.append("Low-grade dysplastic nodule")
        if st.session_state.get('additional_hgd_nodule'):
            additional_findings.append("High-grade dysplastic nodule")
        if st.session_state.get('additional_steatosis'):
            additional_findings.append("Steatosis")
        if st.session_state.get('additional_steatohepatitis'):
            additional_findings.append("Steatohepatitis")
        if st.session_state.get('additional_iron'):
            additional_findings.append("Iron overload")
        if st.session_state.get('additional_hepatitis'):
            etiology = st.session_state.get('hepatitis_etiology', '')
            if etiology:
                additional_findings.append(f"Chronic hepatitis ({etiology})")
            else:
                additional_findings.append("Chronic hepatitis")
        if st.session_state.get('additional_other'):
            detail = st.session_state.get('additional_other_detail', '')
            if detail:
                additional_findings.append(f"Other ({detail})")
            else:
                additional_findings.append("Other")
        
        if additional_findings:
            report_content += f"Additional Findings: {', '.join(additional_findings)}\n"
        
        # Add Special Studies Section
        report_content += f"\nSPECIAL STUDIES\n"
        if st.session_state.get('ancillary_studies'):
            report_content += f"Ancillary Studies: {st.session_state.ancillary_studies}\n"
        else:
            report_content += "No special studies performed.\n"
        
        # Add Comments Section
        if st.session_state.get('comments'):
            report_content += f"\nCOMMENTS\n"
            report_content += str(st.session_state.comments) + "\n"
        
        report_content += f"\nEnd of Report\n"
        
        # Display the complete report in a large text area
        st.text_area(
            "Complete Pathology Report:",
            value=report_content,
            height=600,
            key="final_report"
        )
        
        # Download button for the text report
        st.download_button(
            label="📥 Download Report as Text File",
            data=report_content,
            file_name=f"hcc_pathology_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )

if __name__ == "__main__":
    main()