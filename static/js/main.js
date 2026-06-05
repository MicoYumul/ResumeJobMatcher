// =========================================
// Resume Upload Preview
// =========================================

const resumeInput = document.getElementById("resume");
const uploadBox = document.getElementById("uploadBox");
const uploadText = document.getElementById("uploadText");

if (resumeInput) {
    resumeInput.addEventListener("change", function () {

        if (resumeInput.files.length > 0) {

            const fileName = resumeInput.files[0].name;

            uploadText.innerHTML =
                "✓ Resume Selected<br><br>" +
                fileName;

            uploadBox.classList.add("upload-success");
        }

    });
}


// =========================================
// Theme Toggle
// =========================================

const themeToggle = document.getElementById("themeToggle");

if (themeToggle) {

    if (localStorage.getItem("theme") === "light") {

        document.body.classList.add("light-theme");

        themeToggle.textContent =
            "☀️ Light Mode";
    }

    themeToggle.addEventListener("click", () => {

        document.body.classList.toggle(
            "light-theme"
        );

        if (
            document.body.classList.contains(
                "light-theme"
            )
        ) {

            localStorage.setItem(
                "theme",
                "light"
            );

            themeToggle.textContent =
                "☀️ Light Mode";

        } else {

            localStorage.setItem(
                "theme",
                "dark"
            );

            themeToggle.textContent =
                "🌙 Dark Mode";
        }

    });

}


// =========================================
// Dashboard Charts
// =========================================

console.log("Charts Loading");

const scoreCanvas =
    document.getElementById(
        "scoreChart"
    );

if (
    scoreCanvas &&
    typeof Chart !== "undefined"
) {

    new Chart(scoreCanvas, {

        type: "doughnut",

        data: {

            labels: [
                "Match Score",
                "ATS Score",
                "Resume Quality"
            ],

            datasets: [{
                data: [
                    window.matchScore || 0,
                    window.atsScore || 0,
                    window.qualityScore || 0
                ]
            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {
                    position: "bottom"
                }

            }

        }

    });

}

// =====================================
// Resume Preview Toggle
// =====================================

const togglePreview =
    document.getElementById(
        "togglePreview"
    );

const previewContainer =
    document.getElementById(
        "resumePreviewContainer"
    );

if (
    togglePreview &&
    previewContainer
) {

    togglePreview.addEventListener(
        "click",
        () => {

            if (
                previewContainer.style.display ===
                "none"
            ) {

                previewContainer.style.display =
                    "block";

                togglePreview.textContent =
                    "Hide Preview";

            } else {

                previewContainer.style.display =
                    "none";

                togglePreview.textContent =
                    "Show Preview";
            }

        }
    );
}


// =========================================
// Skills Chart
// =========================================

const skillsCanvas =
    document.getElementById(
        "skillsChart"
    );

if (
    skillsCanvas &&
    typeof Chart !== "undefined"
) {

    new Chart(skillsCanvas, {

        type: "bar",

        data: {

            labels: [
                "Skills Match",
                "Missing Skills"
            ],

            datasets: [{
                label: "Skills Analysis",

                data: [
                    window.skillsMatchScore || 0,
                    window.missingSkillsCount || 0
                ]
            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            scales: {

                y: {
                    beginAtZero: true,
                    max: 100
                }

            }

        }

    });

}