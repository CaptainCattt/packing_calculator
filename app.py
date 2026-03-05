import streamlit as st
import math

st.set_page_config(
    page_title="Packing Calculator",
    page_icon="📦",
    layout="wide",
)

# =============================
# MASTER CONFIG
# =============================

MASTER_STRUCTURE = {
    450: ["X1", "X2", "TCLC"],
    250: ["Sate tôm"],
    200: ["X1 (200)", "X2 (200)", "TCLC (200)"]
}

SPECIAL_STRUCTURE = {
    "BTHP": {
        "pack_size": 50,
        "weight_per_box": 12
    }
}

PACK_CONFIG = {
    450: {"pack_size": 20, "weight_per_box": 10.5},
    250: {"pack_size": 25, "weight_per_box": 7.46},
    200: {"pack_size": 50, "weight_per_box": 12}
}

# =============================
# PREMIUM CSS
# =============================

st.markdown("""
<style>

.block-container {
    padding-top: 1.5rem;
    max-width: 900px;
}

.section-card {
    padding: 20px;
    border-radius: 20px;
    background: #ffffff;
    box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    margin-bottom: 20px;
}

.metric-card {
    padding: 18px;
    border-radius: 16px;
    background: linear-gradient(135deg, #059669, #0d9488);
    color: white;
    text-align: center;
    transition: 0.3s;
    margin-bottom: 20px;
}

.metric-card:hover {
    transform: translateY(-4px);
}

.metric-special {
    background: linear-gradient(135deg, #2563eb, #06b6d4);
}

.metric-grand {
    background: linear-gradient(135deg, #1f2937, #111827);
}

.big-number {
    font-size: 26px;
    font-weight: 800;
}

.small-label {
    font-size: 12px;
    opacity: 0.85;
    letter-spacing: 0.5px;
}
            
/* ===== Centered Hero Header ===== */
.hero-wrapper {
    text-align: center;
    margin-top: 24px;
    padding: 10px;
    border-radius: 24px;
    background: linear-gradient(135deg, #f97316, #ef4444);
    color: white;
    margin-bottom: 5px;
    box-shadow: 0 15px 40px rgba(239,68,68,0.25);
}

.hero-title {
    font-size: 28px;
    font-weight: 800;
    letter-spacing: -0.5px;
}

.hero-subtitle {
    font-size: 15px;
    opacity: 0.9;
    letter-spacing: 0.5px;
}

</style>
""", unsafe_allow_html=True)


# =============================
# HEADER
# =============================
# =============================
# SIDEBAR - PACKING SPEC
# =============================


st.sidebar.markdown("""
<div style="
    background: linear-gradient(135deg,#6366f1,#8b5cf6);
    padding:10px;
    border-radius:14px;
    color:white;
    text-align:center;
    margin-bottom:10px;
    box-shadow:0 6px 16px rgba(0,0,0,0.15);
">

<div style="font-size:18px;font-weight:800;">
📦 QUY CÁCH ĐÓNG THÙNG
</div>

<div style="font-size:13px;opacity:0.9;">
Thông tin chi tiết các loại thùng
</div>

</div>
""", unsafe_allow_html=True)

with st.sidebar.expander("HŨ 200G", expanded=False):
    st.markdown("""
- **20 hũ/thùng**  
  22x22x22 cm – **4.65 kg**

- **25 hũ/thùng**  
  22x22x22 cm – **5.65 kg**

- **50 hũ/thùng**  
  28x28x24 cm – **12 kg**

- **60 hũ/thùng**  
  34x26x32.5 cm – **15.5 kg**
""")

with st.sidebar.expander("SA TẾ TÔM 200G", expanded=False):
    st.markdown("""
- **25 hũ/thùng**  
  34x26x32.5 cm – **7.46 kg**

⚠️ Hũ có quấn bóng xốp, nắp giòn dễ bể.
""")

with st.sidebar.expander("BTHP 200G", expanded=False):
    st.markdown("""
- **12 hũ/thùng**  
  34x26x32.5 cm – **4 kg**
""")

with st.sidebar.expander("HŨ 450G", expanded=False):
    st.markdown("""
- **20 hũ/thùng**  
  29x12.5x36 cm – **10.5 kg**
""")

st.markdown("""
<div class="hero-wrapper">
    <div class="hero-title">📦 Packing Calculator 📦</div>
    <div class="hero-subtitle">Multi Size Management Dashboard</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="font-size:24px; font-weight:800; margin:25px 0 10px 0;">
    📝 THÔNG TIN ĐẦU VÀO - NHẬP SỐ LƯỢNG HŨ 📝
    </div>
""", unsafe_allow_html=True)

grand_total_boxes = 0
grand_total_weight = 0
grand_total_jars = 0

# =============================
# MAIN SIZE BLOCKS
# =============================

for weight, types in MASTER_STRUCTURE.items():

    config = PACK_CONFIG[weight]
    pack_size = config["pack_size"]
    weight_per_box = config["weight_per_box"]

    with st.expander(f"{weight}g  -  {pack_size} hũ/thùng  - {weight_per_box} kg/thùng", expanded=False):

        cols = st.columns(len(types))
        inputs = []

        for i, t in enumerate(types):
            with cols[i]:
                qty = st.number_input(
                    t,
                    min_value=0,
                    step=1,
                    key=f"{weight}_{t}"
                )
                inputs.append(qty)

        total_jars = sum(inputs)

        if total_jars > 0:

            total_boxes = math.ceil(total_jars / pack_size)
            full_boxes = total_jars // pack_size
            remaining = total_jars % pack_size
            weight_per_jar = weight_per_box / pack_size

            total_weight = (
                full_boxes * weight_per_box
                + remaining * weight_per_jar
            )

            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.markdown(f"""
                <div class="metric-card">
                <div class="small-label">TỔNG HŨ</div>
                <div class="big-number">{total_jars:,}</div>
                </div>
                """, unsafe_allow_html=True)

            with c2:
                st.markdown(f"""
                <div class="metric-card">
                <div class="small-label">TỔNG THÙNG</div>
                <div class="big-number">{total_boxes:,}</div>
                </div>
                """, unsafe_allow_html=True)

            with c3:
                st.markdown(f"""
                <div class="metric-card">
                <div class="small-label">THÙNG ĐẦY | LẺ</div>
                <div class="big-number">{full_boxes} | {remaining}</div>
                </div>
                """, unsafe_allow_html=True)

            with c4:
                st.markdown(f"""
                <div class="metric-card">
                <div class="small-label">TỔNG KG</div>
                <div class="big-number">{total_weight:,.3f}</div>
                </div>
                """, unsafe_allow_html=True)

            grand_total_boxes += total_boxes
            grand_total_weight += total_weight
            grand_total_jars += total_jars

# =============================
# BTHP BLOCK (SPECIAL STYLE)
# =============================

config = SPECIAL_STRUCTURE["BTHP"]

with st.expander("BTHP 200g", expanded=False):

    pack_size = config["pack_size"]
    weight_per_box = config["weight_per_box"]

    bthp_qty = st.number_input("Số lượng BTHP", min_value=0, step=1)

    if bthp_qty > 0:

        total_boxes = math.ceil(bthp_qty / pack_size)
        full_boxes = bthp_qty // pack_size
        remaining = bthp_qty % pack_size
        weight_per_jar = weight_per_box / pack_size

        total_weight = (
            full_boxes * weight_per_box
            + remaining * weight_per_jar
        )

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f"""
            <div class="metric-card metric-special">
            <div class="small-label">TỔNG HŨ</div>
            <div class="big-number">{bthp_qty:,}</div>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="metric-card metric-special">
            <div class="small-label">TỔNG THÙNG</div>
            <div class="big-number">{total_boxes:,}</div>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="metric-card metric-special">
            <div class="small-label">THÙNG ĐẦY | LẺ</div>
            <div class="big-number">{full_boxes} | {remaining}</div>
            </div>
            """, unsafe_allow_html=True)

        with c4:
            st.markdown(f"""
            <div class="metric-card metric-special">
            <div class="small-label">TỔNG KG</div>
            <div class="big-number">{total_weight:,.3f}</div>
            </div>
            """, unsafe_allow_html=True)

        grand_total_boxes += total_boxes
        grand_total_weight += total_weight
        grand_total_jars += bthp_qty

# =============================
# GRAND TOTAL BANNER
# =============================

if grand_total_jars > 0:

    st.markdown("""
    <div style="font-size:24px; font-weight:800; margin:25px 0 10px 0;">
    🚚 TỔNG KHỐI LƯỢNG CHI TIẾT
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
        <div class="metric-card metric-grand">
        <div class="small-label">TỔNG HŨ</div>
        <div class="big-number">{grand_total_jars:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="metric-card metric-grand">
        <div class="small-label">TỔNG THÙNG</div>
        <div class="big-number">{grand_total_boxes:,}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="metric-card metric-grand">
        <div class="small-label">TỔNG KG</div>
        <div class="big-number">{grand_total_weight:,.3f}</div>
        </div>
        """, unsafe_allow_html=True)
