document.addEventListener("DOMContentLoaded", function () {
    const passwordInput = document.querySelector('input[name="password"]');

    if (!passwordInput) return;

    const wrapper = document.createElement("div");
    wrapper.className = "password-wrapper";

    passwordInput.parentNode.insertBefore(wrapper, passwordInput);
    wrapper.appendChild(passwordInput);

    const toggleButton = document.createElement("button");
    toggleButton.type = "button";
    toggleButton.className = "toggle-password";
    toggleButton.textContent = "👁️";
    toggleButton.setAttribute("aria-label", "Show password");

    toggleButton.addEventListener("click", function () {
        const isPassword = passwordInput.type === "password";

        passwordInput.type = isPassword ? "text" : "password";
        toggleButton.textContent = isPassword ? "🙈" : "👁️";
        toggleButton.setAttribute(
            "aria-label",
            isPassword ? "Hide password" : "Show password"
        );
    });

    wrapper.appendChild(toggleButton);
});
