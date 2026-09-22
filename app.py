import streamlit as st
from PIL import Image
from src.detector import detect_faults
from src.analyzer import analyze_result

st.set_page_config(
    page_title="HeritAI",
    page_icon="🏛️",
    layout="wide"
)

st.title("🏛️ HeritAI")
st.subheader("AI-Powered Heritage Monitoring & Preservation")

st.caption(
    "Visual intelligence for documenting heritage structures "
    "and identifying potential signs of deterioration."
)

st.write(
    "HeritAI helps document heritage structures and identify "
    "visible signs of deterioration using AI-based image analysis."
)

st.divider()

st.markdown(
    """
    **How HeritAI works:**  
    📷 Upload → 🔍 Analyze → ⚠️ Detect → 📋 Assess
    """
)

st.header("🔍 Heritage Structure Analysis")

uploaded_file = st.file_uploader(
    "Upload an image of a heritage structure",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Heritage Structure",
        use_container_width=True
    )

    st.success("Image uploaded successfully!")

    st.header("🔍 AI Visual Analysis")

    result = detect_faults(image)
    analysis = analyze_result(result)

    st.subheader("Preliminary Condition Assessment")

    st.write(f"**Severity:** {analysis['severity']}")
    st.write(analysis["summary"])

    for observation in result["observations"]:
        st.write("•", observation)
        
    if result["edge_strength"] > 7:
        st.warning(
            "⚠️ Potential Surface Irregularity Detected\n\n"
            "The image contains crack-like or irregular edge patterns "
            "that may require further visual inspection."
        )
    else:
        st.success(
            "✅ No prominent surface irregularity detected by the prototype."
        )

    st.write("### Image Metrics")
    st.write(f"Brightness: {result['brightness']}")
    st.write(f"Contrast: {result['contrast']}")
    st.write(f"Edge Strength: {result['edge_strength']}")