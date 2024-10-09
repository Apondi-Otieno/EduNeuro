// script.js

// This will hold the selected persona
let selectedPersona = "";

// Function to fetch lesson content based on selected persona
function fetchLesson(persona) {
    // Use fetch to call the Flask API endpoint
    fetch(`/lesson/${persona}`)
        .then(response => response.json())
        .then(data => {
            // Set the lesson text dynamically
            document.getElementById("lesson-text").innerText = data.lesson;
            document.getElementById("nextLessonBtn").disabled = false;
        })
        .catch(error => console.error("Error fetching lesson:", error));
}

// Event listeners for avatar selection
document.getElementById("avatar1").addEventListener("click", function() {
    selectedPersona = "Calm and Structured Teacher";
    fetchLesson(selectedPersona);
});

document.getElementById("avatar2").addEventListener("click", function() {
    selectedPersona = "Visual Learner’s Guide";
    fetchLesson(selectedPersona);
});

document.getElementById("avatar3").addEventListener("click", function() {
    selectedPersona = "Interactive and Engaging Mentor";
    fetchLesson(selectedPersona);
});

document.getElementById("avatar4").addEventListener("click", function() {
    selectedPersona = "Supportive and Repetitive Teacher";
    fetchLesson(selectedPersona);
});

// Event listener for next lesson button
document.getElementById("nextLessonBtn").addEventListener("click", function() {
    // Here you can either advance to the next part of the lesson or interact further with the avatar
    alert("Next lesson coming soon!");
});
