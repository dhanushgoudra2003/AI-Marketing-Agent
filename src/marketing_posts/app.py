from pathlib import Path

import streamlit as st

from marketing_posts.main import DEFAULT_REPORTS_DIR, generate_marketing_report

st.set_page_config(
    page_title="AI Marketing Strategy Generator",
    layout="wide",
)

# Custom Style Injection for Premium Modern Look
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');
    
    /* Global Background and Typography */
    html, body, [class*="css"], .stApp {
        font-family: 'Outfit', sans-serif !important;
        background: radial-gradient(circle at top, #0f172a 0%, #020617 100%) !important;
        color: #f1f5f9 !important;
    }
    
    /* Hide Streamlit Sidebar completely */
    div[data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* Centered Gradient Title */
    .main-title-centered {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 50%, #f472b6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 1.5rem !important;
        margin-bottom: 1.5rem !important;
        text-align: center;
        letter-spacing: -1.5px;
        line-height: 1.15 !important;
    }

    /* Subtitle */
    .subtitle-centered {
        text-align: center;
        color: #94a3b8;
        font-size: 1.25rem;
        max-width: 700px;
        margin: -0.5rem auto 2.5rem auto;
        line-height: 1.6;
    }

    /* Standard Title for dashboard */
    .main-title {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        background: linear-gradient(135deg, #60a5fa 0%, #a78bfa 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.5px;
    }

    /* Subheader accents */
    h2, h3, .stSubheader {
        font-weight: 600 !important;
        color: #f1f5f9 !important;
        border-bottom: 2px solid rgba(255, 255, 255, 0.08);
        padding-bottom: 8px;
        margin-top: 20px !important;
    }
    
    /* Dark Mode Inputs */
    input, textarea {
        background-color: rgba(2, 6, 23, 0.8) !important;
        color: #f8fafc !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        padding: 14px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }
    
    input:focus, textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.4) !important;
    }

    /* Widget Labels (Company domain, Product description) */
    div[data-testid="stWidgetLabel"] p,
    label {
        color: #f1f5f9 !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
    }
    
    /* Input Placeholder Color */
    input::placeholder,
    textarea::placeholder {
        color: #64748b !important;
        opacity: 0.8 !important;
    }

    /* Styled Container for Centered Form Card (Glassmorphism) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 24px !important;
        padding: 35px !important;
        backdrop-filter: blur(16px) !important;
        box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.7) !important;
    }

    /* Primary button design (Blue-to-Indigo Gradient) */
    div.stButton > button[data-testid="stBaseButton-primary"],
    div.stButton > button[kind="primary"],
    div.stButton > button:not([data-testid="stBaseButton-secondary"]):not([kind="secondary"]) {
        background: linear-gradient(135deg, #2563eb 0%, #4f46e5 100%) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        padding: 14px 28px !important;
        height: auto !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        box-shadow: 0 8px 20px -4px rgba(99, 102, 241, 0.4) !important;
        display: block !important;
        margin: 10px auto 0 auto !important;
        width: auto !important;
        min-width: 220px !important;
        max-width: 300px !important;
    }
    
    div.stButton > button[data-testid="stBaseButton-primary"]:hover,
    div.stButton > button[kind="primary"]:hover,
    div.stButton > button:not([data-testid="stBaseButton-secondary"]):not([kind="secondary"]):hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 28px -4px rgba(99, 102, 241, 0.6) !important;
        filter: brightness(1.15) !important;
        background: linear-gradient(135deg, #1d4ed8 0%, #4338ca 100%) !important;
        color: #ffffff !important;
    }
    
    div.stButton > button[data-testid="stBaseButton-primary"]:active,
    div.stButton > button[kind="primary"]:active,
    div.stButton > button:not([data-testid="stBaseButton-secondary"]):not([kind="secondary"]):active {
        transform: translateY(1px) !important;
    }

    /* Override secondary buttons (like back button) to keep them outline-styled */
    div.stButton > button[data-testid="stBaseButton-secondary"],
    div.stButton > button[kind="secondary"] {
        background-color: rgba(15, 23, 42, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #cbd5e1 !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 12px 16px !important;
        width: 100% !important;
        margin: 0 !important;
        display: inline-block !important;
        box-shadow: none !important;
    }

    div.stButton > button[data-testid="stBaseButton-secondary"]:hover,
    div.stButton > button[kind="secondary"]:hover {
        background-color: rgba(15, 23, 42, 0.8) !important;
        border-color: rgba(255, 255, 255, 0.2) !important;
        color: #ffffff !important;
        transform: translateY(-1px) !important;
    }

    /* Info messages styling */
    div[data-testid="stNotification"] {
        background-color: rgba(30, 58, 138, 0.3) !important;
        color: #93c5fd !important;
        border: 1px solid rgba(59, 130, 246, 0.2) !important;
        border-left: 4px solid #3b82f6 !important;
        border-radius: 12px !important;
    }

    /* Success message style override */
    div[data-testid="stNotification"][data-status="success"] {
        background-color: rgba(6, 78, 59, 0.3) !important;
        color: #6ee7b7 !important;
        border: 1px solid rgba(16, 185, 129, 0.2) !important;
        border-left: 4px solid #10b981 !important;
    }

    /* Container Card style for report preview */
    .report-container {
        background-color: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 16px !important;
        padding: 30px !important;
        color: #f1f5f9 !important;
        box-shadow: 0 10px 20px -10px rgba(0, 0, 0, 0.5) !important;
        margin-top: 15px;
    }

    /* Secondary action download buttons styling */
    button[kind="secondary"] {
        background-color: rgba(15, 23, 42, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #cbd5e1 !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 12px 16px !important;
        transition: all 0.2s ease !important;
        width: 100%;
        margin-bottom: 8px;
    }
    
    button[kind="secondary"]:hover {
        background-color: rgba(15, 23, 42, 0.8) !important;
        border-color: rgba(255, 255, 255, 0.2) !important;
        color: #ffffff !important;
        transform: translateY(-1px) !important;
    }

    /* Section divider style */
    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.08), transparent);
        margin: 50px 0;
    }

    /* Section titles styling */
    .section-title {
        font-size: 2.2rem !important;
        font-weight: 700 !important;
        text-align: center;
        margin-bottom: 12px !important;
        background: linear-gradient(135deg, #f1f5f9 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        border-bottom: none !important;
        padding-bottom: 0 !important;
    }

    .section-subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.05rem;
        max-width: 600px;
        margin: 0 auto 35px auto;
        line-height: 1.5;
    }

    /* Feature Grid Card style */
    .feature-card {
        background: rgba(15, 23, 42, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        border-color: rgba(99, 102, 241, 0.3);
        background: rgba(15, 23, 42, 0.6);
        transform: translateY(-3px);
        box-shadow: 0 10px 20px -10px rgba(0, 0, 0, 0.5);
    }

    .feature-icon {
        font-size: 1.75rem;
        margin-bottom: 12px;
    }

    .feature-title {
        font-weight: 700;
        color: #f1f5f9;
        font-size: 1.1rem;
        margin-bottom: 8px;
    }

    .feature-desc {
        color: #94a3b8;
        font-size: 0.9rem;
        line-height: 1.5;
    }

    /* Agent Card style */
    .agent-card {
        background: rgba(15, 23, 42, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 24px;
        transition: all 0.3s ease;
    }

    .agent-card:hover {
        border-color: rgba(99, 102, 241, 0.3);
        transform: translateY(-2px);
    }

    .agent-badge {
        background: rgba(99, 102, 241, 0.15);
        color: #a5b4fc;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 12px;
    }

    .agent-name {
        font-size: 1.15rem;
        font-weight: 700;
        color: #f8fafc;
        margin-bottom: 6px;
    }

    .agent-desc {
        color: #94a3b8;
        font-size: 0.85rem;
        line-height: 1.5;
    }

    /* FAQ Card style */
    .faq-card {
        background: rgba(15, 23, 42, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 15px;
    }

    .faq-question {
        font-weight: 600;
        color: #f1f5f9;
        font-size: 1rem;
        margin-bottom: 8px;
    }

    .faq-answer {
        color: #94a3b8;
        font-size: 0.85rem;
        line-height: 1.5;
    }

    /* Citation Box Design */
    .citation-card {
        background-color: rgba(15, 23, 42, 0.4) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 12px;
        padding: 16px;
        margin-bottom: 12px;
        transition: all 0.2s ease;
    }
    
    .citation-card:hover {
        border-color: rgba(99, 102, 241, 0.3) !important;
        background-color: rgba(15, 23, 42, 0.6) !important;
        transform: translateY(-1px) !important;
    }

    .citation-title {
        font-weight: 600;
        color: #60a5fa !important;
        font-size: 0.95rem;
        margin-bottom: 4px;
        text-decoration: none;
        display: block;
    }
    
    .citation-title:hover {
        text-decoration: underline;
    }

    .citation-snippet {
        color: #94a3b8;
        font-size: 0.85rem;
        line-height: 1.4;
        margin-bottom: 6px;
    }
    
    .citation-meta {
        color: #475569;
        font-size: 0.75rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize Session State to hold generation results
if "result" not in st.session_state:
    st.session_state.result = None

# Step 1: Centered Landing Page Form
if st.session_state.result is None:
    col_left, col_mid, col_right = st.columns([1, 2, 1])
    
    with col_mid:
        st.markdown('<h1 class="main-title-centered">Supercharge Your Marketing Strategy</h1>', unsafe_allow_html=True)
        st.markdown('<p class="subtitle-centered">Autonomous agent crews research your market, dissect competitors, outline channels, and write copy in minutes.</p>', unsafe_allow_html=True)
        
        # Center card form wrapper using st.container(border=True) which matches our CSS override
        with st.container(border=True):
            company_domain = st.text_input("Company domain", placeholder="example.com")
            project_description = st.text_area(
                "Product or project description",
                placeholder="Describe what the product does, who it serves, and what makes it different.",
                height=160,
            )
            generate = st.button("Generate Report", type="primary", use_container_width=True)
            
        if generate:
            if not company_domain.strip() or not project_description.strip():
                st.error("Add both a company domain and product description.")
            else:
                with st.status("Generating marketing intelligence report...", expanded=True) as status:
                    st.write("Running research and strategy agents.")
                    try:
                        result = generate_marketing_report(
                            company_domain=company_domain,
                            project_description=project_description,
                            reports_dir=Path(DEFAULT_REPORTS_DIR),
                        )
                        st.session_state.result = result
                        status.update(label="Report generated", state="complete")
                        st.rerun()
                    except Exception as exc:
                        status.update(label="Generation failed", state="error")
                        st.error(str(exc))

    # Extended Landing Page Sections (Full-width sections centered below)
    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
    
    # 1. Features Grid
    st.markdown('<h2 class="section-title">Built-In Marketing Capabilities</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Our multi-agent system runs consecutive tasks to cover all aspects of growth marketing.</p>', unsafe_allow_html=True)
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        st.markdown(
            """
            <div class="feature-card" style="margin-bottom: 20px;">
                <div class="feature-icon">🔍</div>
                <div class="feature-title">Real-Time Competitor Analysis</div>
                <div class="feature-desc">Crawls competitor websites, identifies market gaps, and gathers active benchmarks to locate organic positioning advantages.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📈</div>
                <div class="feature-title">90-Day Growth Roadmap</div>
                <div class="feature-desc">Generates detailed phase-by-phase launch activities split into Days 1-30, 31-60, and 61-90 to guide your team's execution.</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_f2:
        st.markdown(
            """
            <div class="feature-card" style="margin-bottom: 20px;">
                <div class="feature-icon">🎯</div>
                <div class="feature-title">Demographic Profiling</div>
                <div class="feature-desc">Draws detailed target audience personas mapping their psychographics, key pain points, and typical online behaviors.</div>
            </div>
            <div class="feature-card">
                <div class="feature-icon">✍️</div>
                <div class="feature-title">Campaign Ideation & Copywriting</div>
                <div class="feature-desc">Brainstorms engaging promotional campaign narratives and drafts ready-to-run copy including titles and headlines.</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # 2. How it Works (Sequential Process)
    st.markdown('<h2 class="section-title">Our Autonomous Workflow</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">How our CrewAI agents collaborate to construct your marketing strategy.</p>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div style="background: rgba(15, 23, 42, 0.4); border: 1px solid rgba(255, 255, 255, 0.05); border-radius: 20px; padding: 35px; box-shadow: 0 4px 6px rgba(0,0,0,0.025);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 20px; flex-wrap: wrap;">
                <div style="flex: 1; min-width: 200px;">
                    <div style="color: #60a5fa; font-weight: 800; font-size: 1.75rem; margin-bottom: 8px;">01</div>
                    <div style="color: #f1f5f9; font-weight: 700; font-size: 1.1rem; margin-bottom: 8px;">Gather Evidence</div>
                    <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">Analyst crawls search result URLs using the Serper API to collect facts and site overview details.</p>
                </div>
                <div style="font-size: 1.5rem; color: #475569; align-self: center; display: block;">➔</div>
                <div style="flex: 1; min-width: 200px;">
                    <div style="color: #a78bfa; font-weight: 800; font-size: 1.75rem; margin-bottom: 8px;">02</div>
                    <div style="color: #f1f5f9; font-weight: 700; font-size: 1.1rem; margin-bottom: 8px;">Structure Strategy</div>
                    <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">Strategist outlines KPIs, identifies target demographics, and maps channel recommendations.</p>
                </div>
                <div style="font-size: 1.5rem; color: #475569; align-self: center; display: block;">➔</div>
                <div style="flex: 1; min-width: 200px;">
                    <div style="color: #f472b6; font-weight: 800; font-size: 1.75rem; margin-bottom: 8px;">03</div>
                    <div style="color: #f1f5f9; font-weight: 700; font-size: 1.1rem; margin-bottom: 8px;">Content Creation</div>
                    <p style="color: #94a3b8; font-size: 0.85rem; line-height: 1.5;">Creative writer brainstorms themed copy campaigns and structures headlines and call-to-actions.</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

    # 3. Meet the Crew (The Agents)
    st.markdown('<h2 class="section-title">Meet Your Agent Crew</h2>', unsafe_allow_html=True)
    st.markdown('<p class="section-subtitle">Four specialized AI personas working in tandem to build your report.</p>', unsafe_allow_html=True)
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown(
            """
            <div class="agent-card" style="margin-bottom: 20px;">
                <span class="agent-badge">RESEARCHER</span>
                <div class="agent-name">Lead Market Analyst</div>
                <div class="agent-desc">Specializes in online business landscapes. Responsible for analyzing products, competitors, and collecting real-time evidence.</div>
            </div>
            <div class="agent-card">
                <span class="agent-badge" style="background: rgba(167, 139, 250, 0.15); color: #c084fc;">STRATEGIST</span>
                <div class="agent-name">Chief Marketing Strategist</div>
                <div class="agent-desc">Aggregates analyst insights to compile your final structured strategy. Formulates positioning, channels, and KPIs.</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_c2:
        st.markdown(
            """
            <div class="agent-card" style="margin-bottom: 20px;">
                <span class="agent-badge" style="background: rgba(236, 72, 153, 0.15); color: #f472b6;">COPYWRITER</span>
                <div class="agent-name">Creative Content Creator</div>
                <div class="agent-desc">Resonates with target audience pain points to write compelling copy hooks, headlines, and descriptions.</div>
            </div>
            <div class="agent-card">
                <span class="agent-badge" style="background: rgba(34, 197, 94, 0.15); color: #4ade80;">LAUNCH EXPERT</span>
                <div class="agent-name">Growth Hacker</div>
                <div class="agent-desc">Designs technology product launch roadmaps, viral experiments, and trending keyword search terms.</div>
            </div>
            """,
            unsafe_allow_html=True
        )



    # 5. Footer
    st.markdown(
        """
        <div class="footer-container">
            <div>✨ AI Marketing Strategy Generator © 2026. Built with CrewAI & Streamlit.</div>
            <div style="margin-top: 6px; font-size: 0.75rem; color: #334155;">Privacy Secured. Local LLM execution active.</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Step 2: Dashboard Results Page
else:
    result = st.session_state.result
    
    # Navigation bar with back button
    col_back, col_title = st.columns([1, 4])
    with col_back:
        if st.button("⬅️ New Report", use_container_width=True):
            st.session_state.result = None
            st.rerun()
            
    with col_title:
        st.markdown(f'<h1 class="main-title" style="margin: 0 !important; padding: 0 !important; line-height: 1.2;">✨ Intelligence Report: {result.company_domain}</h1>', unsafe_allow_html=True)
        
    st.success(f"Saved report files to: {result.artifacts.output_dir}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Report Preview")
        # Wrap markdown preview in styled container
        st.markdown(f'<div class="report-container">\n\n{result.report_text}\n\n</div>', unsafe_allow_html=True)
        
    with col2:
        st.subheader("Artifacts")
        pdf_bytes = Path(result.artifacts.pdf_path).read_bytes()
        md_text = Path(result.artifacts.markdown_path).read_text(encoding="utf-8")
        json_text = Path(result.artifacts.json_path).read_text(encoding="utf-8")
        
        st.download_button(
            "Download PDF",
            data=pdf_bytes,
            file_name="marketing_report.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
        st.download_button(
            "Download Markdown",
            data=md_text,
            file_name="report.md",
            mime="text/markdown",
            use_container_width=True,
        )
        st.download_button(
            "Download JSON",
            data=json_text,
            file_name="report_data.json",
            mime="application/json",
            use_container_width=True,
        )
        
        st.subheader("Research Sources")
        if result.citations:
            for index, citation in enumerate(result.citations, start=1):
                snippet_html = f'<div class="citation-snippet">{citation.snippet}</div>' if citation.snippet else ''
                st.markdown(
                    f"""
                    <div class="citation-card">
                        <a class="citation-title" href="{citation.link}" target="_blank">
                            [{index}] {citation.title}
                        </a>
                        {snippet_html}
                        <div class="citation-meta">Retrieved: {citation.retrieved_at}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        else:
            st.caption("No citations were collected for this run.")
