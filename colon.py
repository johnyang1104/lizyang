import streamlit as st
import json
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Colorectal Cancer Pathology Reporting Checklist",
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
</style>
""", unsafe_allow_html=True)

def main():
    # Header
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("🔬 Colorectal Cancer Pathology Reporting Checklist")
    st.markdown("**AJCC 8th Edition Standard** | Protocol Posting Date: June 2025")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Initialize session state for form data
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    
    # ========== CASE SUMMARY SECTION ==========
    st.markdown('<div class="section-header"><h2>📋 CASE SUMMARY</h2></div>', unsafe_allow_html=True)
    st.markdown("**(COLON AND RECTUM: Resection)**")
    
    col1, col2 = st.columns(2)
    with col1:
        case_id = st.text_input("Case ID:", key="case_id")
        patient_name = st.text_input("Patient Name:", key="patient_name")
    with col2:
        date_of_procedure = st.date_input("Date of Procedure:", key="date_of_procedure")
        pathologist = st.text_input("Pathologist:", key="pathologist")
    
    # ========== SPECIMEN SECTION ==========
    st.markdown('<div class="section-header"><h2>🧪 SPECIMEN</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><h4>Procedure</h4></div>', unsafe_allow_html=True)
    procedure_options = [
        "Right hemicolectomy",
        "Transverse colectomy", 
        "Left hemicolectomy",
        "Sigmoidectomy",
        "Low anterior resection",
        "Total abdominal colectomy",
        "Abdominoperineal resection",
        "Other",
        "Not specified"
    ]
    procedure = st.selectbox("Select procedure:", [""] + procedure_options, key="procedure")
    if procedure == "Other":
        procedure_other = st.text_input("Specify other procedure:", key="procedure_other")
    
    st.markdown('<div class="subsection"><h4>Macroscopic Evaluation of Mesorectum (Required only for rectal cancers)</h4></div>', unsafe_allow_html=True)
    mesorectum_options = [
        "Not applicable",
        "Complete",
        "Near complete", 
        "Incomplete",
        "Cannot be determined"
    ]
    mesorectum = st.selectbox("Mesorectum evaluation:", [""] + mesorectum_options, key="mesorectum")
    if mesorectum == "Cannot be determined":
        mesorectum_explain = st.text_input("Explain:", key="mesorectum_explain")
    
    # ========== TUMOR SECTION ==========
    st.markdown('<div class="section-header"><h2>🎯 TUMOR</h2></div>', unsafe_allow_html=True)
    
    # Tumor Site
    st.markdown('<div class="subsection"><h4>Tumor Site (select all that apply)</h4></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        cecum = st.checkbox("Cecum", key="site_cecum")
        if cecum:
            cecum_detail = st.text_input("Cecum details:", key="cecum_detail")
        
        ileocecal = st.checkbox("Ileocecal valve", key="site_ileocecal")
        if ileocecal:
            ileocecal_detail = st.text_input("Ileocecal valve details:", key="ileocecal_detail")
        
        ascending = st.checkbox("Ascending colon", key="site_ascending")
        if ascending:
            ascending_detail = st.text_input("Ascending colon details:", key="ascending_detail")
        
        hepatic = st.checkbox("Hepatic flexure", key="site_hepatic")
        if hepatic:
            hepatic_detail = st.text_input("Hepatic flexure details:", key="hepatic_detail")
        
        transverse = st.checkbox("Transverse colon", key="site_transverse")
        if transverse:
            transverse_detail = st.text_input("Transverse colon details:", key="transverse_detail")
    
    with col2:
        splenic = st.checkbox("Splenic flexure", key="site_splenic")
        if splenic:
            splenic_detail = st.text_input("Splenic flexure details:", key="splenic_detail")
        
        descending = st.checkbox("Descending colon", key="site_descending")
        if descending:
            descending_detail = st.text_input("Descending colon details:", key="descending_detail")
        
        sigmoid = st.checkbox("Sigmoid colon", key="site_sigmoid")
        if sigmoid:
            sigmoid_detail = st.text_input("Sigmoid colon details:", key="sigmoid_detail")
        
        rectosigmoid = st.checkbox("Rectosigmoid", key="site_rectosigmoid")
        if rectosigmoid:
            rectosigmoid_detail = st.text_input("Rectosigmoid details:", key="rectosigmoid_detail")
        
        rectum = st.checkbox("Rectum", key="site_rectum")
        if rectum:
            rectum_detail = st.text_input("Rectum details:", key="rectum_detail")
    
    colon_nos = st.checkbox("Colon, NOS", key="site_colon_nos")
    if colon_nos:
        colon_nos_detail = st.text_input("Colon NOS details:", key="colon_nos_detail")
    
    cannot_determine_site = st.checkbox("Cannot be determined", key="site_cannot_determine")
    if cannot_determine_site:
        site_explain = st.text_input("Explain:", key="site_explain")
    
    # Rectal Tumor Location
    st.markdown('<div class="subsection"><h4>Rectal Tumor Location (required for rectal primaries only)</h4></div>', unsafe_allow_html=True)
    rectal_location_options = [
        "Not applicable",
        "Entirely above anterior peritoneal reflection",
        "Entirely below anterior peritoneal reflection", 
        "Straddles anterior peritoneal reflection",
        "Not specified"
    ]
    rectal_location = st.selectbox("Rectal tumor location:", [""] + rectal_location_options, key="rectal_location")
    
    # Histologic Type
    st.markdown('<div class="subsection"><h4>Histologic Type</h4></div>', unsafe_allow_html=True)
    histologic_options = [
        "Adenocarcinoma",
        "Mucinous adenocarcinoma",
        "Poorly cohesive carcinoma",
        "Signet-ring cell carcinoma",
        "Medullary carcinoma",
        "Serrated adenocarcinoma",
        "Micropapillary adenocarcinoma",
        "Adenoma-like adenocarcinoma",
        "Adenosquamous carcinoma",
        "Undifferentiated carcinoma, NOS",
        "Carcinoma with sarcomatoid component",
        "Large cell neuroendocrine carcinoma",
        "Small cell neuroendocrine carcinoma",
        "Mixed neuroendocrine-non-neuroendocrine neoplasm (MiNEN)",
        "Other histologic type not listed",
        "Carcinoma, type cannot be determined"
    ]
    histologic_type = st.selectbox("Histologic type:", [""] + histologic_options, key="histologic_type")
    
    if histologic_type == "Mixed neuroendocrine-non-neuroendocrine neoplasm (MiNEN)":
        minen_components = st.text_input("Specify components:", key="minen_components")
    elif histologic_type == "Other histologic type not listed":
        histologic_other = st.text_input("Specify other type:", key="histologic_other")
    elif histologic_type == "Carcinoma, type cannot be determined":
        histologic_cannot = st.text_input("Explain:", key="histologic_cannot")
    
    histologic_comment = st.text_area("Histologic Type Comment:", key="histologic_comment")
    
    # Histologic Grade
    st.markdown('<div class="subsection"><h4>Histologic Grade</h4></div>', unsafe_allow_html=True)
    grade_options = [
        "G1, well-differentiated",
        "G2, moderately differentiated",
        "G3, poorly differentiated",
        "G4, undifferentiated",
        "Other",
        "GX, cannot be assessed",
        "Not applicable"
    ]
    grade = st.selectbox("Histologic grade:", [""] + grade_options, key="grade")
    if grade == "Other":
        grade_other = st.text_input("Specify other grade:", key="grade_other")
    elif grade == "GX, cannot be assessed":
        grade_cannot = st.text_input("Explain:", key="grade_cannot")
    
    # Tumor Size
    st.markdown('<div class="subsection"><h4>Tumor Size</h4></div>', unsafe_allow_html=True)
    size_method = st.radio(
        "Size measurement:",
        ["Greatest dimension in cm", "Cannot be determined"],
        key="size_method"
    )
    
    if size_method == "Greatest dimension in cm":
        size_cm = st.number_input("Size (cm):", min_value=0.0, step=0.1, key="size_cm")
        
        additional_dims = st.checkbox("Additional dimensions", key="additional_dims")
        if additional_dims:
            col1, col2 = st.columns(2)
            with col1:
                size_x = st.number_input("Width (cm):", min_value=0.0, step=0.1, key="size_x")
            with col2:
                size_y = st.number_input("Height (cm):", min_value=0.0, step=0.1, key="size_y")
    else:
        size_explain = st.text_input("Explain why size cannot be determined:", key="size_explain")
    
    # Multiple Primary Sites
    st.markdown('<div class="subsection"><h4>Multiple Primary Sites</h4></div>', unsafe_allow_html=True)
    multiple_primary = st.radio(
        "Multiple primary sites:",
        ["Not applicable", "Present"],
        key="multiple_primary"
    )
    if multiple_primary == "Present":
        multiple_details = st.text_area("Describe multiple primary sites:", key="multiple_details")
        st.info("Please complete a separate checklist for each primary site")
    
    # Tumor Extent
    st.markdown('<div class="subsection"><h4>Tumor Extent</h4></div>', unsafe_allow_html=True)
    extent_options = [
        "No invasion (high-grade dysplasia)",
        "Invades lamina propria / muscularis mucosae (intramucosal carcinoma)",
        "Invades submucosa",
        "Invades into muscularis propria",
        "Invades through muscularis propria into the pericolic or perirectal tissue",
        "Invades visceral peritoneum",
        "Directly invades or adheres to adjacent structure(s)",
        "Cannot be determined",
        "No evidence of primary tumor"
    ]
    tumor_extent = st.selectbox("Tumor extent:", [""] + extent_options, key="tumor_extent")
    
    if tumor_extent == "Directly invades or adheres to adjacent structure(s)":
        adjacent_structures = st.text_input("Specify adjacent structures:", key="adjacent_structures")
    elif tumor_extent == "Cannot be determined":
        extent_explain = st.text_input("Explain:", key="extent_explain")
    
    # Sub-mucosal Invasion (for pT1 tumors)
    st.markdown('<div class="subsection"><h4>Sub-mucosal Invasion (required only for pT1 tumors)</h4></div>', unsafe_allow_html=True)
    submucosal_applicable = st.radio(
        "Sub-mucosal invasion:",
        ["Not applicable (not a pT1 tumor)", "Not identified", "Present"],
        key="submucosal_applicable"
    )
    
    if submucosal_applicable == "Present":
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Depth of Sub-mucosal Invasion:**")
            depth_options = [
                "Less than 1 mm",
                "Greater than or equal to 1 mm and less than 2 mm",
                "Greater than 2 mm", 
                "Exact depth in mm",
                "Cannot be determined"
            ]
            depth = st.selectbox("Depth:", [""] + depth_options, key="submucosal_depth")
            
            if depth == "Exact depth in mm":
                depth_mm = st.number_input("Depth (mm):", min_value=0.0, step=0.1, key="depth_mm")
            elif depth == "Cannot be determined":
                depth_explain = st.text_input("Explain:", key="depth_explain")
        
        with col2:
            st.write("**Extent of Sub-mucosal Invasion:**")
            extent_sub_options = [
                "Tumor invades into upper one third of submucosa",
                "Tumor invades into middle one third of submucosa",
                "Tumor invades into lower one third of submucosa",
                "Cannot be determined"
            ]
            extent_sub = st.selectbox("Extent:", [""] + extent_sub_options, key="submucosal_extent")
            
            if extent_sub == "Cannot be determined":
                extent_sub_explain = st.text_input("Explain:", key="extent_sub_explain")
    
    # Macroscopic Tumor Perforation
    st.markdown('<div class="subsection"><h4>Macroscopic Tumor Perforation</h4></div>', unsafe_allow_html=True)
    perforation_options = ["Not identified", "Present", "Cannot be determined"]
    perforation = st.selectbox("Macroscopic Tumor Perforation:", [""] + perforation_options, key="perforation")
    if perforation == "Cannot be determined":
        perforation_explain = st.text_input("Explain:", key="perforation_explain")
    
    # Lymphatic and/or Vascular Invasion
    st.markdown('<div class="subsection"><h4>Lymphatic and/or Vascular Invasion (select all that apply)</h4></div>', unsafe_allow_html=True)
    lvi_not_identified = st.checkbox("Not identified", key="lvi_not_identified")
    
    lvi_small = st.checkbox("Small vessel", key="lvi_small")
    if lvi_small:
        lvi_small_detail = st.text_input("Small vessel details:", key="lvi_small_detail")
    
    lvi_large_intramural = st.checkbox("Large vessel (venous), intramural", key="lvi_large_intramural")
    if lvi_large_intramural:
        lvi_large_intramural_detail = st.text_input("Large vessel intramural details:", key="lvi_large_intramural_detail")
    
    lvi_large_extramural = st.checkbox("Large vessel (venous), extramural", key="lvi_large_extramural")
    if lvi_large_extramural:
        lvi_large_extramural_detail = st.text_input("Large vessel extramural details:", key="lvi_large_extramural_detail")
    
    lvi_present_nos = st.checkbox("Present, NOS", key="lvi_present_nos")
    if lvi_present_nos:
        lvi_nos_detail = st.text_input("Present NOS details:", key="lvi_nos_detail")
    
    lvi_cannot_determine = st.checkbox("Cannot be determined", key="lvi_cannot_determine")
    if lvi_cannot_determine:
        lvi_cannot_explain = st.text_input("Cannot be determined - explain:", key="lvi_cannot_explain")
    
    # Perineural Invasion
    st.markdown('<div class="subsection"><h4>Perineural Invasion</h4></div>', unsafe_allow_html=True)
    pni_options = ["Not identified", "Present", "Cannot be determined"]
    pni = st.selectbox("Perineural Invasion:", [""] + pni_options, key="pni")
    if pni == "Cannot be determined":
        pni_explain = st.text_input("Explain:", key="pni_explain")
    
    # Tumor Budding Score
    st.markdown('<div class="subsection"><h4>Tumor Budding Score (required only when applicable)</h4></div>', unsafe_allow_html=True)
    budding_options = ["Not applicable", "Low (0-4)", "Intermediate (5-9)", "High (10 or more)", "Cannot be determined"]
    budding = st.selectbox("Tumor budding score:", [""] + budding_options, key="budding")
    
    if budding == "Cannot be determined":
        budding_explain = st.text_input("Explain:", key="budding_explain")
    
    # Number of Tumor Buds
    st.write("**Number of Tumor Buds (per 'hotspot' field):**")
    buds_method = st.radio(
        "Number of tumor buds per 'hotspot' field:",
        ["Specify number", "Other", "Cannot be determined"],
        key="buds_method"
    )
    
    if buds_method == "Specify number":
        buds_number = st.number_input("Number in one 'hotspot' field (area = 0.785 mm²):", min_value=0, key="buds_number")
    elif buds_method == "Other":
        buds_other = st.text_input("Specify other:", key="buds_other")
    elif buds_method == "Cannot be determined":
        buds_explain = st.text_input("Explain:", key="buds_explain")
    
    # Type of Polyp
    st.markdown('<div class="subsection"><h4>Type of Polyp in which Invasive Carcinoma Arose</h4></div>', unsafe_allow_html=True)
    polyp_options = [
        "None identified",
        "Tubular adenoma",
        "Villous adenoma",
        "Tubulovillous adenoma",
        "Traditional serrated adenoma",
        "Sessile serrated adenoma / sessile serrated polyp",
        "Hamartomatous polyp",
        "Other"
    ]
    polyp_type = st.selectbox("Polyp type:", [""] + polyp_options, key="polyp_type")
    if polyp_type == "Other":
        polyp_other = st.text_input("Specify other polyp type:", key="polyp_other")
    
    # Treatment Effect
    st.markdown('<div class="subsection"><h4>Treatment Effect</h4></div>', unsafe_allow_html=True)
    treatment_options = [
        "No known presurgical therapy",
        "Present, with no viable cancer cells (complete response, score 0)",
        "Present, with single cells or rare small groups of cancer cells (near complete response, score 1)",
        "Present, with residual cancer showing evident tumor regression, but more than single cells or rare small groups of cancer cells (partial response, score 2)",
        "Present, NOS",
        "Absent, with extensive residual cancer and no evident tumor regression (poor or no response, score 3)",
        "Cannot be determined"
    ]
    treatment_effect = st.selectbox("Treatment effect:", [""] + treatment_options, key="treatment_effect")
    if treatment_effect == "Cannot be determined":
        treatment_explain = st.text_input("Explain:", key="treatment_explain")
    
    # Tumor Comment
    tumor_comment = st.text_area("Tumor Comment:", key="tumor_comment")
    
    # ========== MARGINS SECTION ==========
    st.markdown('<div class="section-header"><h2>📏 MARGINS</h2></div>', unsafe_allow_html=True)
    
    # Margin Status for Invasive Carcinoma
    st.markdown('<div class="subsection"><h4>Margin Status for Invasive Carcinoma</h4></div>', unsafe_allow_html=True)
    
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
        
        col1, col2 = st.columns(2)
        with col1:
            proximal_closest = st.checkbox("Proximal", key="proximal_closest")
            if proximal_closest:
                proximal_detail = st.text_input("Proximal details:", key="proximal_detail")
            
            distal_closest = st.checkbox("Distal", key="distal_closest")
            if distal_closest:
                distal_detail = st.text_input("Distal details:", key="distal_detail")
            
            radial_closest = st.checkbox("Radial (circumferential)", key="radial_closest")
            if radial_closest:
                radial_detail = st.text_input("Radial details:", key="radial_detail")
        
        with col2:
            mesenteric_closest = st.checkbox("Mesenteric", key="mesenteric_closest")
            if mesenteric_closest:
                mesenteric_detail = st.text_input("Mesenteric details:", key="mesenteric_detail")
            
            deep_closest = st.checkbox("Deep", key="deep_closest")
            if deep_closest:
                deep_detail = st.text_input("Deep details:", key="deep_detail")
            
            mucosal_closest = st.checkbox("Mucosal", key="mucosal_closest")
            if mucosal_closest:
                mucosal_detail = st.text_input("Mucosal location:", key="mucosal_detail")
        
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
        
        col1, col2 = st.columns(2)
        with col1:
            proximal_involved = st.checkbox("Proximal", key="proximal_involved")
            if proximal_involved:
                proximal_involved_detail = st.text_input("Proximal involved details:", key="proximal_involved_detail")
            
            distal_involved = st.checkbox("Distal", key="distal_involved")
            if distal_involved:
                distal_involved_detail = st.text_input("Distal involved details:", key="distal_involved_detail")
            
            radial_involved = st.checkbox("Radial (circumferential)", key="radial_involved")
            if radial_involved:
                radial_involved_detail = st.text_input("Radial involved details:", key="radial_involved_detail")
        
        with col2:
            mesenteric_involved = st.checkbox("Mesenteric", key="mesenteric_involved")
            if mesenteric_involved:
                mesenteric_involved_detail = st.text_input("Mesenteric involved details:", key="mesenteric_involved_detail")
            
            deep_involved = st.checkbox("Deep", key="deep_involved")
            if deep_involved:
                deep_involved_detail = st.text_input("Deep involved details:", key="deep_involved_detail")
            
            mucosal_involved = st.checkbox("Mucosal", key="mucosal_involved")
            if mucosal_involved:
                mucosal_involved_detail = st.text_input("Mucosal involved location:", key="mucosal_involved_detail")
    
    elif margin_status == "Other":
        margin_other_detail = st.text_input("Specify other:", key="margin_other_detail")
    elif margin_status == "Cannot be determined":
        margin_cannot_explain = st.text_input("Explain:", key="margin_cannot_explain")
    
    # Margin Status for Non-Invasive Tumor
    st.markdown('<div class="subsection"><h4>Margin Status for Non-Invasive Tumor</h4></div>', unsafe_allow_html=True)
    
    non_invasive_status = st.radio(
        "Non-invasive tumor margin status:",
        [
            "All margins negative for high-grade dysplasia / intramucosal carcinoma and low-grade dysplasia",
            "High-grade dysplasia / intramucosal carcinoma present at margin",
            "Low-grade dysplasia present at margin",
            "Other",
            "Cannot be determined",
            "Not applicable"
        ],
        key="non_invasive_status"
    )
    
    if non_invasive_status == "High-grade dysplasia / intramucosal carcinoma present at margin":
        st.write("**Margin(s) Involved by High-Grade Dysplasia / Intramucosal Carcinoma:**")
        hgd_proximal = st.checkbox("Proximal", key="hgd_proximal")
        if hgd_proximal:
            hgd_proximal_detail = st.text_input("HGD Proximal details:", key="hgd_proximal_detail")
        
        hgd_distal = st.checkbox("Distal", key="hgd_distal")
        if hgd_distal:
            hgd_distal_detail = st.text_input("HGD Distal details:", key="hgd_distal_detail")
        
        hgd_mucosal = st.checkbox("Mucosal", key="hgd_mucosal")
        if hgd_mucosal:
            hgd_mucosal_detail = st.text_input("HGD Mucosal location:", key="hgd_mucosal_detail")
        
        hgd_other = st.checkbox("Other", key="hgd_other")
        if hgd_other:
            hgd_other_detail = st.text_input("HGD Other details:", key="hgd_other_detail")
        
        hgd_cannot = st.checkbox("Cannot be determined", key="hgd_cannot")
        if hgd_cannot:
            hgd_cannot_detail = st.text_input("HGD Cannot be determined details:", key="hgd_cannot_detail")
    
    elif non_invasive_status == "Low-grade dysplasia present at margin":
        st.write("**Margin(s) Involved by Low-Grade Dysplasia:**")
        lgd_proximal = st.checkbox("Proximal", key="lgd_proximal")
        if lgd_proximal:
            lgd_proximal_detail = st.text_input("LGD Proximal details:", key="lgd_proximal_detail")
        
        lgd_distal = st.checkbox("Distal", key="lgd_distal")
        if lgd_distal:
            lgd_distal_detail = st.text_input("LGD Distal details:", key="lgd_distal_detail")
        
        lgd_mucosal = st.checkbox("Mucosal", key="lgd_mucosal")
        if lgd_mucosal:
            lgd_mucosal_detail = st.text_input("LGD Mucosal location:", key="lgd_mucosal_detail")
        
        lgd_other = st.checkbox("Other", key="lgd_other")
        if lgd_other:
            lgd_other_detail = st.text_input("LGD Other details:", key="lgd_other_detail")
        
        lgd_cannot = st.checkbox("Cannot be determined", key="lgd_cannot")
        if lgd_cannot:
            lgd_cannot_detail = st.text_input("LGD Cannot be determined details:", key="lgd_cannot_detail")
    
    elif non_invasive_status == "Other":
        non_invasive_other = st.text_input("Specify other:", key="non_invasive_other")
    elif non_invasive_status == "Cannot be determined":
        non_invasive_explain = st.text_input("Explain:", key="non_invasive_explain")
    
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
        ln_other_detail = st.text_input("Specify other:", key="ln_other_detail")
    elif ln_status == "Cannot be determined":
        ln_cannot_explain = st.text_input("Explain:", key="ln_cannot_explain")
    
    # Tumor Deposits
    st.markdown('<div class="subsection"><h4>Tumor Deposits</h4></div>', unsafe_allow_html=True)
    
    tumor_deposits = st.radio(
        "Tumor deposits:",
        ["Not identified", "Present", "Cannot be determined"],
        key="tumor_deposits"
    )
    
    if tumor_deposits == "Present":
        st.write("**Number of Tumor Deposits:**")
        
        deposits_method = st.radio(
            "Number of deposits:",
            ["Specify number", "Other", "Cannot be determined"],
            key="deposits_method"
        )
        
        if deposits_method == "Specify number":
            deposits_number = st.number_input("Number of tumor deposits:", min_value=0, key="deposits_number")
        elif deposits_method == "Other":
            deposits_other = st.text_input("Specify other:", key="deposits_other")
        elif deposits_method == "Cannot be determined":
            deposits_explain = st.text_input("Explain:", key="deposits_explain")
    
    elif tumor_deposits == "Cannot be determined":
        deposits_cannot_explain = st.text_input("Explain:", key="deposits_cannot_explain")
    
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
        "pTis: Carcinoma in situ, intramucosal carcinoma (involvement of lamina propria with no extension through muscularis mucosae)",
        "pT1: Tumor invades the submucosa (through the muscularis mucosa but not into the muscularis propria)",
        "pT2: Tumor invades the muscularis propria",
        "pT3: Tumor invades through the muscularis propria into pericolorectal tissues",
        "pT4a: Tumor invades through the visceral peritoneum",
        "pT4b: Tumor directly invades or adheres to adjacent organs or structures",
        "pT4 (subcategory cannot be determined)"
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
        "pN1a: One regional lymph node is positive",
        "pN1b: Two or three regional lymph nodes are positive",
        "pN1c: No regional lymph nodes are positive, but there are tumor deposits in the subserosa, mesentery, nonperitonealized pericolic or perirectal / mesorectal tissues",
        "pN1 (subcategory cannot be determined)",
        "pN2a: Four to six regional lymph nodes are positive",
        "pN2b: Seven or more regional lymph nodes are positive",
        "pN2 (subcategory cannot be assessed)"
    ]
    
    pn_category = st.selectbox("pN Category:", [""] + pn_options, key="pn_category")
    
    # pM Category
    st.markdown('<div class="subsection"><h4>pM Category (required only if confirmed pathologically)</h4></div>', unsafe_allow_html=True)
    
    pm_options = [
        "Not applicable - pM cannot be determined from the submitted specimen(s)",
        "pM1a: Metastasis to one site or organ is identified without peritoneal metastasis",
        "pM1b: Metastasis to two or more sites or organs is identified without peritoneal metastasis",
        "pM1c: Metastasis to the peritoneal surface is identified alone or with other site or organ metastases",
        "pM1 (subcategory cannot be determined)"
    ]
    
    pm_category = st.selectbox("pM Category:", [""] + pm_options, key="pm_category")
    
    # ========== ADDITIONAL FINDINGS SECTION ==========
    st.markdown('<div class="section-header"><h2>🔍 ADDITIONAL FINDINGS</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><h4>Additional Findings (select all that apply)</h4></div>', unsafe_allow_html=True)
    
    additional_none = st.checkbox("None identified", key="additional_none")
    additional_adenoma = st.checkbox("Adenoma(s)", key="additional_adenoma")
    additional_uc = st.checkbox("Ulcerative colitis", key="additional_uc")
    additional_crohn = st.checkbox("Crohn disease", key="additional_crohn")
    additional_diverticulosis = st.checkbox("Diverticulosis", key="additional_diverticulosis")
    additional_dysplasia_ibd = st.checkbox("Dysplasia arising in inflammatory bowel disease", key="additional_dysplasia_ibd")
    additional_other = st.checkbox("Other", key="additional_other")
    
    if additional_other:
        additional_other_detail = st.text_input("Specify other findings:", key="additional_other_detail")
    
    # Special Studies
    st.markdown('<div class="subsection"><h4>Special Studies</h4></div>', unsafe_allow_html=True)
    st.info("For reporting molecular testing and immunohistochemistry for mismatch repair proteins, and for other cancer biomarker testing results, the CAP Colorectal Biomarker Template should be used. Pending biomarker studies should be listed in the Comments section of this report.")
    
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
        st.markdown("### 📄 COLORECTAL CANCER PATHOLOGY REPORT")
        
        # Create comprehensive report content
        report_content = f"""COLORECTAL CANCER PATHOLOGY REPORT
Date: {datetime.now().strftime('%Y-%m-%d')}
Standard: AJCC 8th Edition
Protocol Posting Date: June 2025

CASE SUMMARY (COLON AND RECTUM: Resection)
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
        
        # Add Specimen Section
        report_content += f"\nSPECIMEN\n"
        
        if st.session_state.get('procedure'):
            report_content += f"Procedure: {st.session_state.procedure}\n"
            if st.session_state.get('procedure_other') and st.session_state.procedure == "Other":
                report_content += f"  Details: {st.session_state.procedure_other}\n"
        
        if st.session_state.get('mesorectum'):
            report_content += f"Macroscopic Evaluation of Mesorectum: {st.session_state.mesorectum}\n"
            if st.session_state.get('mesorectum_explain') and st.session_state.mesorectum == "Cannot be determined":
                report_content += f"  Explanation: {st.session_state.mesorectum_explain}\n"
        
        # Add Tumor Section
        report_content += f"\nTUMOR\n"
        
        # Tumor Sites
        tumor_sites = []
        site_keys = ['site_cecum', 'site_ileocecal', 'site_ascending', 'site_hepatic', 'site_transverse', 
                   'site_splenic', 'site_descending', 'site_sigmoid', 'site_rectosigmoid', 'site_rectum', 'site_colon_nos']
        site_names = ['Cecum', 'Ileocecal valve', 'Ascending colon', 'Hepatic flexure', 'Transverse colon',
                    'Splenic flexure', 'Descending colon', 'Sigmoid colon', 'Rectosigmoid', 'Rectum', 'Colon, NOS']
        
        for key, name in zip(site_keys, site_names):
            if st.session_state.get(key):
                detail_key = key.replace('site_', '') + '_detail'
                detail = st.session_state.get(detail_key, '')
                if detail:
                    tumor_sites.append(f"{name} ({detail})")
                else:
                    tumor_sites.append(name)
        
        if tumor_sites:
            report_content += f"Tumor Site: {', '.join(tumor_sites)}\n"
        
        if st.session_state.get('rectal_location'):
            report_content += f"Rectal Tumor Location: {st.session_state.rectal_location}\n"
        
        if st.session_state.get('histologic_type'):
            report_content += f"Histologic Type: {st.session_state.histologic_type}\n"
            if st.session_state.get('minen_components') and "MiNEN" in str(st.session_state.histologic_type):
                report_content += f"  Components: {st.session_state.minen_components}\n"
            elif st.session_state.get('histologic_other') and st.session_state.histologic_type == "Other histologic type not listed":
                report_content += f"  Specified type: {st.session_state.histologic_other}\n"
        
        if st.session_state.get('histologic_comment'):
            report_content += f"Histologic Type Comment: {st.session_state.histologic_comment}\n"
        
        if st.session_state.get('grade'):
            report_content += f"Histologic Grade: {st.session_state.grade}\n"
            if st.session_state.get('grade_other') and st.session_state.grade == "Other":
                report_content += f"  Specified grade: {st.session_state.grade_other}\n"
        
        # Tumor Size
        if st.session_state.get('size_method') == "Greatest dimension in cm":
            if st.session_state.get('size_cm'):
                size_text = f"{st.session_state.size_cm} cm"
                if st.session_state.get('additional_dims') and st.session_state.get('size_x') and st.session_state.get('size_y'):
                    size_text += f" x {st.session_state.size_x} cm x {st.session_state.size_y} cm"
                report_content += f"Tumor Size: {size_text}\n"
        elif st.session_state.get('size_method') == "Cannot be determined":
            report_content += "Tumor Size: Cannot be determined"
            if st.session_state.get('size_explain'):
                report_content += f" ({st.session_state.size_explain})"
            report_content += "\n"
        
        if st.session_state.get('multiple_primary') == "Present":
            report_content += "Multiple Primary Sites: Present\n"
            if st.session_state.get('multiple_details'):
                report_content += f"  Details: {st.session_state.multiple_details}\n"
        
        if st.session_state.get('tumor_extent'):
            report_content += f"Tumor Extent: {st.session_state.tumor_extent}\n"
            if st.session_state.get('adjacent_structures') and "adjacent structure" in str(st.session_state.tumor_extent):
                report_content += f"  Adjacent structures: {st.session_state.adjacent_structures}\n"
        
        # Additional tumor features
        if st.session_state.get('submucosal_applicable') == "Present":
            report_content += "Sub-mucosal Invasion: Present\n"
            if st.session_state.get('submucosal_depth'):
                report_content += f"  Depth: {st.session_state.submucosal_depth}\n"
            if st.session_state.get('submucosal_extent'):
                report_content += f"  Extent: {st.session_state.submucosal_extent}\n"
        
        if st.session_state.get('perforation'):
            report_content += f"Macroscopic Tumor Perforation: {st.session_state.perforation}\n"
        
        # Lymphatic/Vascular Invasion
        lvi_findings = []
        if st.session_state.get('lvi_not_identified'):
            lvi_findings.append("Not identified")
        if st.session_state.get('lvi_small'):
            lvi_findings.append("Small vessel")
        if st.session_state.get('lvi_large_intramural'):
            lvi_findings.append("Large vessel (venous), intramural")
        if st.session_state.get('lvi_large_extramural'):
            lvi_findings.append("Large vessel (venous), extramural")
        if st.session_state.get('lvi_present_nos'):
            lvi_findings.append("Present, NOS")
        
        if lvi_findings:
            report_content += f"Lymphatic and/or Vascular Invasion: {', '.join(lvi_findings)}\n"
        
        if st.session_state.get('pni'):
            report_content += f"Perineural Invasion: {st.session_state.pni}\n"
        
        if st.session_state.get('budding'):
            report_content += f"Tumor Budding Score: {st.session_state.budding}\n"
        
        if st.session_state.get('polyp_type'):
            report_content += f"Type of Polyp: {st.session_state.polyp_type}\n"
        
        if st.session_state.get('treatment_effect'):
            report_content += f"Treatment Effect: {st.session_state.treatment_effect}\n"
        
        if st.session_state.get('tumor_comment'):
            report_content += f"Tumor Comment: {st.session_state.tumor_comment}\n"
        
        # Add Margins Section
        report_content += f"\nMARGINS\n"
        
        if st.session_state.get('margin_status'):
            report_content += f"Margin Status for Invasive Carcinoma: {st.session_state.margin_status}\n"
        
        if st.session_state.get('non_invasive_status'):
            report_content += f"Margin Status for Non-Invasive Tumor: {st.session_state.non_invasive_status}\n"
        
        if st.session_state.get('margin_comment'):
            report_content += f"Margin Comment: {st.session_state.margin_comment}\n"
        
        # Add Regional Lymph Nodes Section
        report_content += f"\nREGIONAL LYMPH NODES\n"
        
        if st.session_state.get('ln_status'):
            report_content += f"Regional Lymph Node Status: {st.session_state.ln_status}\n"
            
            if st.session_state.get('ln_positive_exact'):
                report_content += f"  Number of positive nodes: {st.session_state.ln_positive_exact}\n"
            if st.session_state.get('ln_examined_exact'):
                report_content += f"  Number of nodes examined: {st.session_state.ln_examined_exact}\n"
        
        if st.session_state.get('tumor_deposits'):
            report_content += f"Tumor Deposits: {st.session_state.tumor_deposits}\n"
            if st.session_state.get('deposits_number'):
                report_content += f"  Number of tumor deposits: {st.session_state.deposits_number}\n"
        
        if st.session_state.get('ln_comment'):
            report_content += f"Regional Lymph Node Comment: {st.session_state.ln_comment}\n"
        
        # Add Distant Metastasis Section
        report_content += f"\nDISTANT METASTASIS\n"
        
        distant_sites = []
        if st.session_state.get('dm_not_applicable'):
            distant_sites.append("Not applicable")
        if st.session_state.get('dm_non_regional_ln'):
            distant_sites.append("Non-regional lymph node(s)")
        if st.session_state.get('dm_liver'):
            distant_sites.append("Liver")
        if st.session_state.get('dm_other'):
            distant_sites.append("Other")
        
        if distant_sites:
            report_content += f"Distant Site(s) Involved: {', '.join(distant_sites)}\n"
        
        # Add pTNM Classification Section
        report_content += f"\npTNM CLASSIFICATION (AJCC 8th Edition)\n"
        
        report_content += "Reporting of pT, pN, and (when applicable) pM categories is based on information\navailable to the pathologist at the time the report is issued.\n\n"
        
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
        if st.session_state.get('additional_adenoma'):
            additional_findings.append("Adenoma(s)")
        if st.session_state.get('additional_uc'):
            additional_findings.append("Ulcerative colitis")
        if st.session_state.get('additional_crohn'):
            additional_findings.append("Crohn disease")
        if st.session_state.get('additional_diverticulosis'):
            additional_findings.append("Diverticulosis")
        if st.session_state.get('additional_dysplasia_ibd'):
            additional_findings.append("Dysplasia arising in inflammatory bowel disease")
        if st.session_state.get('additional_other'):
            additional_findings.append("Other")
        
        if additional_findings:
            report_content += f"Additional Findings: {', '.join(additional_findings)}\n"
        
        report_content += f"\nSPECIAL STUDIES\n"
        report_content += "For reporting molecular testing and immunohistochemistry for mismatch repair\nproteins, and for other cancer biomarker testing results, the CAP Colorectal\nBiomarker Template should be used. Pending biomarker studies should be listed\nin the Comments section of this report.\n"
        
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
            file_name=f"colorectal_pathology_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )

if __name__ == "__main__":
    main()