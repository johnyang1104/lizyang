import streamlit as st
import json
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Ampulla of Vater Pathology Reporting Checklist",
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
    st.title("🔬 Ampulla of Vater Pathology Reporting Checklist")
    st.markdown("**AJCC 8th Edition Standard** | Protocol Posting Date: June 2025")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Initialize session state for form data
    if 'form_data' not in st.session_state:
        st.session_state.form_data = {}
    
    # ========== CASE SUMMARY SECTION ==========
    st.markdown('<div class="section-header"><h2>📋 CASE SUMMARY</h2></div>', unsafe_allow_html=True)
    st.markdown("**(AMPULLA OF VATER)**")
    
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
        "Ampullectomy",
        "Pancreaticoduodenectomy (Whipple resection)",
        "Other",
        "Not specified"
    ]
    procedure = st.selectbox("Select procedure:", [""] + procedure_options, key="procedure")
    if procedure == "Other":
        procedure_other = st.text_input("Specify other procedure:", key="procedure_other")
    
    # ========== TUMOR SECTION ==========
    st.markdown('<div class="section-header"><h2>🎯 TUMOR</h2></div>', unsafe_allow_html=True)
    
    # Tumor Site
    st.markdown('<div class="subsection"><h4>Tumor Site</h4></div>', unsafe_allow_html=True)
    
    tumor_site_options = [
        "Intra-ampullary papillary-tubular neoplasm (IAPN)-associated",
        "Ampullary ductal origin",
        "(Peri-) Ampullary-duodenal",
        "Mixed intra-ampullary and (peri-) ampullary-duodenal, NOS",
        "Other",
        "Cannot be determined",
        "Not specified"
    ]
    tumor_site = st.selectbox("Tumor site:", [""] + tumor_site_options, key="tumor_site")
    
    if tumor_site in ["(Peri-) Ampullary-duodenal", "Mixed intra-ampullary and (peri-) ampullary-duodenal, NOS", "Other", "Cannot be determined"]:
        tumor_site_detail = st.text_input(f"Details for {tumor_site}:", key="tumor_site_detail")
    
    # Histologic Type
    st.markdown('<div class="subsection"><h4>Histologic Type</h4></div>', unsafe_allow_html=True)
    histologic_options = [
        "Adenocarcinoma, pancreaticobiliary-type",
        "Adenocarcinoma, intestinal-type",
        "Adenocarcinoma with mixed features (pancreaticobiliary- and intestinal-type)",
        "Adenocarcinoma, NOS",
        "Adenocarcinoma arising in intra-ampullary papillary-tubular neoplasm (IAPN)",
        "Mucinous adenocarcinoma",
        "Poorly cohesive carcinoma",
        "Signet-ring cell carcinoma",
        "Medullary carcinoma",
        "Adenosquamous carcinoma",
        "Large cell neuroendocrine carcinoma",
        "Small cell neuroendocrine carcinoma",
        "Undifferentiated carcinoma, NOS",
        "Mixed neuroendocrine-non-neuroendocrine neoplasm (MiNEN)",
        "Other histologic type not listed",
        "Carcinoma, NOS"
    ]
    histologic_type = st.selectbox("Histologic type:", [""] + histologic_options, key="histologic_type")
    
    if histologic_type == "Mixed neuroendocrine-non-neuroendocrine neoplasm (MiNEN)":
        minen_components = st.text_input("Specify components:", key="minen_components")
    elif histologic_type == "Other histologic type not listed":
        histologic_other = st.text_input("Specify other type:", key="histologic_other")
    
    histologic_comment = st.text_area("Histologic Type Comment:", key="histologic_comment")
    
    # Histologic Grade
    st.markdown('<div class="subsection"><h4>Histologic Grade</h4></div>', unsafe_allow_html=True)
    grade_options = [
        "G1, well-differentiated",
        "G2, moderately differentiated",
        "G3, poorly differentiated",
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
    
    tumor_size_type = st.radio(
        "Tumor size type:",
        ["Unifocal invasive carcinoma", "Multifocal invasive carcinoma in association with IAPN", "Cannot be determined"],
        key="tumor_size_type"
    )
    
    if tumor_size_type == "Unifocal invasive carcinoma":
        size_cm = st.number_input("Greatest dimension (cm):", min_value=0.0, step=0.1, key="size_cm")
        
        additional_dims = st.checkbox("Additional dimensions", key="additional_dims")
        if additional_dims:
            col1, col2 = st.columns(2)
            with col1:
                size_x = st.number_input("Width (cm):", min_value=0.0, step=0.1, key="size_x")
            with col2:
                size_y = st.number_input("Height (cm):", min_value=0.0, step=0.1, key="size_y")
    
    elif tumor_size_type == "Multifocal invasive carcinoma in association with IAPN":
        largest_focus = st.number_input("Size of largest focus (cm):", min_value=0.0, step=0.1, key="largest_focus")
        aggregate_size = st.number_input("Aggregate size of all foci (cm) (if known):", min_value=0.0, step=0.1, key="aggregate_size")
        invasive_percentage = st.number_input("Invasive component percentage (if known):", min_value=0.0, max_value=100.0, step=0.1, key="invasive_percentage")
    
    elif tumor_size_type == "Cannot be determined":
        size_explain = st.text_input("Explain why size cannot be determined:", key="size_explain")
    
    # Tumor Extent
    st.markdown('<div class="subsection"><h4>Tumor Extent (select all that apply)</h4></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        extent_cis = st.checkbox("Carcinoma in situ / high-grade dysplasia", key="extent_cis")
        extent_ampulla = st.checkbox("Limited to ampulla of Vater or sphincter of Oddi", key="extent_ampulla")
        extent_sphincter = st.checkbox("Invades beyond sphincter of Oddi", key="extent_sphincter")
        extent_submucosa = st.checkbox("Invades into duodenal submucosa", key="extent_submucosa")
        extent_muscularis = st.checkbox("Invades into muscularis propria of duodenum", key="extent_muscularis")
        extent_pancreas_05 = st.checkbox("Directly invades pancreas (up to 0.5 cm)", key="extent_pancreas_05")
        extent_pancreas_more = st.checkbox("Extends more than 0.5 cm into pancreas", key="extent_pancreas_more")
    
    with col2:
        extent_peripancreatic = st.checkbox("Extends into peripancreatic soft tissues", key="extent_peripancreatic")
        extent_periduodenal = st.checkbox("Extends into periduodenal tissue", key="extent_periduodenal")
        extent_serosa = st.checkbox("Extends into duodenal serosa", key="extent_serosa")
        extent_other_organs = st.checkbox("Invades other adjacent organ(s)", key="extent_other_organs")
        extent_no_evidence = st.checkbox("No evidence of primary tumor", key="extent_no_evidence")
        extent_cannot_determine = st.checkbox("Cannot be determined", key="extent_cannot_determine")
    
    if extent_other_organs:
        st.write("**Adjacent organs involved (select all that apply):**")
        col1, col2, col3 = st.columns(3)
        with col1:
            organ_stomach = st.checkbox("Stomach", key="organ_stomach")
            organ_gallbladder = st.checkbox("Gallbladder", key="organ_gallbladder")
        with col2:
            organ_omentum = st.checkbox("Omentum", key="organ_omentum")
            organ_celiac = st.checkbox("Celiac axis", key="organ_celiac")
        with col3:
            organ_sma = st.checkbox("Superior mesenteric artery", key="organ_sma")
            organ_hepatic = st.checkbox("Common hepatic artery", key="organ_hepatic")
        
        organ_other = st.checkbox("Other", key="organ_other")
        if organ_other:
            organ_other_detail = st.text_input("Specify other organ:", key="organ_other_detail")
    
    if extent_cannot_determine:
        extent_explain = st.text_input("Explain:", key="extent_explain")
    
    # Lymphatic and/or Vascular Invasion
    st.markdown('<div class="subsection"><h4>Lymphatic and/or Vascular Invasion</h4></div>', unsafe_allow_html=True)
    lvi_options = ["Not identified", "Present", "Cannot be determined"]
    lvi = st.selectbox("Lymphatic and/or vascular invasion:", [""] + lvi_options, key="lvi")
    if lvi == "Cannot be determined":
        lvi_explain = st.text_input("Explain:", key="lvi_explain")
    
    # Perineural Invasion
    st.markdown('<div class="subsection"><h4>Perineural Invasion</h4></div>', unsafe_allow_html=True)
    pni_options = ["Not identified", "Present", "Cannot be determined"]
    pni = st.selectbox("Perineural invasion:", [""] + pni_options, key="pni")
    if pni == "Cannot be determined":
        pni_explain = st.text_input("Explain:", key="pni_explain")
    
    # Treatment Effect
    st.markdown('<div class="subsection"><h4>Treatment Effect</h4></div>', unsafe_allow_html=True)
    treatment_options = [
        "No known presurgical therapy",
        "Present, with no viable cancer cells (complete response, score 0)",
        "Present, with single cells or rare small groups of cancer cells (near complete response, score 1)",
        "Present, with residual cancer showing evident tumor regression (partial response, score 2)",
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
            margin_deep = st.checkbox("Deep (radial)", key="margin_deep")
            if margin_deep:
                margin_deep_detail = st.text_input("Deep margin details:", key="margin_deep_detail")
            
            margin_duodenal = st.checkbox("Duodenal mucosal", key="margin_duodenal")
            if margin_duodenal:
                margin_duodenal_detail = st.text_input("Duodenal margin details:", key="margin_duodenal_detail")
            
            margin_pancreatic_duct = st.checkbox("Pancreatic duct", key="margin_pancreatic_duct")
            if margin_pancreatic_duct:
                margin_pancreatic_duct_detail = st.text_input("Pancreatic duct margin details:", key="margin_pancreatic_duct_detail")
            
            margin_bile_duct = st.checkbox("Bile duct", key="margin_bile_duct")
            if margin_bile_duct:
                margin_bile_duct_detail = st.text_input("Bile duct margin details:", key="margin_bile_duct_detail")
        
        with col2:
            margin_pancreatic_neck = st.checkbox("Pancreatic neck / parenchymal", key="margin_pancreatic_neck")
            if margin_pancreatic_neck:
                margin_pancreatic_neck_detail = st.text_input("Pancreatic neck margin details:", key="margin_pancreatic_neck_detail")
            
            margin_uncinate = st.checkbox("Uncinate (retroperitoneal / SMA)", key="margin_uncinate")
            if margin_uncinate:
                margin_uncinate_detail = st.text_input("Uncinate margin details:", key="margin_uncinate_detail")
            
            margin_proximal = st.checkbox("Proximal (gastric or duodenal)", key="margin_proximal")
            if margin_proximal:
                margin_proximal_detail = st.text_input("Proximal margin details:", key="margin_proximal_detail")
            
            margin_distal = st.checkbox("Distal (duodenal or jejunal)", key="margin_distal")
            if margin_distal:
                margin_distal_detail = st.text_input("Distal margin details:", key="margin_distal_detail")
        
        margin_other = st.checkbox("Other", key="margin_other")
        if margin_other:
            margin_other_detail = st.text_input("Specify other margin:", key="margin_other_detail")
        
        margin_cannot_determine = st.checkbox("Cannot be determined", key="margin_cannot_determine")
        if margin_cannot_determine:
            margin_cannot_detail = st.text_input("Cannot be determined details:", key="margin_cannot_detail")
        
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
                "Cannot be determined",
                "Not applicable"
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
            involved_deep = st.checkbox("Deep (radial)", key="involved_deep")
            if involved_deep:
                involved_deep_detail = st.text_input("Deep involved details:", key="involved_deep_detail")
            
            involved_duodenal = st.checkbox("Duodenal mucosal", key="involved_duodenal")
            if involved_duodenal:
                involved_duodenal_detail = st.text_input("Duodenal involved details:", key="involved_duodenal_detail")
            
            involved_pancreatic_duct = st.checkbox("Pancreatic duct", key="involved_pancreatic_duct")
            if involved_pancreatic_duct:
                involved_pancreatic_duct_detail = st.text_input("Pancreatic duct involved details:", key="involved_pancreatic_duct_detail")
            
            involved_bile_duct = st.checkbox("Bile duct", key="involved_bile_duct")
            if involved_bile_duct:
                involved_bile_duct_detail = st.text_input("Bile duct involved details:", key="involved_bile_duct_detail")
        
        with col2:
            involved_pancreatic_neck = st.checkbox("Pancreatic neck / parenchymal", key="involved_pancreatic_neck")
            if involved_pancreatic_neck:
                involved_pancreatic_neck_detail = st.text_input("Pancreatic neck involved details:", key="involved_pancreatic_neck_detail")
            
            involved_uncinate = st.checkbox("Uncinate (retroperitoneal / SMA)", key="involved_uncinate")
            if involved_uncinate:
                involved_uncinate_detail = st.text_input("Uncinate involved details:", key="involved_uncinate_detail")
            
            involved_proximal = st.checkbox("Proximal (gastric or duodenal)", key="involved_proximal")
            if involved_proximal:
                involved_proximal_detail = st.text_input("Proximal involved details:", key="involved_proximal_detail")
            
            involved_distal = st.checkbox("Distal (duodenal or jejunal)", key="involved_distal")
            if involved_distal:
                involved_distal_detail = st.text_input("Distal involved details:", key="involved_distal_detail")
        
        involved_other = st.checkbox("Other", key="involved_other")
        if involved_other:
            involved_other_detail = st.text_input("Specify other involved margin:", key="involved_other_detail")
        
        involved_cannot_determine = st.checkbox("Cannot be determined", key="involved_cannot_determine")
        if involved_cannot_determine:
            involved_cannot_detail = st.text_input("Cannot be determined details:", key="involved_cannot_detail")
    
    elif margin_status == "Other":
        margin_other_status = st.text_input("Specify other:", key="margin_other_status")
    elif margin_status == "Cannot be determined":
        margin_cannot_explain = st.text_input("Explain:", key="margin_cannot_explain")
    
    # Margin Status for Dysplasia and Intraepithelial Neoplasia
    st.markdown('<div class="subsection"><h4>Margin Status for Dysplasia and Intraepithelial Neoplasia</h4></div>', unsafe_allow_html=True)
    
    dysplasia_status = st.radio(
        "Dysplasia margin status:",
        [
            "All margins negative for high-grade dysplasia and / or high-grade intraepithelial neoplasia",
            "High-grade dysplasia and / or high-grade intraepithelial neoplasia present at margin",
            "Other",
            "Cannot be determined",
            "Not applicable"
        ],
        key="dysplasia_status"
    )
    
    if dysplasia_status == "High-grade dysplasia and / or high-grade intraepithelial neoplasia present at margin":
        st.write("**Margin(s) Involved by High-Grade Dysplasia:**")
        
        col1, col2 = st.columns(2)
        with col1:
            hgd_pancreatic_neck = st.checkbox("Pancreatic neck / parenchymal margin", key="hgd_pancreatic_neck")
            if hgd_pancreatic_neck:
                hgd_pancreatic_neck_detail = st.text_input("HGD Pancreatic neck details:", key="hgd_pancreatic_neck_detail")
            
            hgd_bile_duct = st.checkbox("Bile duct margin", key="hgd_bile_duct")
            if hgd_bile_duct:
                hgd_bile_duct_detail = st.text_input("HGD Bile duct details:", key="hgd_bile_duct_detail")
        
        with col2:
            hgd_proximal = st.checkbox("Proximal (gastric or duodenal)", key="hgd_proximal")
            if hgd_proximal:
                hgd_proximal_detail = st.text_input("HGD Proximal details:", key="hgd_proximal_detail")
            
            hgd_distal = st.checkbox("Distal (duodenal or jejunal)", key="hgd_distal")
            if hgd_distal:
                hgd_distal_detail = st.text_input("HGD Distal details:", key="hgd_distal_detail")
        
        hgd_other = st.checkbox("Other", key="hgd_other")
        if hgd_other:
            hgd_other_detail = st.text_input("HGD Other details:", key="hgd_other_detail")
        
        hgd_cannot = st.checkbox("Cannot be determined", key="hgd_cannot")
        if hgd_cannot:
            hgd_cannot_detail = st.text_input("HGD Cannot be determined details:", key="hgd_cannot_detail")
    
    elif dysplasia_status == "Other":
        dysplasia_other = st.text_input("Specify other:", key="dysplasia_other")
    elif dysplasia_status == "Cannot be determined":
        dysplasia_explain = st.text_input("Explain:", key="dysplasia_explain")
    
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
        "pTis: Carcinoma in situ",
        "pT1a: Tumor limited to ampulla of Vater or sphincter of Oddi",
        "pT1b: Tumor invades beyond the sphincter of Oddi (perisphincteric invasion) and / or into the duodenal submucosa",
        "pT1 (subcategory cannot be determined)",
        "pT2: Tumor invades into the muscularis propria of the duodenum",
        "pT3a: Tumor directly invades pancreas (up to 0.5 cm)",
        "pT3b: Tumor extends more than 0.5 cm into the pancreas, or extends into peripancreatic tissue or periduodenal tissue or duodenal serosa without involvement of the celiac axis or superior mesenteric artery",
        "pT3 (subcategory cannot be determined)",
        "pT4: Tumor involves the celiac axis, superior mesenteric artery, and / or common hepatic artery, irrespective of size"
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
        "pN1: Metastasis to one to three regional lymph nodes",
        "pN2: Metastasis to four or more regional lymph nodes"
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
    additional_dysplasia = st.checkbox("Dysplasia / adenoma", key="additional_dysplasia")
    additional_other = st.checkbox("Other", key="additional_other")
    
    if additional_other:
        additional_other_detail = st.text_input("Specify other findings:", key="additional_other_detail")
    
    # ========== SPECIAL STUDIES SECTION ==========
    st.markdown('<div class="section-header"><h2>🔬 SPECIAL STUDIES</h2></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="subsection"><h4>Ancillary Studies</h4></div>', unsafe_allow_html=True)
    
    ancillary_performed = st.radio(
        "Ancillary studies:",
        ["Not performed", "Performed"],
        key="ancillary_performed"
    )
    
    if ancillary_performed == "Performed":
        ancillary_details = st.text_area("Specify ancillary studies performed:", key="ancillary_details")
    
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
        st.markdown("### 📄 AMPULLA OF VATER PATHOLOGY REPORT")
        
        # Create comprehensive report content
        report_content = f"""AMPULLA OF VATER PATHOLOGY REPORT
Date: {datetime.now().strftime('%Y-%m-%d')}
Standard: AJCC 8th Edition
Protocol Posting Date: June 2025

CASE SUMMARY (AMPULLA OF VATER)
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
        
        # Add Tumor Section
        report_content += f"\nTUMOR\n"
        
        if st.session_state.get('tumor_site'):
            report_content += f"Tumor Site: {st.session_state.tumor_site}\n"
            if st.session_state.get('tumor_site_detail'):
                report_content += f"  Details: {st.session_state.tumor_site_detail}\n"
        
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
        if st.session_state.get('tumor_size_type'):
            report_content += f"Tumor Size Type: {st.session_state.tumor_size_type}\n"
            
            if st.session_state.get('tumor_size_type') == "Unifocal invasive carcinoma":
                if st.session_state.get('size_cm'):
                    size_text = f"{st.session_state.size_cm} cm"
                    if st.session_state.get('additional_dims') and st.session_state.get('size_x') and st.session_state.get('size_y'):
                        size_text += f" x {st.session_state.size_x} cm x {st.session_state.size_y} cm"
                    report_content += f"  Greatest dimension: {size_text}\n"
            
            elif st.session_state.get('tumor_size_type') == "Multifocal invasive carcinoma in association with IAPN":
                if st.session_state.get('largest_focus'):
                    report_content += f"  Size of largest focus: {st.session_state.largest_focus} cm\n"
                if st.session_state.get('aggregate_size'):
                    report_content += f"  Aggregate size of all foci: {st.session_state.aggregate_size} cm\n"
                if st.session_state.get('invasive_percentage'):
                    report_content += f"  Invasive component percentage: {st.session_state.invasive_percentage}%\n"
            
            elif st.session_state.get('tumor_size_type') == "Cannot be determined":
                if st.session_state.get('size_explain'):
                    report_content += f"  Explanation: {st.session_state.size_explain}\n"
        
        # Tumor Extent
        extent_findings = []
        extent_checkboxes = {
            'extent_cis': 'Carcinoma in situ / high-grade dysplasia',
            'extent_ampulla': 'Limited to ampulla of Vater or sphincter of Oddi',
            'extent_sphincter': 'Invades beyond sphincter of Oddi',
            'extent_submucosa': 'Invades into duodenal submucosa',
            'extent_muscularis': 'Invades into muscularis propria of duodenum',
            'extent_pancreas_05': 'Directly invades pancreas (up to 0.5 cm)',
            'extent_pancreas_more': 'Extends more than 0.5 cm into pancreas',
            'extent_peripancreatic': 'Extends into peripancreatic soft tissues',
            'extent_periduodenal': 'Extends into periduodenal tissue',
            'extent_serosa': 'Extends into duodenal serosa',
            'extent_other_organs': 'Invades other adjacent organ(s)',
            'extent_no_evidence': 'No evidence of primary tumor',
            'extent_cannot_determine': 'Cannot be determined'
        }
        
        for key, label in extent_checkboxes.items():
            if st.session_state.get(key):
                extent_findings.append(label)
        
        if extent_findings:
            report_content += f"Tumor Extent: {', '.join(extent_findings)}\n"
        
        # Adjacent organs if applicable
        if st.session_state.get('extent_other_organs'):
            organ_findings = []
            organ_checkboxes = {
                'organ_stomach': 'Stomach',
                'organ_gallbladder': 'Gallbladder',
                'organ_omentum': 'Omentum',
                'organ_celiac': 'Celiac axis',
                'organ_sma': 'Superior mesenteric artery',
                'organ_hepatic': 'Common hepatic artery'
            }
            
            for key, label in organ_checkboxes.items():
                if st.session_state.get(key):
                    organ_findings.append(label)
            
            if st.session_state.get('organ_other'):
                organ_findings.append("Other")
                if st.session_state.get('organ_other_detail'):
                    organ_findings.append(f"({st.session_state.organ_other_detail})")
            
            if organ_findings:
                report_content += f"  Adjacent organs involved: {', '.join(organ_findings)}\n"
        
        if st.session_state.get('lvi'):
            report_content += f"Lymphatic and/or Vascular Invasion: {st.session_state.lvi}\n"
        
        if st.session_state.get('pni'):
            report_content += f"Perineural Invasion: {st.session_state.pni}\n"
        
        if st.session_state.get('treatment_effect'):
            report_content += f"Treatment Effect: {st.session_state.treatment_effect}\n"
        
        if st.session_state.get('tumor_comment'):
            report_content += f"Tumor Comment: {st.session_state.tumor_comment}\n"
        
        # Add Margins Section
        report_content += f"\nMARGINS\n"
        
        if st.session_state.get('margin_status'):
            report_content += f"Margin Status for Invasive Carcinoma: {st.session_state.margin_status}\n"
        
        # Closest margins if all negative
        if st.session_state.get('margin_status') == "All margins negative for invasive carcinoma":
            closest_margins = []
            margin_checkboxes = {
                'margin_deep': 'Deep (radial)',
                'margin_duodenal': 'Duodenal mucosal',
                'margin_pancreatic_duct': 'Pancreatic duct',
                'margin_bile_duct': 'Bile duct',
                'margin_pancreatic_neck': 'Pancreatic neck / parenchymal',
                'margin_uncinate': 'Uncinate (retroperitoneal / SMA)',
                'margin_proximal': 'Proximal (gastric or duodenal)',
                'margin_distal': 'Distal (duodenal or jejunal)'
            }
            
            for key, label in margin_checkboxes.items():
                if st.session_state.get(key):
                    closest_margins.append(label)
            
            if closest_margins:
                report_content += f"  Closest margin(s): {', '.join(closest_margins)}\n"
            
            # Distance information
            if st.session_state.get('distance_method'):
                if st.session_state.get('distance_method') == "Exact distance in cm" and st.session_state.get('distance_cm'):
                    report_content += f"  Distance to closest margin: {st.session_state.distance_cm} cm\n"
                elif st.session_state.get('distance_method') == "Exact distance in mm" and st.session_state.get('distance_mm'):
                    report_content += f"  Distance to closest margin: {st.session_state.distance_mm} mm\n"
                elif st.session_state.get('distance_method') in ["Greater than 1 cm", "Greater than 10 mm"]:
                    report_content += f"  Distance to closest margin: {st.session_state.distance_method}\n"
        
        # Involved margins if positive
        elif st.session_state.get('margin_status') == "Invasive carcinoma present at margin":
            involved_margins = []
            involved_checkboxes = {
                'involved_deep': 'Deep (radial)',
                'involved_duodenal': 'Duodenal mucosal',
                'involved_pancreatic_duct': 'Pancreatic duct',
                'involved_bile_duct': 'Bile duct',
                'involved_pancreatic_neck': 'Pancreatic neck / parenchymal',
                'involved_uncinate': 'Uncinate (retroperitoneal / SMA)',
                'involved_proximal': 'Proximal (gastric or duodenal)',
                'involved_distal': 'Distal (duodenal or jejunal)'
            }
            
            for key, label in involved_checkboxes.items():
                if st.session_state.get(key):
                    involved_margins.append(label)
            
            if involved_margins:
                report_content += f"  Involved margin(s): {', '.join(involved_margins)}\n"
        
        if st.session_state.get('dysplasia_status'):
            report_content += f"Margin Status for Dysplasia and Intraepithelial Neoplasia: {st.session_state.dysplasia_status}\n"
        
        if st.session_state.get('margin_comment'):
            report_content += f"Margin Comment: {st.session_state.margin_comment}\n"
        
        # Add Regional Lymph Nodes Section
        report_content += f"\nREGIONAL LYMPH NODES\n"
        
        if st.session_state.get('ln_status'):
            report_content += f"Regional Lymph Node Status: {st.session_state.ln_status}\n"
            
            if st.session_state.get('ln_tumor_status'):
                report_content += f"  Tumor status: {st.session_state.ln_tumor_status}\n"
            
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
            distant_sites.append("Non-regional lymph node(s)")
        if st.session_state.get('dm_liver'):
            distant_sites.append("Liver")
        if st.session_state.get('dm_other'):
            distant_sites.append("Other")
        if st.session_state.get('dm_cannot_determine'):
            distant_sites.append("Cannot be determined")
        
        if distant_sites:
            report_content += f"Distant Site(s) Involved: {', '.join(distant_sites)}\n"
        
        # Add pTNM Classification Section
        report_content += f"\npTNM CLASSIFICATION (AJCC 8th Edition)\n"
        
        report_content += "Reporting of pT, pN, and (when applicable) pM categories is based on information\navailable to the pathologist at the time the report is issued.\n\n"
        
        # Modified classification
        modified_classifications = []
        if st.session_state.get('modified_y'):
            modified_classifications.append("y (post-neoadjuvant therapy)")
        if st.session_state.get('modified_r'):
            modified_classifications.append("r (recurrence)")
        
        if modified_classifications:
            report_content += f"Modified Classification: {', '.join(modified_classifications)}\n"
        
        if st.session_state.get('pt_category'):
            report_content += f"pT: {st.session_state.pt_category}\n"
        
        if st.session_state.get('t_suffix_applicable') == "(m) multiple primary synchronous tumors in a single organ":
            report_content += f"T Suffix: (m) multiple primary synchronous tumors in a single organ\n"
        
        if st.session_state.get('pn_category'):
            report_content += f"pN: {st.session_state.pn_category}\n"
        
        if st.session_state.get('pm_category') and st.session_state.pm_category != "Not applicable - pM cannot be determined from the submitted specimen(s)":
            report_content += f"pM: {st.session_state.pm_category}\n"
        
        # Add Additional Findings Section
        report_content += f"\nADDITIONAL FINDINGS\n"
        
        additional_findings = []
        if st.session_state.get('additional_none'):
            additional_findings.append("None identified")
        if st.session_state.get('additional_dysplasia'):
            additional_findings.append("Dysplasia / adenoma")
        if st.session_state.get('additional_other'):
            additional_findings.append("Other")
            if st.session_state.get('additional_other_detail'):
                additional_findings.append(f"({st.session_state.additional_other_detail})")
        
        if additional_findings:
            report_content += f"Additional Findings: {', '.join(additional_findings)}\n"
        
        # Add Special Studies Section
        report_content += f"\nSPECIAL STUDIES\n"
        
        if st.session_state.get('ancillary_performed'):
            report_content += f"Ancillary Studies: {st.session_state.ancillary_performed}\n"
            if st.session_state.get('ancillary_details') and st.session_state.ancillary_performed == "Performed":
                report_content += f"  Details: {st.session_state.ancillary_details}\n"
        
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
            file_name=f"ampulla_vater_pathology_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
            mime="text/plain",
            use_container_width=True
        )

if __name__ == "__main__":
    main()