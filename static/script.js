// This will hold the selected persona
let selectedPersona = "";

// Function to fetch lesson content based on selected persona
function fetchLesson(persona) {
    // Use fetch to call the Flask API endpoint
    fetch(`/lesson/${persona}`)
        .then(response => response.json())
        .then(data => {
            // Set the modal content dynamically with the fetched lesson data
            document.getElementById("modal-title").innerText = `Lesson for ${persona}`;
            document.getElementById("modal-text").innerText = data.lesson; // Assuming data.lesson contains the text for the lesson

            // Display the modal
            var modal = document.getElementById("lessonModal");
            modal.style.display = "block";

            // Enable the next lesson button
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

// Close the modal when clicking the "x" button
document.getElementsByClassName("close")[0].onclick = function() {
    var modal = document.getElementById("lessonModal");
    modal.style.display = "none";
}

// Close the modal when clicking outside of the modal content
window.onclick = function(event) {
    var modal = document.getElementById("lessonModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

// Event listener for the "Next Lesson" button
document.getElementById("nextLessonBtn").addEventListener("click", function() {
    alert("Next lesson coming soon!");
    // You can implement functionality for fetching the next lesson here.
});
