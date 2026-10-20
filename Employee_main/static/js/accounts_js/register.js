document.addEventListener("DOMContentLoaded", function () {

    const username = document.getElementById("id_username");
    const password = document.getElementById("id_password1");
    const confirmPassword = document.getElementById("id_password2");

    const passwordStatus = document.getElementById("password-status");
    const confirmStatus = document.getElementById("confirm-status");

    // Show / hide password
    window.togglePassword = function (inputId, button) {
        const input = document.getElementById(inputId);

        if (!input) return;

        if (input.type === "password") {
            input.type = "text";
            button.textContent = "🙈";
            button.setAttribute("aria-label", "Hide password");
        } else {
            input.type = "password";
            button.textContent = "👁️";
            button.setAttribute("aria-label", "Show password");
        }
    };

    // Show validation message
    function showStatus(element, message, isValid) {
        if (!element) return;

        element.textContent = message;
        element.className = "validation-message";

        if (message) {
            element.classList.add(
                isValid ? "success-message" : "error-message"
            );
        }
    }

    // Password validation
    function validatePassword() {
        if (!password || !username) return false;

        const value = password.value;
        const usernameValue = username.value.trim();

        if (!value) {
            showStatus(passwordStatus, "", false);
            validateConfirmPassword();
            return false;
        }

        const checks = [
            {
                valid: value.length >= 8,
                message: "Use at least 8 characters."
            },
            {
                valid: !/^\d+$/.test(value),
                message: "Password cannot contain only numbers."
            },
            {
                valid: !usernameValue ||
                    !value.toLowerCase().includes(usernameValue.toLowerCase()),
                message: "Password should not contain your username."
            }
        ];

        const failed = checks.filter(check => !check.valid);

        if (failed.length > 0) {
            showStatus(
                passwordStatus,
                failed.map(check => check.message).join(" "),
                false
            );
        } else {
            showStatus(
                passwordStatus,
                "Basic password checks passed. Django will check the remaining rules.",
                true
            );
        }

        validateConfirmPassword();

        return failed.length === 0;
    }

    // Confirm password validation
    function validateConfirmPassword() {
        if (!password || !confirmPassword) return false;

        const confirmValue = confirmPassword.value;

        if (!confirmValue) {
            showStatus(confirmStatus, "", false);
            return false;
        }

        if (confirmValue === password.value) {
            showStatus(confirmStatus, "Passwords match.", true);
            return true;
        }

        showStatus(confirmStatus, "Passwords do not match.", false);
        return false;
    }

    // Validate while typing
    if (password) {
        password.addEventListener("input", validatePassword);
    }

    if (confirmPassword) {
        confirmPassword.addEventListener("input", validateConfirmPassword);
    }

    if (username) {
        username.addEventListener("input", function () {
            if (password && password.value) {
                validatePassword();
            }
        });
    }

});
