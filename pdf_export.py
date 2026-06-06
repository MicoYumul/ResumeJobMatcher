from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(filepath, data):

    doc = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph("Resume Analysis Report", styles["Title"])
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Predicted Career: {data['predicted_career']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Match Score: {data['match_score']}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"ATS Score: {data['ats_score']}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Resume Quality Score: {data['quality_score']}%",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Resume Grade: {data['resume_grade']}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Hiring Recommendation: {data['hiring_recommendation']}",
            styles["Normal"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph("Matching Skills", styles["Heading2"])
    )

    for skill in data["matching_skills"]:
        content.append(
            Paragraph(f"• {skill}", styles["Normal"])
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph("Missing Skills", styles["Heading2"])
    )

    for skill in data["missing_skills"]:
        content.append(
            Paragraph(f"• {skill}", styles["Normal"])
        )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph("Recommendations", styles["Heading2"])
    )

    for rec in data["recommendations"]:
        content.append(
            Paragraph(f"• {rec}", styles["Normal"])
        )

    doc.build(content)