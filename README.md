# EduNeuro

<body>
    <div class="container">
        <h2>Login / Sign Up</h2>
        <div>
            <button onclick="showForm('login')">Log In</button>
            <button onclick="showForm('signup')">Sign Up</button>
        </div>
        
        <div id="formContainer">
            <div id="loginForm" class="form hidden">
                <h3>Log In as</h3>
                <select id="roleSelect" onchange="toggleRole()">
                    <option value="teacher">Teacher</option>
                    <option value="student">Student</option>
                </select>
                <form>
                    <input type="text" placeholder="Email" required>
                    <input type="password" placeholder="Password" required>
                    <button type="submit">Log In</button>
                </form>
            </div>

            <div id="signupForm" class="form hidden">
                <h3>Sign Up as</h3>
                <select id="roleSelectSignup" onchange="toggleRoleSignup()">
                    <option value="teacher">Teacher</option>
                    <option value="student">Student</option>
                </select>
                <form>
                    <input type="text" placeholder="Email" required>
                    <input type="password" placeholder="Password" required>
                    <button type="submit">Sign Up</button>
                </form>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>
</html>
