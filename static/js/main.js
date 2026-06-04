// =========================================
// Resume Upload Preview
// =========================================

const resumeInput = document.getElementById("resume");
const uploadBox = document.getElementById("uploadBox");
const uploadText = document.getElementById("uploadText");

resumeInput.addEventListener("change", function () {

    if (resumeInput.files.length > 0) {

        const fileName = resumeInput.files[0].name;

        uploadText.innerHTML =
            "✓ Resume Selected<br><br>" +
            fileName;

        uploadBox.classList.add("upload-success");
    }

});







// =====================================
// Theme Toggle
// =====================================

const themeToggle =
    document.getElementById("themeToggle");

if (
    localStorage.getItem("theme") ===
    "light"
) {

    document.body.classList.add(
        "light-theme"
    );

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