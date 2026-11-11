#!/usr/bin/env python3
"""Generate Meriem Beghili's CV (coherent with meriembeghili.github.io)."""
from fpdf import FPDF

SUP = "/System/Library/Fonts/Supplemental/"
INK = (28, 27, 25)
MUTED = (107, 103, 95)
ACCENT = (138, 109, 59)
LINE = (200, 195, 185)

class CV(FPDF):
    def header(self):
        pass
    def footer(self):
        self.set_y(-14)
        self.set_font("Helv", "", 8)
        self.set_text_color(*MUTED)
        self.cell(0, 5, f"Meriem Beghili · CV · {self.page_no()}", align="C")

pdf = CV(format="A4")
pdf.set_margins(20, 18, 20)
pdf.set_auto_page_break(True, margin=20)
pdf.add_page()
pdf.add_font("Geo", "", SUP + "Georgia.ttf")
pdf.add_font("Geo", "B", SUP + "Georgia Bold.ttf")
pdf.add_font("Geo", "I", SUP + "Georgia Italic.ttf")
pdf.add_font("Geo", "BI", SUP + "Georgia Bold Italic.ttf")
pdf.add_font("Helv", "", SUP + "Arial.ttf")
pdf.add_font("Helv", "B", SUP + "Arial Bold.ttf")
pdf.add_font("Helv", "I", SUP + "Arial Italic.ttf")

def h1(text):
    pdf.set_font("Geo", "", 26)
    pdf.set_text_color(*INK)
    pdf.cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")

def subtitle(text):
    pdf.set_font("Geo", "I", 11.5)
    pdf.set_text_color(*MUTED)
    pdf.multi_cell(0, 6, text, new_x="LMARGIN", new_y="NEXT")

def contact(line1):
    pdf.ln(2)
    pdf.set_font("Helv", "", 9)
    pdf.set_text_color(*INK)
    pdf.multi_cell(0, 5, line1, new_x="LMARGIN", new_y="NEXT")

def rule():
    pdf.ln(1.5)
    pdf.set_draw_color(*LINE)
    pdf.set_line_width(0.3)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(3)

def section(title):
    if pdf.get_y() > 240:
        pdf.add_page()
    else:
        pdf.ln(3)
    pdf.set_font("Helv", "B", 10.5)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 6, title.upper(), new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1.5)

def entry(title, right, desc=None):
    pdf.set_font("Geo", "B", 10.5)
    pdf.set_text_color(*INK)
    pdf.cell(0, 5.5, title, new_x="LMARGIN", new_y="NEXT")
    if right:
        pdf.set_font("Helv", "I", 8.5)
        pdf.set_text_color(*MUTED)
        pdf.cell(0, 4.5, right, new_x="LMARGIN", new_y="NEXT")
    if desc:
        pdf.set_font("Helv", "", 9.5)
        pdf.set_text_color(*INK)
        pdf.multi_cell(0, 5, desc, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(1.8)

def dash(text, bold_head=None):
    pdf.set_font("Helv", "", 9.5)
    pdf.set_text_color(*INK)
    full = ("— " + text) if not bold_head else f"— {bold_head} {text}"
    pdf.multi_cell(0, 5, full, new_x="LMARGIN", new_y="NEXT")

# ---------------- header ----------------
h1("Meriem Beghili")
subtitle("PhD candidate in AI ethics · Sorbonne Université / ISIR–CNRS · Paris, France")
contact("meriem.beghili@sorbonne-universite.fr  ·  meriem.beghili@gmail.com  ·  "
        "ORCID: 0009-0009-8560-560X  ·  linkedin.com/in/meriem-beghili-726046259  ·  meriembeghili.github.io")
rule()

section("Profile")
pdf.set_font("Helv", "", 9.5)
pdf.set_text_color(*INK)
pdf.multi_cell(0, 5,
    "PhD candidate in AI ethics (defense December 2026) working on the ethical issues raised by the use of "
    "social robots in healthcare. I designed a reusable ethical-risk assessment framework for AI systems and "
    "robots deployed in care settings, built on qualitative fieldwork with clinicians, caregivers, and roboticists. "
    "Experienced in cross-disciplinary coordination on funded international projects; six peer-reviewed publications; "
    "talks in three countries; programme committee member, HHAI 2026. Interests extend to AI governance and AI Act "
    "compliance. Working fluently with AI-augmented development tools (Cursor, Hermes, GitHub, agentic automation).",
    new_x="LMARGIN", new_y="NEXT")

section("Education")
entry("PhD in AI ethics — Ethical Issues in the Use of Social Robots in Healthcare",
      "2022 – 2026 (defense December 2026) · Sorbonne Université, Paris",
      "Supervisors: Anouk Barberousse, Mohamed Chetouani. Affiliations: Sciences, Norms, Democracy (SND); "
      "Institute of Intelligent Systems and Robotics (ISIR – CNRS); Sorbonne Center for Artificial Intelligence (SCAI).")
entry("Master's Degree in Philosophy, Biomedical Humanities",
      "2020 – 2022 · Sorbonne Université, Paris",
      "Dissertation: Ethical Issues Related to the Use of Artificial Intelligence in Assisting People with Alzheimer's Disease: The PARO Robot.")
entry("Bachelor's Degree in Philosophy and Biology (Dual Program)",
      "2016 – 2020 · Sorbonne Université, Paris",
      "Interdisciplinary training in life sciences (genetics, molecular biology, neurophysiology) and philosophy "
      "(ethics, philosophy of science, metaphysics).")

section("Research Experience")
entry("Research Engineer — INNOVCARE", "2026 · ISIR (CNRS) — Sorbonne Université, Paris",
      "France 2030 / ANR project on care-led innovation for elderly autonomy, inside a Franco-Japanese consortium. "
      "Interface between humanities research and robotics engineering teams, in a deliverable-driven setting. "
      "Member of the ACIDE team (Action, Cognition, Interaction and Decision Embodied).")
entry("PhD Researcher", "2022 – 2026 · SND / ISIR–CNRS / SCAI — Sorbonne Université",
      "Designed and led the development of a reusable ethical-risk assessment framework for AI systems and robots in "
      "healthcare, applied to systems in use and to prospective cases (PARO, MediXpert). Qualitative fieldwork in care "
      "settings (semi-structured interviews, thematic analysis), identifying use risks designers had not anticipated. "
      "Cross-cutting work with roboticists, clinicians, and partners on INNOVCARE and TAPAS (Franco-Japanese collaboration).")
entry("Research Intern, PIRoS Team", "2021 – 2022 · ISIR (CNRS) — Sorbonne Université",
      "Perception, Interaction, and Social Robotics. Supervisors: Raja Chatila, Mohamed Chetouani.")

section("Teaching Experience")
entry("Course Author and Lecturer — Introduction to the Philosophy of AI",
      "2022 – 2023 · Faculty of Arts and Humanities, Sorbonne Université",
      "Original syllabus, lectures, and assessments for first- and second-year undergraduates (~35 students). "
      "Supervised one guided research project (analysis of the Replika app).")
entry("Teaching Assistant — Ethics and General Philosophy",
      "2022 – 2023 · Faculty of Arts and Humanities, Sorbonne Université",
      "~35 students per course. Supervised three guided research projects (Schrödinger's Cat; Kuhn's Structure of "
      "Scientific Revolutions; On Truth).")

section("Publications — Peer-Reviewed & Forthcoming")
dash("Beghili, M. (2026). Ethical Dimensions of Human–AI Collaboration: A Philosophical Perspective. In: Handbook of Human–AI Collaboration (Chetouani, Nowak & Lukowicz, eds.). Springer. doi:10.1007/978-3-031-61050-9.")
dash("Dhaussy, T., Beghili, M., Chetouani, M., Alami, R. (2026). Assistive Robots for Elder Care: Let Us Not Neglect the Invisible Labour of Care Personnel. RobotPhilosophy 2026, Dublin. hal-05767973.")
dash("Rahimi, H., Cattoni, J., Beghili, M., et al. (2025). Reasoning LLMs for User-Aware Multimodal Conversational Agents. arXiv:2504.01700.")
dash("Beghili, M., Chetouani, M., Barberousse, A. (2024). Ethical Perspectives on Natural Autonomy and Artificial Autonomy. Proceedings of Robophilosophy 2024, IOS Press, pp. 77–84. doi:10.3233/FAIA241491.")
dash("Beghili, M. (2024). L'utilisation des robots sociaux dans le soin : quels enjeux éthiques ? IHM'24, AFIHM, Paris. hal-04490644.")
dash("Tielman, M., et al., Beghili, M., et al. (2026). Positioning Explanations for Trust on Rational vs Human-like Thinking and Behavior. Accepted.")

pdf.add_page()
section("Publications — Under Review & In Progress")
dash("Beghili, M., Chetouani, M., Barberousse, A. Ethical Risk Assessment Approach for Social Robots in Healthcare: Insights from Real and Imaginary Robots. Under review.")
dash("Beghili, M., Pistilli, G., Chetouani, M., Barberousse, A. (2026). Trust in Human–Robot Interaction: Ethical Foundations and the Design of Trustworthy Social Robots in Healthcare. In progress.")
dash("Beghili, M., Tallent, A. (2026). Social Robots Should Not Be Designed for Moral Autonomy, but for Moral Traceability. In progress.")

section("Talks, Panels & Outreach")
dash("“Building Trust in Human–Machine Interaction: Ethical Challenges”, HHAI 2025, MULTITRUST 4.0 workshop, Pisa, June 2025.")
dash("“Ethical Perspectives on Natural Autonomy and Artificial Autonomy”, Robophilosophy 2024, Aarhus, August 2024.")
dash("Panelist, Ethics of Robotics and AI Conference (CERIA), with Serge Tisseron and Aurore Kiesler, Paris, December 2023.")
dash("Panelist, “Ethics and AI”, ISIR, with Daniel Andler and Mohamed Chetouani, Paris, June 2023.")
dash("Doctoral seminar, IHM 2024, Paris (March 2024); OFFRES network seminar, Poitiers (July 2024); GRH seminar, IRCOM, Angers (February 2024).")
dash("3rd Annual INNOVCARE Forum, EHESS, Paris, November 2023.")
dash("Research presentations: Hôpital Broca (2023); TAPAS project meeting, ISIR (2023); SND doctoral students' day (2024).")
dash("“Applying Philosophy of Science and Technology”, Sorbonne Université, March 2024.")
dash("Science Festival, Faculty of Science and Engineering, Sorbonne Université, October 2024.")

section("Academic Service")
dash("Programme Committee Member, 5th International Conference on Hybrid Human–Artificial Intelligence (HHAI 2026).")

section("Skills")
entry("AI-augmented development", None,
      "AI-assisted coding and workflows (Cursor, Hermes); GitHub (version control, collaboration, automation); "
      "prompt engineering; designing and running agentic task automation pipelines.")
entry("AI ethics & governance", None,
      "Ethical risk assessment; AI Act compliance; responsible design of AI systems and social robots; "
      "technology assessment.")
entry("Research methods", None,
      "Qualitative methods (semi-structured interviews, thematic analysis); interdisciplinary literature review "
      "(philosophy, robotics, AI, medicine, sociology, psychology).")
entry("Tools", None, "LaTeX, Overleaf, Zotero; HAL, PhilPapers, Google Scholar, Cairn, JSTOR.")
entry("Languages", None,
      "French (native), English (native), Arabic (intermediate), Spanish (basic).")
entry("Communication", None,
      "Academic writing and public speaking in French and English; science outreach to diverse audiences; "
      "open-access dissemination (HAL).")

section("References")
dash("Anouk Barberousse — Professor, Sorbonne Université · anouk.barberousse@sorbonne-universite.fr")
dash("Mohamed Chetouani — Professor, Sorbonne Université · mohamed.chetouani@sorbonne-universite.fr")
dash("Raja Chatila — Professor, Sorbonne Université · raja.chatila@sorbonne-universite.fr")
dash("Giada Pistilli — Multilingual Team Lead, Mistral · hello@giadapistilli.com")

out = "/Users/meriem/site-meriem/assets/CV_Meriem_Beghili.pdf"
pdf.output(out)
print("written", out)
